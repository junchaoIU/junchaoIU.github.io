---
permalink: /
title: "WU JUNCHAO"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

- I am [WU JUNCHAO](https://junchaoiu.github.io) (吴俊潮). Currently, I am a second-year Ph.D. student in Computer Science at [NLP2CT Lab](http://nlp2ct.cis.umac.mo/), [University of Macau](https://www.um.edu.mo/), fortunately advised by [Prof. Derek F. Wong](https://www.fst.um.edu.mo/personal/derek-wong/). Previously, I completed my M.S. in Data Science (Computational Lingustics) at the same lab, co-advised by [Prof. Derek F. Wong](https://www.fst.um.edu.mo/personal/derek-wong/) and [Prof. Yuan Yulin](https://fah.um.edu.mo/yuan-yulin/). I achineved my bachelor's degree at Beijing Normal University, Zhuhai, supervised by [Prof. JiangYing](https://rsgyy.bnu.edu.cn/yjjg/glcxyjzx/glcxyjzxrcdw/97671.html) and [Prof. Yangjing](https://rsgyy.bnu.edu.cn/yjjg/yykxyjzx/rcdw2/97903.html). 
- My current research interests are Natural Language Processing, Machine Translation and Trustworthy AI. Please feel free to contact me via email!

Research Overview
======
My core research centers on **explainable, trustworthy, and secure large language models (LLMs)**, with a primary focus on LLM-generated text detection and effecient model post-training.
​
- **LLM-Generated Text Detection & Benchmarking**: To address the opacity of AI-generated content, I developed detection frameworks that leverage intrinsic differences between human and model text, specifically in grammatical features [COLING'25] and hidden representation patterns [TACL'25]. I also constructed leading benchmarks tailored to real-world scenarios [NeurIPS'24] and specialized domains, such as modern Chinese poetry [EMNLP'25], and organized the NLPCC 2025 shared task on this topic [NLPCC'25]. Additionally, I published a systematic survey [Computational Linguistics'24] that highlights the field’s key challenges and future directions.​

- **Effecient and Controllable LLM Tuning & Reasoning**: I also focus on efficient, controllable, and explainable LLM post-training and reasoning to optimize model reliability. I developed a neuron-aware data selection framework [ICLR'26] for efficient instruction tuning, which reduces dataset redundancy and bias by aligning training data with target domain neuron activation patterns. Collaboratively, I investigated internal reasoning mechanisms of LLMs, including "aha moments" in complex problem-solving [TACL'26] and inconsistencies in long-to-short text conversion [arXiv'25], to enhance model trustworthiness.
​
- **Collaborative Research on Multilingual & Safety**: I also engage in collaborative research on related directions, including: 1) domain-adaptive machine translation [TALLIP'26], where synthetic feedback is used to improve alignment with specialized terminology; 2) multimodal long-document understanding [CVPR'26], achieved by extending vision-language models (LVLMs) with segment-wise attention; and 3) LLM safety & ethics [ACL'25; EMNLP'25], covering debiasing optimization, resistance to fraud/phishing inducements, and implicit risk identification.

News
======
- [2026-03-14] One paper accepted by **CVPR 2026 Findings** as Co-author: **LongDocSpan: Extending LVLMs for Long Document Understanding**.
- [2026-01-27] One paper accepted by **ICLR 2026** as Co-first author: [Neuron-Aware Data Selection in Instruction Tuning for Large Language Models](https://openreview.net/forum?id=uq6UWRgzMr). We propose the NAIT framework, which selects optimal instruction tuning data samples by evaluating the impact of IT data on LLMs performance by analyzing the similarity of neuron activation patterns between the IT dataset and the target domain capability. 
- [2026-01-05] One paper accepted by **ACM Transactions on Asian and Low-Resource Language Information Processing (TALLIP)** as Co-author. Congratulations to Xinyi and all Co-authors!
- [2025-08-21] Two paper accepted by **EMNLP 2025 Findings** as Co-author. And our CL paper [A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions](https://arxiv.org/abs/2310.14724) and TACL paper [RepreGuard: Detecting LLM-Generated Text by Revealing Hidden Representation Patterns](https://arxiv.org/abs/2508.13152) will also oral present in **EMNLP 2025**. See you in Suzhou!!!
  - *[Can Large Language Models Identify Implicit Suicidal Ideation? An Empirical Evaluation](https://arxiv.org/abs/2502.17899)*. 
  <!-- We introduce Fraud-R1, a benchmark evaluating LLMs' ability to resist internet fraud through 8,564 real-world cases, uncovering significant challenges in role-play scenarios and a performance gap between Chinese and English. -->
  - *[Benchmarking the Detection of LLMs-Generated Modern Chinese Poetry](https://arxiv.org/abs/2509.01620)*. 
- [2025-08-01] One Paper accepted by **Transactions of the Association for Computational Linguistics (TACL)** as Co-first author: *[RepreGuard: Detecting LLM-Generated Text by Revealing Hidden Representation Patterns](https://arxiv.org/abs/2508.13152)*. We propose RepreGuard, a low-overhead, highly generalizable, and interpretable detector, based on the observation that there are significant differences in neural activation patterns when LLMs process LLM-generated text versus human-written text.
- [2025-06-27] One Evaluation Paper accepted by **CCL 2025 Evaluation Workshop** as Co-author: *[Overview of CCL25-Eval Task 4: Factivity Inference Evaluation 2025]()*, we will update the paper in arxiv soon~
<!-- - [2025-06-20] One Paper accepted by **Actionable Interpretability Workshop @ICML 2025** as Co-author: *[Why Do Metrics Think That? Towards Understanding Large Language Models as Machine Translation Evaluators]()*. -->
- [2025-06-13] One Evaluation Paper accepted by **NLPCC 2025** as First-author, *[Overview of the NLPCC 2025 Shared Task 1: LLM-Generated Text Detection]()*. We provide a comprehensive overview of the task, including the dataset, task design, evaluation results, and an in-depth analysis of the submitted solutions.
- [2025-05-16] Two paper accepted by **ACL 2025 Findings** as Co-author. Congratulations to Shu🌳, Xinyi, and all Co-authors!
  - *[Fraud-R1: A Multi-Round Benchmark for Assessing the Robustness of LLM Against Augmented Fraud and Phishing Inducements](https://arxiv.org/abs/2502.12904)*. 
  <!-- We introduce Fraud-R1, a benchmark evaluating LLMs' ability to resist internet fraud through 8,564 real-world cases, uncovering significant challenges in role-play scenarios and a performance gap between Chinese and English. -->
  - *[Rethinking Prompt-based Debiasing in Large Language Models](https://arxiv.org/abs/2503.09219)*. 
  <!-- We investigate bias in LLMs, revealing that prompt-based methods often provide superficial results, with flawed metrics and evaluation settings leading to misclassifications and evasive answers, highlighting the need to rethink bias metrics for trustworthy AI. -->
- [2025-04-03] Our new preprint *[Understanding Aha Moments: from External Observations to Internal Mechanisms](https://arxiv.org/abs/2504.02956)* released. We reveal that "aha moments" help LRMs solve complex problems by using anthropomorphic language, adjusting uncertainty, and preventing reasoning collapse, while internally balancing self-reflection with reasoning and adapting to task difficulty.

<!-- 这是一个注释，读者看不到 
- [2025-03-04] 🔥 We’re excited to announce a shared task at NLPCC 2025: [LLM-Generated Text Detection](https://github.com/NLP2CT/NLPCC-2025-Task1) !!! This task focuses on Chinese and offers a great opportunity to explore unique findings compared to English detection. Join us and create your own detector now! 🚀
- [2024-11-31] One paper accepted by **COLING 2025** as First-author: *[Who Wrote This? The Key to Zero-Shot LLM-Generated Text Detection Is GECScore](https://arxiv.org/abs/2405.04286)*. We introduce a novel black-box zero-shot method for detecting LLM-generated text, called GECScore 🔍. This method is remarkably simple yet effective, based on the observation that LLMs tend to prefer grammatically correcting human-written text over LLM-generated text.
- [2024-11-28] One paper accepted by **Computational Linguistics (CL)** as First-author: *[A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions](https://arxiv.org/abs/2310.14724)*. This survey offers a comprehensive overview of the latest advancements in LLM-generated text detection, highlighting the urgent need for more robust methods. It reviews mainstream approaches, addresses key challenges, and outlines promising future research directions. The paper serves as both a clear introduction for newcomers and a valuable resource for experts seeking updates in the field.
- [2024-09-27] One paper accepted by **NeurIPS 2024** as First-author: *[DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios](https://openreview.net/forum?id=ZGMkOikEyv)*. We introduce a new benchmark, **DetectRL**, which covers multiple realistic scenarios, including usage of various prompts, human revisions of LLM-generated text, adversarial spelling errors, taking measures to attack detectors, etc., provide real utility to researchers on the topic and practitioners looking for consistent evaluation methods.
-->

<!-- 这是一个注释，读者看不到 - [2023-12-23] Really excited that my girlfriend and I published our first paper. It is worth commemorating this moment. Welcome to access it: *[Evolutionary game analysis of prefabricated buildings adoption under carbon emission trading scheme](https://www.sciencedirect.com/science/article/pii/S0360132323011484)*. -->
<!-- 这是一个注释，读者看不到 - [2023-10-23] Our survey paper on **LLM-generated Text Detection** is now available on arxiv: *[A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions](https://arxiv.org/abs/2310.14724)*. -->
<!-- 这是一个注释，读者看不到 - [2023-10-13] One paper accepted by **MT Summit 2023** as Co-author, and is now available on arxiv: *[Human-in-the-loop Machine Translation with Large Language Model](https://arxiv.org/abs/2310.08908)*.  -->

Publications
======
{% include base_path %}
{% for post in site.publications reversed %}
  {% include archive-single-publications.html %}
{% endfor %}

<br/>

Services
======
- Conference Reviewer: ACL ARR, ICML, ICLR, NeurIPS, AAAI, CVPR, COLM, CCL, NLPCC
- Journal Reviewer: Proc. IEEE, ACM Computing Surveys, IEEE TIFS, ACM TALLIP, ACM TIST
- Student Volunteer: MT Summit 2023
- Teaching Assistant
  - Computational Linguistics (MSc) programme (2023 Fall)
  - AHGC7315 Language and Linguistics (2023 Spring)

Experience
======
- Alibaba Cloud, Alibaba Group - LLM Research Intern (Feb. 2026 - Present), Supervised by [Yichao Du](https://duyichao.github.io/) and [Longyue Wang](https://www.longyuewang.com/).
- Alibaba International, Alibaba Group - LLM Research Intern (Jul. 2025 - Jan. 2026), Supervised by [Yichao Du](https://duyichao.github.io/), [Yefeng Liu](https://openreview.net/profile?id=~Yefeng_Liu4) and [Longyue Wang](https://www.longyuewang.com/).
- PRADA Lab, King Abdullah University of Science and Technology (KAUST) - Visiting Research Intern (Mar. 2025 - Jun. 2025), Supervised by [Prof. Di Wang](https://shao3wangdi.github.io/).



<!-- 
Awards
======
- Outstanding graduate of Beijing Normal University,Zhuhai, 2022
- The Outstanding Graduation Thesis of Beijing Normal University, Zhuhai, 2022
- Professional Scholarship of Beijing Normal University, Zhuhai, 2019, 2020, 2021
- Academic Scholarship of Beijing Normal University, Zhuhai, 2021
- Outstanding student cadre Honor of Beijing Normal University, Zhuhai, 2019, 2020
- National Second Prize & Guangdong First Prize in the 7th Teddy Cup Data Mining Challenge (Title: Analysis of Safe Driving Behavior of Transport Vehicles), 2019
- First Prize in China University Students Mathematical Contest in Modeling, Guangdong Division (Title: Credit Decisions of Small, Medium and Micro Enterprises), 2020
- Best Presentation Award in the 10th IEEE International Conference on Education and Information Technology, ICEIT 2021
- Third Prize in the 8th "Challenge Cup" College Students' Extracurricular Academic Science and Technology Works Competition in Beijing Normal University, Zhuhai, 2020
- Third Prize in the 2nd Guangdong-Hong Kong-Macau College Student Public Administration Data Analysis Contest, 2022
-->


Professional skills
======
* English Level: IELTS(6.5), CET-6(507)
* Programming Languages: C, Python, Java, JavaScript, SQL, Bash
* Development Frameworks: SpringBoot, React.js, Flask
* Deep Learning Tools: Scikit-learn, PyTorch, Fairseq, Transformers
* DB Tools: Neo4j, MySQL, Oracle DB
* Other Tools: WebLogic, Apache Ant, Jena, Git

Others
======
- 🎓 If you are also interested in natural language processing and machine translation, you can follow my lab and lab members: [NLP2CT LAB](http://nlp2ct.cis.um.edu.mo/), I love them.
- ✨[Zhan Runzhe](https://runzhe.me/) is my current advisor, who focus on machine translation and LLMs. He is a brilliant scientist and one of the nicest people I have ever met.
- 🌈[Chen Xin](https://github.com/Chen-X666) is one of my best friends, who is presently a PhD student at Nanjing University and is also committed to NLP research., he has many interesting dreams.

<a href="https://info.flagcounter.com/kvwb"><img src="https://s11.flagcounter.com/count/kvwb/bg_FFFFFF/txt_000000/border_CCCCCC/columns_5/maxflags_15/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
