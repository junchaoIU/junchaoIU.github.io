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
    gs_words = set(normalize(gs_title))
    hp_words = set(normalize(homepage_title))
    if not gs_words or not hp_words:
        return False
    overlap = len(gs_words & hp_words)
    return overlap / min(len(gs_words), len(hp_words)) >= 0.6


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
        if row.get("citations", {}).get("all"):
            total_citations = int(row["citations"]["all"])
        if row.get("hindex", {}).get("all"):
            h_index = int(row["hindex"]["all"])

    print(f"Total citations: {total_citations}")
    print(f"h-index: {h_index}")

    print("Fetching papers...")
    papers_data = fetch_papers()
    articles = papers_data.get("articles", [])

    paper_citations = {}
    first_author_total = 0

    for article in articles:
        gs_title = article.get("title", "")
        gs_cite = article.get("cited_by", {}).get("value", 0)
        gs_authors = article.get("authors", "")

        for hp_title in PAPER_TITLES:
            if title_match(gs_title, hp_title):
                cite = int(gs_cite) if gs_cite else 0
                paper_citations[hp_title] = cite
                first_author_field = gs_authors.split(",")[0].strip().lower() if gs_authors else ""
                if "j wu" in first_author_field or "junchao wu" in first_author_field or "wu j" in first_author_field:
                    first_author_total += cite
                break

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


if __name__ == "__main__":
    main()
