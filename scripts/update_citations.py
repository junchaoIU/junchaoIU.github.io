#!/usr/bin/env python3
"""Fetch Google Scholar citation data via SerpApi and update citations.json."""

import json
import os
import re
import sys
from serpapi import GoogleSearch

GS_USER_ID = "jhLZtgYAAAAJ"

# Map paper titles on the homepage to Google Scholar titles (normalize)
PAPER_TITLES = [
    "Neuron-Aware Data Selection in Instruction Tuning for Large Language Models",
    "DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection",
    "RepreGuard: Detecting LLM-Generated Text by Revealing Hidden Representation Patterns",
    "DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios",
    "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions",
    "UniRRM: Unified Reasoning Reward Models Across Languages and Evaluation Paradigms",
    "Understanding and Mitigating Political Stance Cross-topic Generalization in Large Language Models",
    "LongDocSpan: Extending LVLMs for Long Document Understanding",
    "Domain Adaptive Machine Translation with Synthetic Feedback for Large Language Models",
    "Who Wrote This? The Key to Zero-Shot LLM-Generated Text Detection Is GECScore",
    "Benchmarking the Detection of LLMs-Generated Modern Chinese Poetry",
    "Is Long-to-Short a Free Lunch? Investigating Inconsistency and Reasoning Efficiency in LRMs",
    "Why Do Metrics Think That? Towards Understanding Large Language Models as Machine Translation Evaluators",
    "Overview of CCL25-Eval Task 4: Factivity Inference Evaluation 2025",
    "Overview of the NLPCC 2025 Shared Task 1: LLM-Generated Text Detection",
    "Understanding Aha Moments: From External Observations to Internal Mechanisms",
    "Rethinking Prompt-based Debiasing in Large Language Models",
    "Fraud-R1: A Multi-Round Benchmark for Assessing the Robustness of LLM Against Augmented Fraud and Phishing Inducements",
    "Human-in-the-loop Machine Translation with Large Language Model",
    "The Canton Canon Digital Library Based on Knowledge Graph",
]


def normalize(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()


def title_match(gs_title, homepage_title):
    """Match by checking if one title contains the other as substring (after normalization)."""
    gs_norm = " ".join(normalize(gs_title))
    hp_norm = " ".join(normalize(homepage_title))
    if not gs_norm or not hp_norm:
        return False
    # Exact match (normalized)
    if gs_norm == hp_norm:
        return True
    # Substring containment (one is prefix of the other)
    if gs_norm in hp_norm or hp_norm in gs_norm:
        return True
    # Word overlap >= 80% of the shorter title
    gs_words = set(normalize(gs_title))
    hp_words = set(normalize(homepage_title))
    overlap = len(gs_words & hp_words)
    shorter = min(len(gs_words), len(hp_words))
    return shorter > 0 and overlap / shorter >= 0.85


def fetch_author_profile():
    params = {
        "engine": "google_scholar_author",
        "author_id": GS_USER_ID,
        "hl": "en",
        "api_key": os.environ.get("SERPAPI_API_KEY", ""),
    }
    search = GoogleSearch(params)
    return search.get_dict()


def fetch_papers():
    params = {
        "engine": "google_scholar_author",
        "author_id": GS_USER_ID,
        "hl": "en",
        "sort": "pubdate",
        "start": "0",
        "num": "100",
        "api_key": os.environ.get("SERPAPI_API_KEY", ""),
    }
    search = GoogleSearch(params)
    return search.get_dict()


def main():
    api_key = os.environ.get("SERPAPI_API_KEY", "")
    if not api_key:
        print("ERROR: SERPAPI_API_KEY not set")
        sys.exit(1)

    print("Fetching author profile...")
    profile = fetch_author_profile()

    total_citations = 0
    h_index = 0

    cited_by = profile.get("cited_by", {})
    table = cited_by.get("table", [])
    for row in table:
        # Try multiple key formats
        for cite_key in ["citations", "cited_by"]:
            val = row.get(cite_key, {})
            if isinstance(val, dict) and val.get("all"):
                total_citations = int(val["all"])
                break
        for h_key in ["hindex", "h_index", "h-index"]:
            val = row.get(h_key, {})
            if isinstance(val, dict) and val.get("all"):
                h_index = int(val["all"])
                break
        # Direct numeric values
        if "citations" in row and isinstance(row["citations"], int):
            total_citations = int(row["citations"])
        if "hindex" in row and isinstance(row["hindex"], int):
            h_index = int(row["hindex"])

    # Fallback: check cited_by directly
    if not total_citations:
        total_citations = int(cited_by.get("total", 0)) if cited_by.get("total") else 0
    if not h_index:
        h_index = int(profile.get("h_index", 0)) if profile.get("h_index") else 0

    print(f"Total citations: {total_citations}")
    print(f"h-index: {h_index}")
    print(f"Debug - cited_by keys: {list(cited_by.keys())}")
    print(f"Debug - table rows: {len(table)}")
    for i, row in enumerate(table):
        print(f"  Row {i}: {row}")

    print("Fetching papers...")
    papers_data = fetch_papers()
    articles = papers_data.get("articles", [])

    # Build GS title -> citations map
    gs_map = {}
    for article in articles:
        gs_title = article.get("title", "")
        gs_cite = article.get("cited_by", {}).get("value", 0)
        gs_authors = article.get("authors", "")
        gs_map[gs_title] = {
            "cite": int(gs_cite) if gs_cite else 0,
            "authors": gs_authors,
        }

    paper_citations = {}
    first_author_total = 0
    used_gs_titles = set()

    # First pass: exact (normalized) matches
    for hp_title in PAPER_TITLES:
        hp_norm = " ".join(normalize(hp_title))
        for gs_title, info in gs_map.items():
            if gs_title in used_gs_titles:
                continue
            gs_norm = " ".join(normalize(gs_title))
            if gs_norm == hp_norm:
                paper_citations[hp_title] = info["cite"]
                used_gs_titles.add(gs_title)
                first_author_field = info["authors"].split(",")[0].strip().lower() if info["authors"] else ""
                if "j wu" in first_author_field or "junchao wu" in first_author_field or "wu j" in first_author_field:
                    first_author_total += info["cite"]
                break

    # Second pass: substring matches
    for hp_title in PAPER_TITLES:
        if hp_title in paper_citations:
            continue
        hp_norm = " ".join(normalize(hp_title))
        best_match = None
        for gs_title, info in gs_map.items():
            if gs_title in used_gs_titles:
                continue
            gs_norm = " ".join(normalize(gs_title))
            if hp_norm in gs_norm or gs_norm in hp_norm:
                best_match = gs_title
                break
        if best_match:
            info = gs_map[best_match]
            paper_citations[hp_title] = info["cite"]
            used_gs_titles.add(best_match)
            first_author_field = info["authors"].split(",")[0].strip().lower() if info["authors"] else ""
            if "j wu" in first_author_field or "junchao wu" in first_author_field or "wu j" in first_author_field:
                first_author_total += info["cite"]

    # Third pass: high-overlap fuzzy matches
    for hp_title in PAPER_TITLES:
        if hp_title in paper_citations:
            continue
        hp_words = set(normalize(hp_title))
        best_match = None
        best_score = 0
        for gs_title, info in gs_map.items():
            if gs_title in used_gs_titles:
                continue
            gs_words = set(normalize(gs_title))
            overlap = len(hp_words & gs_words)
            shorter = min(len(hp_words), len(gs_words))
            score = overlap / shorter if shorter > 0 else 0
            if score > best_score and score >= 0.85:
                best_score = score
                best_match = gs_title
        if best_match:
            info = gs_map[best_match]
            paper_citations[hp_title] = info["cite"]
            used_gs_titles.add(best_match)
            first_author_field = info["authors"].split(",")[0].strip().lower() if info["authors"] else ""
            if "j wu" in first_author_field or "junchao wu" in first_author_field or "wu j" in first_author_field:
                first_author_total += info["cite"]

    for title in PAPER_TITLES:
        if title not in paper_citations:
            paper_citations[title] = 0

    data = {
        "totalCitations": total_citations,
        "hIndex": h_index,
        "firstAuthorCitations": first_author_total,
        "papers": paper_citations,
    }

    os.makedirs("data", exist_ok=True)
    with open("data/citations.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Updated data/citations.json with {len(paper_citations)} papers")
    print(f"First-author citations: {first_author_total}")
    for title, cite in sorted(paper_citations.items(), key=lambda x: -x[1]):
        print(f"  {cite:4d} | {title}")


if __name__ == "__main__":
    main()
