# Layout style guide

This guide keeps every lesson and project consistent, so learners always know where to look. It is adapted from [The Odin Project's layout style guide](https://github.com/TheOdinProject/curriculum/blob/main/LAYOUT_STYLE_GUIDE.md).

## Where files live

```text
curriculum/
  curriculum.json          # order of paths → sections → lessons (the site reads this)
  about.md                 # the About page
  tcf.md                   # the TCF Canada exam reference page
  <path>/<section>/<lesson>.md
```

- Folder and file names use `snake_case`.
- Project files start with `project_`, for example `a1_basics/greetings_and_introductions/project_introduce_yourself.md`.
- A lesson only appears on the site once it is listed in `curriculum.json`. Each entry has an `id` (kebab-case, unique within its path), a `title`, a one-line `description`, the `file` path relative to `curriculum/`, and `"project": true` for projects.

## Lesson layout

Copy [templates/lesson-template.md](templates/lesson-template.md). Sections, in order:

1. `### Introduction`: what the lesson is about and why it matters.
1. `### Lesson overview`: up to 7 bullets naming what the learner will *learn about*.
1. Custom sections (`### Your heading`): the actual teaching, written in your own words. French examples with pronunciation and translation are encouraged (see below). This is what makes a lesson more than a reading list.
1. `### Assignment`: a numbered list of the resources to read, watch or listen to, and the exercises to do, wrapped in `<div class="lesson-content__panel" markdown="1">`. Aim for 3–5 items. Say why each one is there, and which parts to focus on.
1. `### Knowledge check`: 4–7 questions that test the main ideas. Each question is a link to the `###` heading that answers it, so a learner who is unsure can jump back. Headings get their anchor from their text: lowercase, with runs of anything that isn't a letter or digit replaced by `-` (`### Tu vs Vous` → `#tu-vs-vous`). The validator checks that every anchor exists.
1. `### Additional resources` (optional): supplemental links, each with a sentence on what it adds. Leave the section out entirely if there are none.

A lesson is **written** (no longer an outline) when it has:

- at least 600 words of explanation in your own words in its custom sections;
- at least three French examples with pronunciation and translation;
- a practice step in the Assignment;
- a knowledge check.

Lessons that don't meet this yet start with the "Outline lesson" warning box. Remove the box when the lesson is written.

## Project layout

Copy [templates/project-template.md](templates/project-template.md): `### Introduction`, an optional pre-assignment section, `### Assignment` (numbered requirements, then `#### Evidence`, then `#### Extra credit`), and an optional post-assignment section.

Every project produces evidence the learner keeps. Projects must require evidence that the skill works, not only that the learner attempted it. The `#### Evidence` list builds up through the curriculum:

| From | Evidence every project requires |
| --- | --- |
| A1: Introduce Yourself | An audio recording of the speaking task, timed to the TCF format. |
| A2: Mock Listening & Reading | Scores on a timed practice set, logged with the date. |
| B1: Write a Formal Letter | A written text in the TCF format with word count and time taken. |
| B2: Full Mock Exam | All four parts timed, scored and converted to CEFR and NCLC levels. |

A project may only require skills taught earlier in the curriculum. If it needs something new, teach it in a lesson first.

## Headings

- Lessons start at `###`. The site renders the lesson title as the page heading, so never use `#` or `##`.
- `###` headings appear in the "On this page" sidebar, so keep them short and descriptive.
- No French text in headings (keep headings in English for navigation clarity).

## Note boxes

Leave a blank line after the opening `<div>` and before the closing `</div>`, and always give the box a `####` title.

```markdown
<div class="lesson-note lesson-note--tip" markdown="1">

#### Title

Text.

</div>
```

Variants: `lesson-note` (info), `lesson-note--tip`, `lesson-note--warning`, `lesson-note--critical`.

### Exam tip box

Use `lesson-note--warning` for exam-specific tips about the TCF Canada (time management, task structure, scoring traps):

```markdown
<div class="lesson-note lesson-note--warning" markdown="1">

#### Exam tip

In the TCF writing test, going under the minimum word count on any task can result in a score of "below A1" for the entire writing section.

</div>
```

### Québec vs France box

Use `lesson-note--tip` when noting differences between Québec and European French:

```markdown
<div class="lesson-note lesson-note--tip" markdown="1">

#### Québec vs France

In Québec, *Bienvenue* means "You're welcome," while in France it only means "Welcome."

</div>
```

## French examples

Every lesson should teach with real French. Format examples consistently:

### Inline examples

Use **bold** for the French, IPA in slashes, and *italics* for the English translation:

```markdown
**Bonjour** — /bɔ̃.ʒuʁ/ — *Hello / Good day*
```

### Blockquote examples (for longer phrases or dialogues)

Use blockquotes with the French on one line and the translation on the next:

```markdown
> **Comment allez-vous aujourd'hui ?** — /kɔ.mɑ̃.t‿a.le vu o.ʒuʁ.dɥi/
> *How are you today?*
```

### Tables of vocabulary

Use tables for lists of related words. Always include pronunciation:

```markdown
| French | Pronunciation | English |
| --- | --- | --- |
| **Bonjour** | /bɔ̃.ʒuʁ/ | Hello |
| **Merci** | /mɛʁ.si/ | Thank you |
```

### Pronunciation hints

- Use IPA (International Phonetic Alphabet) for precision. Learners will encounter IPA in dictionaries and language tools.
- For sounds that don't exist in English, add a brief note: "The French *r* (/ʁ/) is produced at the back of the throat, unlike the English *r*."
- Nasal vowels (/ɑ̃/, /ɔ̃/, /ɛ̃/) deserve special attention — point them out whenever they appear.

### Québec French markers

When a word, pronunciation or usage differs between standard (European) French and Québec French:

- Use the Québec vs France note box (see above).
- Mark Québec-specific vocabulary with **(QC)** inline when it appears in a table or list.
- The TCF Canada tests standard French, but understanding Québec variants helps learners who will live in Canada.

## Links

- Use descriptive link text such as `[the TV5Monde TCF practice site](…)`, never "click here."
- **Free resources only.** No paywalls, no required sign-ups where a free alternative exists, no affiliate links.
- Prefer, in order: official sources (France Éducation international, IRCC); well-known free platforms (TV5Monde, RFI, Lawless French); respected language-teaching sites.
- Language resources change frequently. When you link to a specific page, check that it still exists.

## Language

Use English for all lesson text (the learner is an English speaker learning French). Write in plain, direct sentences. Define grammatical terms the first time they appear. French words and phrases in the lesson text should be in *italics* with a translation on first use.
