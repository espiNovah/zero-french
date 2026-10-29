# Zéro French — Writer Brief & Editorial Guide

> **Audience**: This document is the mandatory standard operating procedure for every AI agent, instructional designer, teacher, and contributor authoring lessons or projects for **Zéro French**. Every pull request and authored markdown file will be audited against these rules before merging.

---

## 1. Core Mission & Guiding Principles

Our single goal is to take an adult learner from zero French to passing the **TCF Canada** with **at least B2 and NCLC 7 across all four competencies** (Listening, Reading, Writing, Speaking), unlocking maximum points for Canadian economic immigration (Express Entry, Francophone Mobility, and Provincial Nominee Programs).

Every lesson and project must obey the seven core principles established in our master roadmap:

1. **Teach Before Linking**: Every lesson must teach the concept thoroughly in our own words (1,500–2,200 words of real pedagogical prose, examples, and mechanics) before offering external links. External resources reinforce; they never substitute for primary teaching.
2. **Practice Every Lesson**: No passive reading. Every lesson includes a hands-on task embedded directly in the text, complete with answers or self-assessment criteria.
3. **Every Skill in Every Path**: The four competencies—*Compréhension orale* (CO), *Compréhension écrite* (CE), *Expression écrite* (EE), and *Expression orale* (EO)—are developed concurrently from Day 1.
4. **Never Require Something Not Yet Taught**: Strict sequential scaffolding. A lesson or exercise may only assume vocabulary, grammar, and structures introduced earlier in the curriculum order file (`curriculum.json`).
5. **Honest Hours for a Safe Score**: We prepare learners for a comfortable safety buffer (Upper B2 / NCLC 8), not a precarious borderline pass. Reaching NCLC 7 from zero takes **750–800 guided and self-study hours**. Path 05 (B2+ Safety Margin) is mandatory core curriculum.
6. **100% Free Resources Only**: Never link to a resource behind a paywall, a paid subscription, or an obligatory sign-up when a free open alternative exists. Never link to copyrighted exam leaks; use only officially released sample materials.
7. **Strict Exam Alignment**: From Path 01 (A2) onwards, every section must feature at least one task mirroring official TCF Canada formats, word counts, and timers, culminating in full 4-part timed milestone mocks.

---

## 2. Lesson Structure & Requirements

Every lesson file lives in `curriculum/<path_folder>/<section_folder>/<lesson_name>.md`. All lesson headings start at `###` because the site rendering engine reserves `#` and `##` for the course shell.

Lessons must follow this exact section sequence:

```markdown
### Introduction

### Lesson overview

### [Custom Teaching Section 1: Concept & Patterns]

### [Custom Teaching Section 2: Mechanics & Variations]

### [Custom Teaching Section 3: Nuance, Registers & Traps]

### Assignment

### Knowledge check

### Additional resources
```

### 2.1 Introduction
- 100–150 words setting the scene.
- Explain **what** the lesson covers and **why it matters for everyday communication and the TCF Canada exam**.
- Hook the adult learner by connecting the topic to immigration realities (workplace, renting, administrative calls, or exam tasks).

### 2.2 Lesson overview
- A clean, bulleted list of 4 to 7 items outlining what the learner will understand and be able to do by the end of the lesson. Use active, learner-focused verbs:
  - *Differentiate between formal vous and informal tu...*
  - *Form the passé composé with auxiliary être for movement verbs...*
  - *Scan public transportation notices for departure times and platform changes...*

### 2.3 Teaching Sections (1,500–2,200 words)
- **Depth**: Deliver substantive, adult-oriented pedagogical explanations in plain English. Avoid condescending textbook jargon; explain the underlying communicative logic.
- **Pattern-First Grammar**: Always explain grammar inductively. Present clear, paired examples first so the learner observes the pattern, and then codify the grammatical rule or formula.
- **French Examples**: Every concept must have abundant French examples. Format every example consistently:
  - **Inline**: `**Phrase en français** — /fʁaz ɑ̃ fʁɑ̃.sɛ/ — *English translation*`
  - **Dialogue / Blockquote**:
    > **Comment vous appelez-vous ?** — /kɔ.mɑ̃ vu.z‿a.ple vu/  
    > *What is your name? (formal)*
- **Pronunciation Hints**: Every new sound, liaison, silent consonant, or elision must include an IPA transcription in slashes or an accessible plain-English phonetic hint (e.g., *"The French u (/y/) is made by shaping your lips to say 'oo' while trying to pronounce 'ee'"*).
- **Exam Tip Callout**: Include at least one `lesson-note--warning` box addressing specific TCF Canada traps:
  ```markdown
  <div class="lesson-note lesson-note--warning" markdown="1">

  #### Exam tip

  In TCF Listening, audio recordings are played **only once**. Train yourself to read the four answer options during the 10-second pause before the audio begins.

  </div>
  ```
- **Canadian French Callout**: When vocabulary, pronunciation, or cultural usage differs between standard international French and Canadian/Québec French, include a `lesson-note--tip` box and mark Québec terms with **(QC)**:
  ```markdown
  <div class="lesson-note lesson-note--tip" markdown="1">

  #### Québec vs France

  In France, you will hear *faire les courses* or *faire du shopping*. In Québec, the standard term is *magasiner* **(QC)**. On the TCF Canada, both are recognized, but listening prompts set in Montreal or Gatineau will use Canadian terms.

  </div>
  ```

### 2.4 Assignment
Enclose the entire assignment inside `<div class="lesson-content__panel" markdown="1">`. Every lesson assignment must contain:
1. **Core Practice Step**: A hands-on exercise embedded directly in the markdown (e.g., fill-in-the-blank, error correction, sentence transformation) with an expandable `<details><summary>Check your answers</summary>...</details>` solution block.
2. **Vocabulary / Anki Deck**: Curated vocabulary list (10–20 words with IPA and context sentence) or direct Anki card prompt.
3. **Receptive Task (Listening or Reading)**: A link to a free native audio clip or short text (RFI, TV5Monde, Radio-Canada) with 3 comprehension questions.
4. **Productive Task (Speaking or Writing)**: A short active production prompt (e.g., a 60-second voice note or a 60-word email draft).

### 2.5 Knowledge Check
- **4 to 7 questions** that test the core concepts taught in the lesson.
- **Strict Anchor Requirement**: Every question must be a Markdown link pointing to the exact `###` heading that answers it:
  `- [When must you use être instead of avoir in compound past tenses?](#passe-compose-with-etre)`
- Slugs are generated automatically: lowercase, alphanumeric characters, with spaces and punctuation replaced by hyphens (`### Passé Composé with Être` → `#passe-compose-with-etre`).

### 2.6 Additional Resources
- 2 to 4 high-quality, completely free resources for learners seeking deeper immersion.
- For each resource, write a descriptive link title (never "click here") and a sentence explaining exactly what it adds and how to use it.

---

## 3. Projects & Milestone Mock Exams

Project files are named `project_<name>.md`. Projects are where learners prove competency and accumulate portfolio evidence.

### 3.1 Project Structure
1. `### Introduction`: What the learner will produce and which TCF skill it tests.
2. `### Before you start`: Equipment needed (audio recorder, countdown timer, keyboard setting) and reference materials.
3. `### Assignment`: Step-by-step instructions wrapped in `<div class="lesson-content__panel" markdown="1">`:
   - Exact TCF task type (Writing Task 1/2/3, Speaking Task 1/2/3, or timed MCQ).
   - Strict time limits (e.g., 15 minutes for Writing Task 1; 2 minutes prep + 3.5 minutes speaking for Speaking Task 2).
   - Word count boundaries (e.g., 60–120 words for Task 1; 120–150 words for Task 2; 120–180 words for Task 3).
4. `#### Evidence`: Bulleted list specifying the tangible proof the learner must preserve:
   - MP3 audio recording of unedited speaking delivery.
   - Text file typed without autocorrect or grammar plugins.
   - Standardized score log entry recording raw score, CEFR level, NCLC equivalency, and date.
5. `#### Scoring Rubric`: Complete table matching official FEI criteria:
   - *Respect de la consigne / Réalisation de la tâche*
   - *Cohérence et cohésion / Organisation textuelle*
   - *Étendue et maîtrise du lexique*
   - *Correction morphosyntaxique et grammaticale*
6. `#### AI Self-Assessment Prompt`: A pre-engineered prompt template the learner can paste into an LLM to receive strict, uninflated rubric grading.
7. `#### Extra credit`: An optional extension pushing the response toward higher CEFR complexity.

---

## 4. TCF Canada Exam Alignment Reference

When designing exam tasks, writers must use official France Éducation international (FEI) and IRCC parameters:

| Component | Format | Official Timing | Official Word / Question Count | Scoring Scale | NCLC 7 Minimum Threshold |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Compréhension orale (CO)** | 4-choice MCQ, audio played **once** | 35 minutes | 39 questions | 0–699 pts | **458 pts** (Upper B2) |
| **Compréhension écrite (CE)** | 4-choice MCQ | 60 minutes | 39 questions | 0–699 pts | **453 pts** (Upper B2) |
| **Expression écrite (EE)** | 3 written tasks (computer-typed) | 60 minutes total | Task 1: 60–120 words<br>Task 2: 120–150 words<br>Task 3: 120–180 words | 0–20 pts | **10 pts** (Solid B2) |
| **Expression orale (EO)** | 3 face-to-face recorded tasks | 12 minutes total | Task 1: 2 min (no prep)<br>Task 2: 5 min 30 (2 min prep + 3.5 min roleplay)<br>Task 3: 4 min 30 (no prep) | 0–20 pts | **10 pts** (Solid B2) |

> **Critical Note on Writing Task 3**: Task 3 requires the candidate to read two short documents presenting opposing viewpoints, synthesize both positions in their own words, and take a defended personal stance. **Copying phrases directly from the prompt documents is severely penalized by FEI examiners.** Lessons and projects must explicitly drill paraphrasing and synthesis techniques.

---

## 5. Resource Curation, Authenticity & Balance

### 5.1 Permitted & Recommended Sources
- **Official Exam Bodies**: France Éducation international (FEI), IRCC, TV5Monde TCF entraînement.
- **Authentic Francophone Media**:
  - *Canada*: Radio-Canada (*Midi info*, *Aujourd'hui l'histoire*, *Rad*, *Téléjournal*), Le Devoir, La Presse.
  - *International*: RFI (*Le Journal en français facile*), TV5Monde (*7 jours sur la planète*), Le Monde, France Info.
- **Reference & Grammar**: Lawless French, Le Robert, CNRTL, Vitrine linguistique (OQLF Québec).

### 5.2 Strict Rules on Links & Resources
- **Zero Paywalls**: Never link to resources requiring payment, subscription, or trial credit cards.
- **No Sign-Up Barriers**: If a resource requires creating an account, verify that a completely open alternative does not exist.
- **No Hallucinated Links**: Every URL must be tested and verified to return an HTTP 200 status code before inclusion. Never guess or invent URLs.
- **Anti-Bot Sites**: If a valid site (e.g., Coursera, certain news sites) blocks automated bots with Cloudflare or 403, test it manually in a real browser, retain the link, and document it in the pull request notes.
- **Curriculum Balance**: Never rely exclusively on a single YouTube channel (e.g., Français Authentique or InnerFrench) or website. Rotate across European, Canadian, and African Francophone sources. Always include Canadian audio sources in every path.

---

## 6. Layout, Styling & Neubrutalist Conventions

All pages must comply with [LAYOUT_STYLE_GUIDE.md](file:///Users/mac/Desktop/vibe%20coding/zero-french/LAYOUT_STYLE_GUIDE.md):

- **Headings**: Only `###` for main sections, `####` for subsections or note box titles. Never `#` or `##`.
- **Note Boxes**: Enclose in `<div class="lesson-note lesson-note--variant" markdown="1">` followed by an empty line, a `#### Title`, the content, an empty line, and `</div>`.
  - Info: `lesson-note`
  - Québec nuance: `lesson-note--tip`
  - Exam warning: `lesson-note--warning`
  - Critical trap: `lesson-note--critical`
- **Tables**: Use clean Markdown tables with header separators. Left-align text, right-align numbers.
- **No Broken Elements**: Ensure all HTML tags are closed, blockquotes are indented properly, and markdown inside `<div>` panels uses `markdown="1"`.

---

## 7. Authoring Workflow & Verification Report

Every writer must follow this three-step authoring workflow:

1. **Draft to Disk**: Write the complete, untruncated lesson directly to its final destination file in `curriculum/`. Do not produce partial placeholders or leave "TODO" sections.
2. **Automated Validation**: Run the validator script locally from the repository root:
   ```bash
   python3 scripts/validate.py
   python3 scripts/validate.py --links
   ```
   Fix all anchor mismatches, missing headings, or dead links before proceeding.
3. **Verification & Audit Report**: Conclude your pull request or authoring log with a standardized **Quality & Verification Report**:

```markdown
### Authoring Verification Report
- **File**: `curriculum/path/section/lesson.md`
- **Word Count**: [X] words of instructional prose in custom sections (Target: 1,500–2,200).
- **Prerequisites Checked**: Confirmed only assumes concepts up to lesson [ID].
- **TCF Alignment**: Practices [Part / Task type] under official [timing/word count] rules.
- **Links Tested**: [X] external URLs verified returning HTTP 200.
- **Québec Variants**: Marked with `(QC)` and referenced to OQLF standards.
- **Unverified Items**: [List any items that require human review or native speaker audio verification].
```

---

## 8. Master Curriculum Roadmap

For full path structure, lesson inventories, milestone mock schedules, and project deliverables, refer to the complete master roadmap below.

***

*(Embedded Reference: Complete `ROADMAP.md`)*

```markdown
# Zéro French — Curriculum Roadmap

This roadmap operationalizes the expert examiner audit into a concrete, phased implementation plan. Every finding from the review is mapped to specific files and deliverables that can be authored, reviewed, and shipped in discrete increments.

---

## 1. Guiding Principles

Every lesson, project, and code commit must adhere to these seven non-negotiable principles:

1. **Teach Before Linking**: Every lesson must teach the concept thoroughly in our own words (minimum 600 words of substantive prose, grammar mechanics, and examples) before offering external links. External resources reinforce; they never substitute for core teaching.
2. **Practice Every Lesson**: No passive reading. Every single lesson must include an active exercise (fill-in, transformation, audio comprehension check, or mini-speaking drill) with solutions or self-check criteria right in the lesson.
3. **Every Skill in Every Path**: The four TCF competencies—Compréhension orale (CO), Compréhension écrite (CE), Expression écrite (EE), and Expression orale (EO)—must be exercised systematically across every path from A1 to B2+.
4. **Never Require Something Not Yet Taught**: Strict sequential scaffolding. A project or exercise in Section 2 may never presume grammar, syntax, or vocabulary introduced in Section 3.
5. **Honest Hours for a Safe Score**: No marketing illusions. Reaching a guaranteed, safe NCLC 7 across all four skills requires 750–800 total hours for an adult beginner. Path 05 (B2+ Safety Margin) is mandatory core curriculum, not an optional bonus.
6. **100% Free Resources Only**: Every linked resource, audio stream, dictionary, and mock item must be permanently free to access without paywalls, required paid subscriptions, or trial traps.
7. **Strict Exam Alignment**:
   - From Path 01 (A2) onwards, every section includes at least one task in the official TCF Canada format (Task 1/2/3 for writing or speaking, or official 4-choice MCQ sets for listening/reading).
   - Every path ends with a timed, four-part milestone mock exam logged in a standardized score sheet.
   - All written production simulates the computer-based exam format (TCF-SO): typed without autocorrect, adhering strictly to official FEI word-count ceilings and floors.

---

## 2. Definitions of "Done"

### 2.1 Definition of "Done" for a Lesson
A lesson is marked Done only when it meets all of the following criteria:
- [ ] Substance: At least 600 words of original, pedagogical explanation in English in its custom sections (standard target: 1,500–2,200 words).
- [ ] Linguistic Examples: At least 3 distinct French examples formatted with bold French, IPA pronunciation in slashes, and italicized English translation.
- [ ] Embedded Practice Step: An interactive self-practice exercise embedded directly in the Assignment panel following the standardized exercise schema.
- [ ] Exam Alignment Box: At least one lesson-note--warning containing an authentic Exam tip covering TCF pacing, rubric traps, distractor patterns, or computer interface quirks.
- [ ] Canadian Context: When applicable, at least one lesson-note--tip highlighting Québec vs France lexical, phonetic, or cultural differences (marked with (QC)).
- [ ] Knowledge Check: 4 to 7 clickable anchor questions linking back to headings in the lesson, verified by the automated validator.
- [ ] Free Resource Vetted: 2 to 4 curated external links to free, working audio/reading sources verified with HTTP 200 responses.

### 2.2 Definition of "Done" for a Project
A project is marked Done only when it meets all of the following criteria:
- [ ] TCF Task Specification: Explicitly specifies the TCF task type, exact word count range, and preparation/execution timers.
- [ ] FEI Criteria Rubric: Contains the complete 4-criterion grading matrix matching France Éducation international standards.
- [ ] Verifiable Evidence Requirement: Clear instructions on the exact tangible artifact the learner must generate and archive.
- [ ] Calibrated AI Evaluation Prompt: A copy-paste prompt formatted with strict FEI grading parameters for self-evaluation.
- [ ] Typing & Timing Constraints: Mandatory simulation of TCF-SO conditions (physical typing without spellcheck).

---

## 3. Phase Breakdown Summary
- **Phase 1: Verified Exam & Documentation Bugs**: Fixes score ranges, NCLC cut-offs, exam parameters, and keyboard realities in `curriculum/tcf.md` and `curriculum/about.md`.
- **Phase 2: Infrastructure & Tooling**: Templates, score logs (`templates/mock-exam-score-log.md`), exercise formats, and validator enhancements.
- **Phase 3: Curriculum Restructuring & Manifest**: Full 6-path registration in `curriculum.json` and pedagogical re-sequencing (Passé Composé isolated before Imparfait; Conditionnel before Subjunctive).
- **Phase 4: Authoring Lessons**:
  - Path 00: A1 Basics (~100h / 16 lessons + 4 projects)
  - Path 01: A2 Survival French (~100h / 16 lessons + 4 projects)
  - Path 02: B1 Independent French (~200h / 16 lessons + 4 projects)
  - Path 03: B2 Advanced French (~200h / 16 lessons + 4 projects)
  - Path 04: TCF Canada Exam Prep (~60h / 16 lessons + 4 projects)
  - Path 05: B2+ Safety Margin (~60h / 8 lessons + 2 projects)
- **Phase 5: Upgrading Projects**: Embedding official FEI rubrics, timers, evidence specifications, and AI feedback prompts across all project files.
- **Phase 6: Final Verification & Build**: Running automated checks, link crawlers, and static site build verification.
```
