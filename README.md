# Ahmed-Hamdy / Graduation-Portfolio
<div align="center">

# 🧠 AI Linguistics & Prompt Engineering Portfolio

### Graduation Capstone — Motrjim Academy | AI Linguistics & Prompt Engineering Diploma

**Where linguistic precision meets AI engineering** — five applied tasks spanning prompt engineering, ISO-compliant translation systems, data cleaning, dataset annotation, and AI safety evaluation under the EU AI Act.

**Tools:** Python 3.12 · Google AI Studio · Label Studio
**Standards:** ISO 17100 · 18587 · 9001 · EU AI Act · NIST AI RMF 1.0

</div>

---

## 📑 Table of Contents

- [📊 At a Glance](#-at-a-glance)
- [👤 About Me](#-about-me)
- [🧭 How to Navigate This Repository](#-how-to-navigate-this-repository)
- [🧭 Frameworks & Standards Applied](#-frameworks--standards-applied)
- [📂 Portfolio Tasks](#-portfolio-tasks)
- [🛠️ Tools & Technologies](#️-tools--technologies)
- [💡 What This Project Reinforced](#-what-this-project-reinforced)
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

I'm **Ahmed Hamdy**, a legal translator working in AI engineering and prompt design. Before this program, I applied my own quality-review process to legal translation work — checking every output against evidence rather than assuming it's correct. This portfolio carries that same habit into five different tasks: designing prompts, building an ISO-aligned translation workflow, cleaning real datasets, running structured annotation, and testing two AI systems for safety risks under the EU AI Act.

The results below are documented with specific numbers, not general claims: 21 prompt strategies, each verified against the prompt text itself; two datasets cleaned with every removed row logged and explained; 36 annotation tasks completed with none left blank; and 11 safety findings, traced across two separate test sessions until the same underlying weakness appeared in two unrelated domains.

---

## 🧭 How to Navigate This Repository

Each task folder is self-contained: open it, and the working artifact (a prompt file, a cleaned dataset, an annotation export, the red-teaming JSON) is what to look at first — the supporting report explains the decisions behind it, not the other way around. The table below links directly to that artifact for each task, so you don't have to dig through folders to find it.

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

| # | Task | Approach | Outcome | Folder |
|---|------|-----------|-------------|--------|
| 🧩 **01** | **Master Prompt Engineering** | Designed reusable Master Prompts for **legal contract translation** and **financial statement analysis**, applying role/persona, few-shot, chain-of-thought, decomposition, and anti-hallucination strategies. | **21 strategies**, each explicitly mapped to purpose | [`01_master_prompt`](./01_master_prompt/) |
| 🌐 **02** | **ISO Prompt Lab** | Built an ISO-aligned System Instruction in Google AI Studio for translation — embedding a **mandatory second-linguist review step** (ISO 17100), MTPE handling (ISO 18587), and consistency controls (ISO 9001). Domain-agnostic by design. | Explicit clause-by-clause ISO mapping | [`02_iso_prompt_lab`](./02_iso_prompt_lab/) |
| 🧹 **03** | **Data Cleaning Pipeline** | Cleaned two deliberately "dirty" datasets — a legal termbase and a company ledger — resolving duplicates, mojibake encoding, inconsistent dates/currencies, and malformed rows, via a fully reproducible Python script. | **106→96** and **50→47** rows, zero duplicates | [`03_data_cleaning`](./03_data_cleaning/) |
| 🏷️ **04** | **Label Studio Annotation** | Ran two parallel annotation projects: **Legal NER** (10 entity types incl. CASE, JURISDICTION, LAW_STATUTE) and **Prompt Classification** (technique, quality, and risk scoring with justification). | **36/36 tasks** annotated, zero left empty | [`04_label_studio`](./04_label_studio/) |
| 🛡️ **05** | **AI Red Teaming (EU AI Act)** | Structured adversarial testing of an AI conversational system across two independent sessions, uncovering a **repeating structural pattern** — human-oversight bypass and identity-based bias — across two unrelated domains. | **11 documented findings** ([full report](./05_red_teaming/red_teaming_documentation.json)) — more than double the required minimum | [`05_red_teaming`](./05_red_teaming/) |

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| **AI & Prompt Engineering** | Prompt Engineering · AI Evaluation · AI Red Teaming · Google AI Studio (Gemini) |
| **Programming & Data** | Python · Pandas · Google Colab · JSON · Microsoft Excel |
| **Annotation** | Label Studio · NER · Multi-label Classification |
| **Translation & Linguistics** | Legal Translation · Financial Translation · Terminology Management · ISO 17100 / 18587 / 9001 |
| **Documentation & Workflow** | Markdown · Git · GitHub |

---

## 💡 What This Project Reinforced

1. **A number is only worth reporting once it's been checked twice.** An early draft of my prompt-strategy table over-counted techniques through double-labeling. Fixing it meant going back and verifying each entry against the actual prompt text — a habit I kept for every count in this portfolio since.

2. **A refusal means little if it can't survive a second try.** During red teaming, one AI system refused a harmful request cleanly, then reversed itself completely when the same request was rephrased in six words. That's a more concerning failure than no refusal at all, because it looks safe until someone actually tests it.

3. **The decision behind a result matters as much as the result.** A cleaned dataset or a working prompt says little on its own — I logged why each row was dropped and why each term was chosen, because that's what makes the output checkable by someone other than me.

4. **One finding is an anecdote; the same finding twice is a pattern.** The same two failures — bypassing human oversight, normalizing identity-based bias — showed up independently in a financial scenario and a medical one. That repetition across unrelated domains is what made the red-teaming report worth trusting.

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

- 📧 **Email:** [ahmed.hamdy.m111@gmail.com]
  

---

<div align="center">

✦ ✦ ✦

*The same weakness showing up twice, in two unrelated domains, is what separates a red-teaming finding from a coincidence — that's the standard applied throughout this portfolio.*

**Motrjim Academy**
AI Linguistics & Prompt Engineering Diploma · Graduation Capstone 2026

</div>
