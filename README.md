# Ahmed-Hamdy / Graduation-Portfolio
<div align="center">

# 🧠 AI Linguistics & Prompt Engineering Portfolio

### Graduation Capstone — Motrjim Academy | AI Linguistics & Prompt Engineering Diploma

**Where linguistic precision meets AI engineering** — five applied tasks spanning prompt engineering, ISO-compliant translation systems, data cleaning, dataset annotation, and AI safety evaluation under the EU AI Act.

**Tools:** Python 3.12 · Google AI Studio · Label Studio
**Standards:** ISO 17100 · 18587 · 9001 · EU AI Act · NIST AI RMF 1.0

**Email:** [PLACEHOLDER — أرسل الإيميل] · **LinkedIn:** [Connect](https://www.linkedin.com)

</div>

---

## 📑 Table of Contents

- [📊 At a Glance](#-at-a-glance)
- [👤 About Me](#-about-me)
- [📖 Repository Overview](#-repository-overview)
- [🧭 Frameworks & Standards Applied](#-frameworks--standards-applied)
- [📂 Portfolio Tasks](#-portfolio-tasks)
- [🛠️ Tools & Technologies](#️-tools--technologies)
- [💡 Key Learnings](#-key-learnings)
- [🗂️ Repository Structure](#️-repository-structure)
- [📬 Contact](#-contact)

---

## 📊 At a Glance

<div align="center">

**21** Prompt Strategies · **11** Vulnerabilities Documented · **7** International Frameworks Applied
**36** Annotated Tasks · **2** Datasets Cleaned & Reproducible · **0** Empty Annotations

</div>

---

## 👤 About Me

I'm **Ahmed**, an AI Linguist and legal translation specialist working at the intersection of linguistics and AI engineering. Before this diploma, I built and maintained a proprietary legal-translation quality framework with **90+ documented error categories** — a background that directly shaped how I approached every task in this portfolio: not as isolated exercises, but as an extension of the same discipline of precision, reproducibility, and documented decision-making I already apply professionally.

This portfolio documents five hands-on capstone tasks, each designed to prove **reproducible, production-ready output** — not theory: prompts that actually work, datasets cleaned with documented decisions, annotations exported in spec-compliant formats, and a safety evaluation that surfaced real, structural weaknesses across two AI systems.

---

## 📖 Repository Overview

This repository contains my graduation portfolio for the **AI Linguistics & Prompt Engineering Diploma — Motrjim Academy (2026)**, demonstrating practical, end-to-end application of:

- Prompt Engineering (legal & financial domains)
- ISO-Compliant Translation Systems
- Data Cleaning & Preprocessing
- Dataset Annotation via Label Studio
- AI Red Teaming & Safety Evaluation (EU AI Act)

Each task folder includes complete documentation, implementation files, actual outputs, and supporting reports — reproducible from scratch, not just described.

---

## 🧭 Frameworks & Standards Applied

A core differentiator of this portfolio: every task is grounded in a named, verifiable international standard — not general best practice.

| Framework | Applied In |
|---|---|
| **ISO 17100** — Translation Services Requirements | Task 02 |
| **ISO 18587** — Post-Editing of Machine Translation | Task 02 |
| **ISO 9001** — Quality Management Systems | Task 02 |
| **EU AI Act** (Regulation 2024/1689) | Task 05 |
| **NIST AI RMF 1.0** — AI Risk Management Framework | Task 05 |
| **OWASP LLM Top 10** | Task 05 |
| **MITRE ATLAS** — Adversarial Threat Landscape for AI | Task 05 |

---

## 📂 Portfolio Tasks

| # | Task | What I Did | Key Result | Folder |
|---|------|-----------|-------------|--------|
| 🧩 **01** | **Master Prompt Engineering** | Designed reusable Master Prompts for **legal contract translation** and **financial statement analysis**, applying role/persona, few-shot, chain-of-thought, decomposition, and anti-hallucination strategies. | **21 strategies**, each explicitly mapped to purpose | [`01_master_prompt`](./01_master_prompt/) |
| 🌐 **02** | **ISO Prompt Lab** | Built an ISO-aligned System Instruction in Google AI Studio for translation — embedding a **mandatory second-linguist review step** (ISO 17100), MTPE handling (ISO 18587), and consistency controls (ISO 9001). Domain-agnostic by design. | Explicit clause-by-clause ISO mapping | [`02_iso_prompt_lab`](./02_iso_prompt_lab/) |
| 🧹 **03** | **Data Cleaning Pipeline** | Cleaned two deliberately "dirty" datasets — a legal termbase and a company ledger — resolving duplicates, mojibake encoding, inconsistent dates/currencies, and malformed rows, via a fully reproducible Python script. | **106→96** and **50→47** rows, zero duplicates | [`03_data_cleaning`](./03_data_cleaning/) |
| 🏷️ **04** | **Label Studio Annotation** | Ran two parallel annotation projects: **Legal NER** (10 entity types incl. CASE, JURISDICTION, LAW_STATUTE) and **Prompt Classification** (technique, quality, and risk scoring with justification). | **36/36 tasks** annotated, zero left empty | [`04_label_studio`](./04_label_studio/) |
| 🛡️ **05** | **AI Red Teaming (EU AI Act)** | Structured adversarial testing of an AI conversational system across two independent sessions, uncovering a **repeating structural pattern** — human-oversight bypass and identity-based bias — across two unrelated domains. | **11 documented findings** ([full report](./05_red_teaming/red_teaming_documentation.json)) — more than double the required minimum | [`05_red_teaming`](./05_red_teaming/) |

---

## 🛠️ Tools & Technologies

**Artificial Intelligence**
`Prompt Engineering` · `AI Evaluation` · `AI Red Teaming` · `Google AI Studio (Gemini)`

**Programming & Data**
`Python` · `Pandas` · `Google Colab` · `JSON` · `Microsoft Excel`

**Annotation**
`Label Studio` · `NER` · `Multi-label Classification`

**Translation & Linguistics**
`Legal Translation` · `Financial Translation` · `Terminology Management` · `ISO 17100 / 18587 / 9001`

**Documentation & Workflow**
`Markdown` · `Git` · `GitHub`

---

## 💡 Key Learnings

1. **Quantitative honesty is a discipline, not a formality.** Early drafts of my prompt-strategy table over-counted techniques through double-labeling. Catching and correcting this taught me to verify every claimed capability against actual evidence in the output — not assume it.

2. **A refusal is only as strong as its understanding of *why*.** During red teaming, one system refused a harmful request cleanly — then reversed itself completely under a six-word rephrasing of the *same* request. That taught me safety behavior built on surface pattern-matching is fragile in a way that's more dangerous than having no refusal at all, because it creates false confidence.

3. **Reproducibility is the real deliverable, not the output itself.** A clean dataset or a passing prompt means little without the documented decisions behind it (why a row was dropped, why a term was chosen). I treated every "why" as part of the deliverable, not an afterthought.

4. **Cross-domain repetition is stronger evidence than a single finding.** The same two failure patterns (oversight bypass, identity-based bias) surfaced independently in a financial scenario and a medical scenario. That cross-domain repetition — not any single finding — is what makes a red-teaming report credible rather than anecdotal.

---

## 🗂️ Repository Structure

```text
ai-linguistics-graduation-portfolio/
├── README.md
├── 01_master_prompt/
├── 02_iso_prompt_lab/
├── 03_data_cleaning/
├── 04_label_studio/
├── 05_red_teaming/
│   ├── red_teaming_documentation.json
│   └── evidence/
└── assets/
```

---

## 📬 Contact

- 📧 **Email:** [PLACEHOLDER — أرسل الإيميل]
- 💼 **LinkedIn:** [linkedin.com/in/your-profile](https://www.linkedin.com)

---

<div align="center">

*Artificial intelligence becomes trustworthy only when paired with linguistic precision, documented reasoning, and rigorous evaluation.*

**Motrjim Academy — AI Linguistics & Prompt Engineering Diploma · Graduation Capstone 2026**

</div>
