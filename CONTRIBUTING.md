# Contributing to Zéro French

Thank you for your interest in contributing to **Zéro French**! Our mission is to provide a free, world-class, project-based French curriculum specifically calibrated for the **TCF Canada** and Canadian immigration (NCLC 7+ / B2).

---

## How You Can Contribute

1. **Fix Broken Links or Suggest Better Free Resources**:
   - If an external link changes or goes behind a paywall, open an issue or pull request with a high-quality free replacement.
   - All links must be permanently free to access without account creation traps or credit card requirements.

2. **Report Grammatical or Phonetic Errors**:
   - Spot an incorrect gender, missing accent, unnatural turn of phrase, or flawed IPA transcription? Please submit a pull request or file an issue.

3. **Contribute Canadian French Context**:
   - We actively integrate authentic Québec and Canadian French terms, OQLF standards, and North American administrative conventions alongside standard international French.

4. **Author Lessons for Upcoming Paths**:
   - Before drafting new lessons, read our mandatory standard operating procedure: [WRITER_BRIEF.md](WRITER_BRIEF.md).
   - Lessons must follow our section layout, pattern-first inductive grammar method, and 1,500–3,500 word depth.

---

## Authoring Standards & Pull Request Checklist

Before submitting a pull request for a lesson or project:

- [ ] Lesson headings start strictly at `###` (never `#` or `##`).
- [ ] Substantive depth: at least 1,500 words of real instructional prose in teaching sections.
- [ ] French examples include bold French, IPA pronunciation in slashes, and italicized English translation.
- [ ] Embedded practice task in the Assignment panel with an expandable `<details><summary>` solution.
- [ ] At least one `lesson-note--warning` (Exam tip) and one `lesson-note--tip` (Canadian context).
- [ ] 4 to 7 clickable Knowledge Check anchor questions linking to section headings.
- [ ] Automated validation passes cleanly:
  ```bash
  python3 scripts/validate.py
  python3 scripts/validate.py --links
  ```

---

## Community & Questions

- Browse existing issues or open a new one on [GitHub](https://github.com/espiNovah/zero-french/issues).
- Check [PROGRESS.md](PROGRESS.md) to see current authoring batches and pipeline status.
