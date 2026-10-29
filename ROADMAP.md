# Zéro French — Curriculum Roadmap

This roadmap operationalizes the expert examiner audit into a concrete, phased implementation plan. Every finding from the review is mapped to specific files and deliverables that can be authored, reviewed, and shipped in discrete increments.

---

## 1. Guiding Principles

Every lesson, project, and code commit must adhere to these seven non-negotiable principles:

1. **Teach Before Linking**: Every lesson must teach the concept thoroughly in our own words (minimum 600 words of substantive prose, grammar mechanics, and examples) before offering external links. External resources reinforce; they never substitute for core teaching.
2. **Practice Every Lesson**: No passive reading. Every single lesson must include an active exercise (fill-in, transformation, audio comprehension check, or mini-speaking drill) with solutions or self-check criteria right in the lesson.
3. **Every Skill in Every Path**: The four TCF competencies—*Compréhension orale* (CO), *Compréhension écrite* (CE), *Expression écrite* (EE), and *Expression orale* (EO)—must be exercised systematically across every path from A1 to B2+.
4. **Never Require Something Not Yet Taught**: Strict sequential scaffolding. A project or exercise in Section 2 may never presume grammar, syntax, or vocabulary introduced in Section 3.
5. **Honest Hours for a Safe Score**: No marketing illusions. Reaching a guaranteed, safe NCLC 7 across all four skills requires **750–800 total hours** for an adult beginner. Path 05 (B2+ Safety Margin) is mandatory core curriculum, not an optional bonus.
6. **100% Free Resources Only**: Every linked resource, audio stream, dictionary, and mock item must be permanently free to access without paywalls, required paid subscriptions, or trial traps.
7. **Strict Exam Alignment**:
   - From Path 01 (A2) onwards, **every section includes at least one task in the official TCF Canada format** (Task 1/2/3 for writing or speaking, or official 4-choice MCQ sets for listening/reading).
   - **Every path ends with a timed, four-part milestone mock exam** logged in a standardized score sheet.
   - All written production simulates the computer-based exam format (**TCF-SO**): typed without autocorrect, adhering strictly to official FEI word-count ceilings and floors.

---

## 2. Definitions of "Done"

### 2.1 Definition of "Done" for a Lesson

A lesson is marked **Done** (and ready to have its outline warning removed) only when it meets all of the following criteria:

- [ ] **Substance**: At least 600 words of original, pedagogical explanation in English in its custom sections (standard target: 1,500–2,200 words).
- [ ] **Linguistic Examples**: At least 3 distinct French examples formatted with bold French, IPA pronunciation in slashes, and italicized English translation:  
  `> **Phrase** — /fʁaz/ — *Sentence*`
- [ ] **Embedded Practice Step**: An interactive self-practice exercise embedded directly in the `### Assignment` panel following the standardized exercise schema (with expandable answer key or self-scoring rubric).
- [ ] **Exam Alignment Box**: At least one `lesson-note--warning` containing an authentic **Exam tip** covering TCF pacing, rubric traps, distractor patterns, or computer interface quirks.
- [ ] **Canadian Context**: When applicable, at least one `lesson-note--tip` highlighting **Québec vs France** lexical, phonetic, or cultural differences (marked with **(QC)**).
- [ ] **Knowledge Check**: 4 to 7 clickable anchor questions linking back to `###` headings in the lesson, verified by the automated validator.
- [ ] **Free Resource Vetted**: 2 to 4 curated external links to free, working audio/reading sources (RFI, TV5Monde, Radio-Canada, Lawless French) verified with HTTP 200 responses.

### 2.2 Definition of "Done" for a Project

A project is marked **Done** only when it meets all of the following criteria:

- [ ] **TCF Task Specification**: Explicitly specifies the TCF task type (Writing Task 1/2/3, Speaking Task 1/2/3, or timed MCQ set), exact word count range, and preparation/execution timers.
- [ ] **FEI Criteria Rubric**: Contains the complete 4-criterion grading matrix matching France Éducation international standards:
  1. *Respect de la consigne / Réalisation de la tâche*
  2. *Cohérence et cohésion / Organisation du discours*
  3. *Étendue et maîtrise du lexique*
  4. *Correction grammaticale et morphosyntaxique*
- [ ] **Verifiable Evidence Requirement**: Clear instructions on the exact tangible artifact the learner must generate and archive (e.g., MP3 audio file, unassisted typed text file with timestamp, or mock exam score log).
- [ ] **Calibrated AI Evaluation Prompt**: A copy-paste prompt formatted with strict FEI grading parameters, few-shot scoring penalties, and word-count enforcement for learners using AI tools for self-evaluation.
- [ ] **Typing & Timing Constraints**: For writing projects, mandatory simulation of TCF-SO conditions (physical typing on QWERTY/AZERTY, no spellcheck, timer running).

---

## 3. Phase-by-Phase Work Breakdown

### Phase 1: Verified Exam & Documentation Bugs
*Fix misleading score ranges, NCLC cut-offs, exam parameters, and keyboard realities.*
* **Dependencies**: None.
* **Estimated Size**: Small (~1 day).

| Action | Target File | Description |
| :--- | :--- | :--- |
| **EDIT** | `curriculum/tcf.md` | **Fix the "Middle of B2" fallacy**: Explicitly state that NCLC 7 requires Upper B2 (Listening ≥ 458, Reading ≥ 453), whereas mid-B2 (450) is a failing NCLC 6. Set safe study target scores: Listening ≥ 475, Reading ≥ 470, Writing ≥ 12, Speaking ≥ 12. |
| **EDIT** | `curriculum/tcf.md` | **Add TCF-SO Computer Exam Specifics**: Add section on the computer-delivered interface, typing without autocorrect, keyboard layout traps (AZERTY vs QWERTY Canadian Multilingual), and accent key combinations. |
| **EDIT** | `curriculum/tcf.md` | **Correct Speaking Task 2 Timing**: Update description to explicitly state `2 minutes preparation` + `3 minutes 30 seconds interaction`. |
| **EDIT** | `curriculum/about.md` | Update the total curriculum hour estimates to 750–800 hours to reflect safe NCLC 7 preparation for adult self-study learners. |
| **EDIT** | `curriculum_plan.md` | Synchronize the master architectural plan in the artifacts directory with these corrected numbers and guidelines. |

---

### Phase 2: Infrastructure & Tooling
*Create standard templates, mock logs, exercise formats, and extend the validator script to enforce pedagogical rules.*
* **Dependencies**: Phase 1.
* **Estimated Size**: Medium (~2–3 days).

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `templates/mock-exam-score-log.md` | Standardized Markdown score log template. Tracks Listening (/699), Reading (/699), Writing (/20), Speaking (/20), time elapsed, distractor analysis, and automatic conversion to CEFR and NCLC 4–10+. |
| **NEW** | `templates/exercise-format.md` | Specification and HTML/Markdown snippets for standard lesson micro-exercises: Fill-in-the-blank (Cloze), Distractor Multiple Choice, Transformation Drills, and Unscripted 60-Second Audio Prompts. |
| **EDIT** | `templates/lesson-template.md` | Add explicit placeholder sections for the embedded practice exercise, standard answer-disclosure markup, and required TCF Exam Tip box. |
| **EDIT** | `templates/project-template.md` | Update template to include official FEI 4-criteria rubric table, word count floor/ceiling enforcement warnings, TCF-SO typing instructions, and copy-paste AI grading prompt block. |
| **EDIT** | `scripts/validate.py` | Add validation passes: (1) check lessons for embedded practice section in Assignment; (2) verify all projects have FEI rubric tables; (3) verify that every section in paths A2–B2 contains at least one TCF-aligned task; (4) verify that every path ends with a project containing a 4-part mock. |
| **NEW** | `scripts/score_calculator.py` | Command-line utility to convert raw TCF scores to official CEFR and NCLC levels, flagging whether the candidate meets Express Entry NCLC 7 requirements. |

---

### Phase 3: Curriculum Restructuring & Manifest
*Fix sequence errors (PC vs Imparfait, Subjunctive vs Conditional) and establish the full multi-path structure in `curriculum.json`.*
* **Dependencies**: Phase 2.
* **Estimated Size**: Medium (~2 days).

| Action | Target File | Description |
| :--- | :--- | :--- |
| **EDIT** | `curriculum/curriculum.json` | Expand manifest from single A1 stub to all 6 complete paths: `a1-basics`, `a2-survival-french`, `b1-independent-french`, `b2-advanced-french`, `tcf-canada-prep`, and `b2-safety-margin`. Set `optional: false` on ALL paths (total: ~760 hours). |
| **MOVE / EDIT** | `curriculum/a2_survival/` | **Restructure A2 Sequence**: Move Imparfait and PC vs Imparfait out of Section 1. Section 1 becomes Passé Composé only (Avoir & Être); Section 2 introduces Imparfait for descriptions/habits; Section 3 introduces PC vs Imparfait contrast after object pronouns. |
| **MOVE / EDIT** | `curriculum/b1_independent/` | **Restructure B1 Sequence**: Swap Subjunctive and Conditionnel. Section 1 teaches Conditionnel présent, polite requests (*vouvoiement*), and *Si* hypotheses. Section 2 introduces Subjunctive Present for obligations and emotions. |
| **EDIT** | `curriculum/curriculum.json` | Register 8 full timed mock exams across the curriculum (milestones at ends of A2, B1, B2, mid-Prep, end-Prep, and Safety Margin). |

---

### Phase 4: Writing Curriculum Lessons
*Author the core lessons (~600+ words, authentic French examples, IPA, embedded exercises, free native audio).*
* **Dependencies**: Phase 2 (templates), Phase 3 (manifest structure).
* **Estimated Size**: Large (multi-week iterative authoring).

#### Sub-phase 4A: Path 00 — A1 Basics (~100 hours / 16 lessons + 4 projects)
Focus: Phonetics, numbers, survival vocabulary, basic present conjugation, oral introduction.

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `curriculum/a1_basics/foundations_and_pronunciation/alphabet_and_accents.md` | French alphabet, accents (é, è, ê, ë, ç), pronunciation impact. |
| **NEW** | `curriculum/a1_basics/foundations_and_pronunciation/vowels_and_nasals.md` | Standard vowel positions, oral vs nasal sounds (/ɑ̃/, /ɛ̃/, /ɔ̃/). |
| **NEW** | `curriculum/a1_basics/foundations_and_pronunciation/silent_letters_and_liaisons.md` | Final consonant rules, basic liaisons (*les‿amis*), elisions. |
| **NEW** | `curriculum/a1_basics/foundations_and_pronunciation/numbers_time_dates.md` | Numbers 0–100+, telling time, days, months, and calendar dates. |
| **NEW** | `curriculum/a1_basics/foundations_and_pronunciation/project_pronunciation_benchmark.md` | Project: Audio reading benchmark of minimal pairs and number sequences. |
| **EDIT** | `curriculum/a1_basics/greetings_and_introductions/greetings_and_politeness.md` | Upgrade to Done: Expand explanation, add IPA to all phrases, embed practice drill, add TCF Speaking Task 1 intro box. |
| **NEW** | `curriculum/a1_basics/greetings_and_introductions/personal_identity_and_verbs.md` | State name, nationality, age, profession with *être* and *avoir*. |
| **NEW** | `curriculum/a1_basics/greetings_and_introductions/family_and_relationships.md` | Immediate family members, possessive adjectives (*mon/ma/mes*). |
| **NEW** | `curriculum/a1_basics/greetings_and_introductions/everyday_objects_and_gender.md` | Grammatical gender (*le/la/un/une*), basic colors, office/home items. |
| **EDIT** | `curriculum/a1_basics/greetings_and_introductions/project_introduce_yourself.md` | Upgrade to Done: Add FEI criteria rubric, 2-minute timer constraint, self-scoring rubric for Speaking Task 1. |
| **NEW** | `curriculum/a1_basics/daily_routine_and_places/regular_er_verbs.md` | Present tense regular *-er* verbs, daily routine actions. |
| **NEW** | `curriculum/a1_basics/daily_routine_and_places/irregular_verbs_triad.md` | High-frequency irregulars: *aller*, *faire*, *venir*. |
| **NEW** | `curriculum/a1_basics/daily_routine_and_places/asking_questions_basics.md` | Intonation, *est-ce que*, question words (*qui, quand, où, comment*). |
| **NEW** | `curriculum/a1_basics/daily_routine_and_places/places_in_town_and_prepositions.md` | City landmarks, navigation prepositions (*à côté de, en face de, chez*). |
| **NEW** | `curriculum/a1_basics/daily_routine_and_places/project_daily_routine_and_neighborhood.md` | Project: 60–80 word email describing workday and living area (pre-Writing Task 1). |
| **NEW** | `curriculum/a1_basics/food_shopping_needs/food_and_partitives.md` | Foodstuffs, ordering groceries, partitives (*du, de la, des*). |
| **NEW** | `curriculum/a1_basics/food_shopping_needs/cafe_and_transactions.md` | Ordering breakfast, asking prices (*C'est combien ?*), polite transactions. |
| **NEW** | `curriculum/a1_basics/food_shopping_needs/clothing_and_agreements.md` | Clothes, sizes, colors, and adjective agreement rules. |
| **NEW** | `curriculum/a1_basics/food_shopping_needs/weather_and_seasons.md` | Describing weather conditions, temperature, and seasonal activities. |
| **NEW** | `curriculum/a1_basics/food_shopping_needs/project_a1_capstone.md` | Project: A1 Capstone (3-min audio inquiry + 60-word practical message). |

#### Sub-phase 4B: Path 01 — A2 Survival French (~100 hours / 16 lessons + 4 projects)
Focus: Past narration, routine transactions, formal questioning, transport, health, A2 milestone mock.

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `curriculum/a2_survival/past_narratives/passe_compose_avoir.md` | Passé composé mechanics with *avoir*, regular and irregular past participles. |
| **NEW** | `curriculum/a2_survival/past_narratives/passe_compose_etre.md` | Movement verbs (*Dr & Mrs Vandertramp*) and reflexive verb agreements. |
| **NEW** | `curriculum/a2_survival/past_narratives/narrative_chronology_connectors.md` | Chronology markers (*d'abord, ensuite, puis, soudain, finalement*). |
| **NEW** | `curriculum/a2_survival/past_narratives/tcf_listening_short_announcements.md` | Decoding voicemail messages, train platform calls, store announcements. |
| **NEW** | `curriculum/a2_survival/past_narratives/project_past_vacation_recount.md` | Project: 80–100 word vacation recount + 2-minute recorded recount. |
| **NEW** | `curriculum/a2_survival/housing_and_transit/apartment_features_and_ads.md` | Reading real-estate listings, rooms, amenities, rental conditions. |
| **NEW** | `curriculum/a2_survival/housing_and_transit/imparfait_descriptions_habits.md` | Imparfait formation, describing background states and past habits. |
| **NEW** | `curriculum/a2_survival/housing_and_transit/object_pronouns_direct_indirect.md` | Direct (*le/la/les*) and indirect (*lui/leur*) pronouns in routine responses. |
| **NEW** | `curriculum/a2_survival/housing_and_transit/formal_questioning_techniques.md` | Master inversion, *est-ce que*, and indirect questions for TCF Speaking Task 2. |
| **NEW** | `curriculum/a2_survival/housing_and_transit/project_apartment_inquiry_roleplay.md` | Project: Speaking Task 2 roleplay simulation (asking 7–10 formal questions). |
| **NEW** | `curriculum/a2_survival/work_and_daily_life/professions_and_workplace_tasks.md` | Professional duties, work schedules, job titles, and CV basics. |
| **NEW** | `curriculum/a2_survival/work_and_daily_life/passe_compose_vs_imparfait.md` | Master the contrast: event backbone vs descriptive backdrop. |
| **NEW** | `curriculum/a2_survival/work_and_daily_life/futur_proche_and_simple.md` | Expressing upcoming plans, career projects, and weather forecasts. |
| **NEW** | `curriculum/a2_survival/work_and_daily_life/comparisons_and_superlatives.md` | Comparing housing, jobs, prices, and consumer products. |
| **NEW** | `curriculum/a2_survival/work_and_daily_life/project_career_profile_and_goals.md` | Project: 100-word cover note + 2-minute spoken career profile. |
| **NEW** | `curriculum/a2_survival/health_and_public_services/medical_symptoms_and_advice.md` | Expressing symptoms (*avoir mal à...*), medical visits, imperative advice. |
| **NEW** | `curriculum/a2_survival/health_and_public_services/pronouns_y_and_en.md` | Replacing locations (*y*) and quantities/de-phrases (*en*) in daily speech. |
| **NEW** | `curriculum/a2_survival/health_and_public_services/administrative_interactions.md` | Counter interactions at post office, bank, clinic (*le vouvoiement*). |
| **NEW** | `curriculum/a2_survival/health_and_public_services/tcf_a2_reading_signage_notices.md` | Fast scanning of signs, warning notices, and classified ads. |
| **NEW** | `curriculum/a2_survival/health_and_public_services/project_a2_milestone_mock.md` | Project: Full 4-part A2 milestone mock exam with standardized score log. |

#### Sub-phase 4C: Path 02 — B1 Independent French (~200 hours / 16 lessons + 4 projects)
Focus: Conditionnel, hypotheses, subjunctive, opinion debates, Canadian exposure, B1 milestone mock.

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `curriculum/b1_independent/politeness_and_hypotheses/conditionnel_present.md` | Conditionnel present formation, polite requests, advice, and wishes. |
| **NEW** | `curriculum/b1_independent/politeness_and_hypotheses/si_clauses_structures_1_2.md` | Hypotheses: *si + présent → futur*, *si + imparfait → conditionnel*. |
| **NEW** | `curriculum/b1_independent/politeness_and_hypotheses/workplace_negotiation_disputes.md` | Professional dissatisfaction, proposing solutions, negotiating schedules. |
| **NEW** | `curriculum/b1_independent/politeness_and_hypotheses/tcf_speaking_task2_negotiation.md` | Advanced Speaking Task 2: Leading the dialogue, reacting, negotiating terms. |
| **NEW** | `curriculum/b1_independent/politeness_and_hypotheses/project_writing_task2_letter.md` | Project: Writing Task 2 simulation (120-word formal letter to a supervisor). |
| **NEW** | `curriculum/b1_independent/opinions_and_social_debates/expressing_viewpoints_nuance.md` | Nuanced opinion markers (*selon moi, à mon sens, il me paraît évident que*). |
| **NEW** | `curriculum/b1_independent/opinions_and_social_debates/subjonctif_present_triggers.md` | Subjunctive formation and triggers: obligation, emotion, desire, doubt. |
| **NEW** | `curriculum/b1_independent/opinions_and_social_debates/indicative_vs_subjunctive.md` | Deciding between indicative and subjunctive; avoiding false triggers. |
| **NEW** | `curriculum/b1_independent/opinions_and_social_debates/structuring_arguments_concession.md` | Concession markers (*certes... mais, bien que, toutefois, en revanche*). |
| **NEW** | `curriculum/b1_independent/opinions_and_social_debates/project_speaking_task3_simulator.md` | Project: Speaking Task 3 simulator (3-minute unscripted monologue on telework). |
| **NEW** | `curriculum/b1_independent/media_and_society/reading_francophone_press.md` | Skimming articles, headlines, editorial tone in Le Devoir, La Presse, Le Monde. |
| **NEW** | `curriculum/b1_independent/media_and_society/radio_bulletins_rfi_radiocanada.md` | Training ears to rapid broadcast cadences (RFI *Journal en français facile*). |
| **NEW** | `curriculum/b1_independent/media_and_society/relative_pronouns_qui_que_ou_dont.md` | Complex sentence building with *dont* and *où* without repetition. |
| **NEW** | `curriculum/b1_independent/media_and_society/reported_speech_present.md` | Relaying interviews and statements (*il affirme que, elle précise que*). |
| **NEW** | `curriculum/b1_independent/media_and_society/project_current_event_digest.md` | Project: 120-word news synthesis + 3-minute oral briefing. |
| **NEW** | `curriculum/b1_independent/canadian_realities/canadian_immigration_integration.md` | Societal topics: immigration, regional integration, multiculturalism in Canada. |
| **NEW** | `curriculum/b1_independent/canadian_realities/quebec_lexicon_and_phonology.md` | Canadian French terms (*courriel, char, fin de semaine*) and vowel shifts. |
| **NEW** | `curriculum/b1_independent/canadian_realities/discourse_connectors_b1.md` | Text cohesion: *en premier lieu, d'ailleurs, par conséquent, ainsi*. |
| **NEW** | `curriculum/b1_independent/canadian_realities/tcf_b1_listening_reading_tactics.md` | Handling items 1–25 in listening and reading; pacing and elimination. |
| **NEW** | `curriculum/b1_independent/canadian_realities/project_b1_milestone_mock.md` | Project: Full 4-part B1 milestone mock exam with score log. |

#### Sub-phase 4D: Path 03 — B2 Advanced French (~200 hours / 16 lessons + 4 projects)
Focus: Upper B2 competencies for NCLC 7+, complex synthesis, Radio-Canada audio, unscripted debate defense, B2 milestone mock.

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `curriculum/b2_advanced/argumentation_mastery/structuring_persuasive_essays.md` | Thesis statements, counterargument refutation, and formal synthesis. |
| **NEW** | `curriculum/b2_advanced/argumentation_mastery/nominalization_and_formality.md` | Elevating style: transforming verbal phrases into administrative nominal structures. |
| **NEW** | `curriculum/b2_advanced/argumentation_mastery/advanced_logical_articulators.md` | Mastery of *d'autant plus que, nonobstant, pourvu que, quand bien même*. |
| **NEW** | `curriculum/b2_advanced/argumentation_mastery/nuance_and_modalization.md` | Modulating certainty, probability, and academic rhetorical distance. |
| **NEW** | `curriculum/b2_advanced/argumentation_mastery/project_writing_task3_foundations.md` | Project: Paraphrasing and synthesizing two documents without verbatim copying. |
| **NEW** | `curriculum/b2_advanced/complex_audio_and_voices/decoding_rapid_spontaneous_speech.md` | Overcoming background noise, colloquial drops (*ch'sais pas*), rapid turn-taking. |
| **NEW** | `curriculum/b2_advanced/complex_audio_and_voices/radiocanada_podcasts_analysis.md` | Analyzing debates from Radio-Canada (*Midi info*, *Aujourd'hui l'histoire*). |
| **NEW** | `curriculum/b2_advanced/complex_audio_and_voices/canadian_accents_and_idioms.md` | Diphthongization, contractions, and authentic Canadian expressions. |
| **NEW** | `curriculum/b2_advanced/complex_audio_and_voices/tcf_listening_advanced_drills.md` | Tackling items 26–39: multi-speaker inference and distractor traps. |
| **NEW** | `curriculum/b2_advanced/complex_audio_and_voices/project_tcf_listening_sprint.md` | Project: Full timed 35-minute, 39-question listening sprint (audio played once). |
| **NEW** | `curriculum/b2_advanced/editorial_reading/analyzing_academic_journalistic_texts.md` | Deconstructing editorials, government white papers, and economic reports. |
| **NEW** | `curriculum/b2_advanced/editorial_reading/detecting_bias_irony_implied_meaning.md` | Identifying rhetorical stance, author bias, and implicit arguments. |
| **NEW** | `curriculum/b2_advanced/editorial_reading/tcf_reading_advanced_drills.md` | Managing 60 minutes across 39 questions; banking time for items 26–39. |
| **NEW** | `curriculum/b2_advanced/editorial_reading/fast_elimination_keyword_traps.md` | Defeating absolute wording traps (*toujours, jamais*) and deceptive cognates. |
| **NEW** | `curriculum/b2_advanced/editorial_reading/project_tcf_reading_marathon.md` | Project: Full timed 60-minute, 39-question reading marathon with error log. |
| **NEW** | `curriculum/b2_advanced/high_stakes_production/writing_task1_perfection.md` | Writing Task 1: 60–120 words with precise register, tone, and zero word-count penalty. |
| **NEW** | `curriculum/b2_advanced/high_stakes_production/writing_task2_perfection.md` | Writing Task 2: 120–150 words balancing personal recount and critical opinion. |
| **NEW** | `curriculum/b2_advanced/high_stakes_production/writing_task3_perfection.md` | Writing Task 3: 120–180 words complete synthesis + reasoned original thesis. |
| **NEW** | `curriculum/b2_advanced/high_stakes_production/speaking_task2_3_b2_tactics.md` | Sustaining 4.5 minutes in Task 3; leading examiner in Task 2. |
| **NEW** | `curriculum/b2_advanced/high_stakes_production/project_b2_milestone_mock.md` | Project: Full 4-part B2 milestone mock exam evaluating NCLC 7 benchmark. |

#### Sub-phase 4E: Path 04 — TCF Canada Exam Prep (~60 hours / 16 lessons + 4 projects)
Focus: Psychological readiness, unassisted typing drills, distractor dissection, full-dress simulations.

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `curriculum/tcf_prep/exam_mechanics/listening_prediction_and_choice_scanning.md` | Utilizing the 10-second preview window to predict answers. |
| **NEW** | `curriculum/tcf_prep/exam_mechanics/distractor_dissection_negatives_friends.md` | Catching false friends, reversed polarity, and chronological misdirection. |
| **NEW** | `curriculum/tcf_prep/exam_mechanics/reading_pacing_blueprint.md` | Strict time allocation: A1–A2 (15 min), B1 (15 min), B2–C1 (30 min). |
| **NEW** | `curriculum/tcf_prep/exam_mechanics/the_five_second_drop_rule.md` | Mental resilience: how to let go of missed audio questions without spiraling. |
| **NEW** | `curriculum/tcf_prep/exam_mechanics/project_timed_mcq_sprint.md` | Project: Back-to-back timed Listening (35 min) + Reading (60 min) sprint. |
| **NEW** | `curriculum/tcf_prep/writing_speed/typing_french_under_exam_conditions.md` | Typing on QWERTY/AZERTY without spellcheck; muscle memory for French accents. |
| **NEW** | `curriculum/tcf_prep/writing_speed/writing_task1_speed_drill.md` | 80 words in 12 minutes with 3 minutes of proofreading. |
| **NEW** | `curriculum/tcf_prep/writing_speed/writing_task2_speed_drill.md` | 135 words in 16 minutes with 4 minutes of proofreading. |
| **NEW** | `curriculum/tcf_prep/writing_speed/writing_task3_speed_drill.md` | 150 words synthesis + stance in 20 minutes with 5 minutes proofreading. |
| **NEW** | `curriculum/tcf_prep/writing_speed/project_full_timed_writing_simulation.md` | Project: Complete 3-task writing test in 60 minutes sharp under TCF-SO rules. |
| **NEW** | `curriculum/tcf_prep/speaking_pressure/task1_modular_intro_framework.md` | Modular self-intro components; handling unexpected examiner follow-ups. |
| **NEW** | `curriculum/tcf_prep/speaking_pressure/task2_two_minute_prep_template.md` | Rapid question generation grid (Who, What, Where, When, Cost, Rules, Terms). |
| **NEW** | `curriculum/tcf_prep/speaking_pressure/task3_sustaining_the_monologue.md` | The "Rule of Three" arguments + concrete societal illustrations for 4.5 min. |
| **NEW** | `curriculum/tcf_prep/speaking_pressure/overcoming_hesitations_and_recovery.md` | High-register fillers (*en effet, force est de constater, d'ailleurs*) and repair strategies. |
| **NEW** | `curriculum/tcf_prep/speaking_pressure/project_full_speaking_simulation.md` | Project: 12-minute timed speaking simulation with recorded evidence. |
| **NEW** | `curriculum/tcf_prep/full_rehearsals/rehearsal_exam_1_protocol.md` | Protocol and setup for Full Official Mock Sitting #1. |
| **NEW** | `curriculum/tcf_prep/full_rehearsals/diagnostic_recovery_blueprint.md` | Step-by-step weakness triage based on Mock Sitting #1 score log. |
| **NEW** | `curriculum/tcf_prep/full_rehearsals/rehearsal_exam_2_protocol.md` | Protocol and setup for Full Official Mock Sitting #2. |
| **NEW** | `curriculum/tcf_prep/full_rehearsals/test_day_logistics_and_psychology.md` | Arrival, ID rules, computer login, fatigue management, break logistics. |
| **NEW** | `curriculum/tcf_prep/full_rehearsals/project_final_readiness_audit.md` | Project: Complete evidence portfolio check and final NCLC score verification. |

#### Sub-phase 4F: Path 05 — B2+ Safety Margin (~60 hours / 8 lessons + 2 projects)
Focus: Pushing comfortably into C1 territory (NCLC 8–9) to make NCLC 7 immune to bad test-day conditions.

| Action | Target File | Description |
| :--- | :--- | :--- |
| **NEW** | `curriculum/b2_safety/advanced_grammar/passe_simple_recognition.md` | Recognizing literary past tenses in high-difficulty reading texts. |
| **NEW** | `curriculum/b2_safety/advanced_grammar/conditionnel_passe_regrets.md` | Expressing past hypotheses and unfulfilled outcomes (*si j'avais su...*). |
| **NEW** | `curriculum/b2_safety/advanced_grammar/subjonctif_passe_concordance.md` | Elevating writing conclusions with past subjunctive structures. |
| **NEW** | `curriculum/b2_safety/advanced_grammar/cultural_metaphors_and_idioms.md` | Implicit cultural metaphors in Canadian political and media discourse. |
| **NEW** | `curriculum/b2_safety/advanced_grammar/project_c1_argumentative_essay.md` | Project: 200-word deep-dive essay on technological or environmental policy. |
| **NEW** | `curriculum/b2_safety/spontaneous_debate/counter_intuitive_prompt_defense.md` | Defending complex or counter-intuitive positions with zero preparation. |
| **NEW** | `curriculum/b2_safety/spontaneous_debate/sophisticated_rhetorical_connectors.md` | Advanced rhetorical tools: *non seulement... mais encore, qui plus est*. |
| **NEW** | `curriculum/b2_safety/spontaneous_debate/pronunciation_intonation_cadence.md` | Eliminating English stress patterns; refining French rhythmic groups. |
| **NEW** | `curriculum/b2_safety/spontaneous_debate/project_c1_spoken_defense_challenge.md` | Project: 5-minute unscripted defense responding to hostile counter-arguments. |
| **NEW** | `curriculum/b2_safety/spontaneous_debate/project_safety_margin_final_mock.md` | Project: Full final mock aiming for NCLC 8–9 (Listening ≥ 503, Reading ≥ 499). |

---

### Phase 5: Upgrading Projects & Evaluation Infrastructure
*Ensure every project has verifiable evidence, FEI rubric tables, automated word-count warnings, and calibrated AI evaluation prompts.*
* **Dependencies**: Phase 4.
* **Estimated Size**: Medium (~3–4 days).

| Action | Target File | Description |
| :--- | :--- | :--- |
| **EDIT** | All project files (`project_*.md`) across paths | Ensure each project file contains: (1) exact TCF task timer; (2) official FEI 4-criteria rubric table; (3) calibrated copy-paste AI feedback prompt; (4) explicit evidence checklist. |
| **NEW** | `templates/ai_evaluator_prompts/writing_task1_prompt.md` | Standard prompt template for AI self-evaluation of Writing Task 1 with strict word-count penalty checks. |
| **NEW** | `templates/ai_evaluator_prompts/writing_task2_prompt.md` | Standard prompt template for AI self-evaluation of Writing Task 2 with argument cohesion checks. |
| **NEW** | `templates/ai_evaluator_prompts/writing_task3_prompt.md` | Standard prompt template for AI self-evaluation of Writing Task 3 with document paraphrase vs copying analysis. |
| **NEW** | `templates/ai_evaluator_prompts/speaking_task_prompt.md` | Standard prompt template for AI transcription review of Speaking Tasks 1, 2, and 3. |

---

### Phase 6: Final Verification & Build
*Validate all links, anchors, site builds, and pedagogical continuity.*
* **Dependencies**: Phase 5.
* **Estimated Size**: Medium (~2 days).

| Action | Target File | Description |
| :--- | :--- | :--- |
| **RUN** | `python3 scripts/validate.py` | Run local structural validation to verify headings, anchor tags, and required sections across all paths. |
| **RUN** | `python3 scripts/validate.py --links` | Run automated external link validation to guarantee 100% of external resources resolve with HTTP 200. |
| **RUN** | `python3 scripts/build.py` | Verify that the static build and site generator render every path, section, lesson, and project cleanly. |
| **EDIT** | `sitemap.xml` | Update sitemap to include all newly generated lesson and project URLs. |

---

## 4. Phase Dependencies & Sequence Diagram

```
Phase 1: Verified Exam & Doc Bugs
  │
  ▼
Phase 2: Infrastructure & Validator Tooling
  │
  ▼
Phase 3: Restructuring & Manifest (curriculum.json)
  │
  ├───────────────────────────────────────────┐
  ▼                                           ▼
Phase 4: Writing Lessons (A1 → B2+)       Phase 5: Upgrading Projects & Prompts
  │                                           │
  └─────────────────────┬─────────────────────┘
                        ▼
Phase 6: Final Verification & Link Audit
```

---

## 5. Effort & Milestone Estimates

| Phase | Description | Estimated Effort | Milestone Target |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Verified Bugs & Exam Realities | ~1 day | Corrected score charts & TCF-SO documentation live |
| **Phase 2** | Infrastructure, Templates & Validator | ~2–3 days | All templates, score logs, and `validate.py` rules operational |
| **Phase 3** | Restructuring & Full Manifest | ~2 days | `curriculum.json` fully populated across all 6 paths |
| **Phase 4A**| Path 00 (A1 Basics) Lessons & Projects | ~1 week | Complete A1 path written and verified |
| **Phase 4B**| Path 01 (A2 Survival) Lessons & Projects | ~1.5 weeks | Complete A2 path with first milestone mock live |
| **Phase 4C**| Path 02 (B1 Independent) Lessons & Projects| ~2 weeks | Complete B1 path with Speaking/Writing simulators |
| **Phase 4D**| Path 03 (B2 Advanced) Lessons & Projects | ~2.5 weeks | Complete B2 path hitting Upper B2 requirements |
| **Phase 4E**| Path 04 (TCF Prep) Lessons & Projects | ~1.5 weeks | Exam mechanics, unassisted typing drills & mock exams |
| **Phase 4F**| Path 05 (B2+ Safety Margin) Lessons | ~1 week | Mandatory C1 buffer path completed |
| **Phase 5** | Project Rubrics & AI Evaluator Prompts | ~3 days | Standardized rubrics and prompt suite deployed |
| **Phase 6** | Final Verification, Link Check & Build | ~2 days | 100% green validation across all lessons and links |
