# Zéro French — Accuracy Audit

**Date:** 2026-10-31 · **Scope:** all 110 lesson/project files + `curriculum/tcf.md` + `curriculum/about.md` · **Mode:** read-only audit, no files changed.

This audit checks the **correctness** of the content: French grammar, translations, Québec claims, phonetics/IPA, answer keys, and TCF Canada / IRCC facts. It does not cover pedagogy, formatting, links or audio.

> ⚠️ This audit was done by AI reviewers (Claude), which checked some points against official sources (IRCC, FEI, OQLF, Usito, Académie française). Items marked **Check** could not be confirmed and need a native speaker or an official source. Everything Québec-specific should still get a final native review.

## How to use this file

1. **Fix Part 2 first.** These errors repeat across dozens of files, so they're cheaper to fix with one global pass each than file by file.
2. **Then work through Part 3**, the file-specific errors grouped by path.
3. **Use Part 1 as the single source of truth** for every exam/immigration fact. Do not reintroduce numbers that aren't in it.
4. After each fix, update PROGRESS.md and mark idioms/regionalisms for native review.

## Overall verdict

- **The French itself is mostly sound.** Conjugation tables, si-clauses, subjunctive triggers, passé simple forms and most answer keys are correct. `b2_advanced/argumentation_mastery/` is clean.
- **The biggest problem is invented exam and immigration facts, presented as official.** Every path contains made-up item-number→level maps, invented interface timings, invented raw-score conversions, fabricated "official FEI" grids, quotes and regulations, and wrong NCLC bands. A learner who trusts these tables will misjudge whether they've reached NCLC 7.
- **Québec content is the weakest linguistically.** It includes invented or mis-glossed québécismes (*donner son voyage*, *un brun*, *cabaret* = cart), affrication applied where it never occurs (*député*, *équipe*, *tout*), and many pan-French words wrongly tagged **(QC)**.
- **Model-answer word counts are routinely inflated.** Several "model" answers are actually below the word floor the lesson says is penalized.

---

## Part 1 — Reference facts (single source of truth)

Use these everywhere. Sources: IRCC equivalency table (canada.ca), France Éducation international (FEI).

**TCF Canada → NCLC (IRCC)**

| NCLC | Compréhension orale | Compréhension écrite | Expression écrite / orale (/20) |
|---|---|---|---|
| 10+ | 549–699 | 549–699 | 16–20 |
| 9 | 523–548 | 524–548 | 14–15 |
| 8 | 503–522 | 499–523 | 12–13 |
| **7** | **458–502** | **453–498** | **10–11** |
| 6 | 398–457 | 406–452 | 7–9 |
| 5 | 369–397 | 375–405 | 6 |
| 4 | 331–368 | 342–374 | 4–5 |

**Exam format**
- CO: 39 items, 35 min. CE: 39 items, 60 min. Both scored 0–699. Items get progressively harder. **No official item-number→level map, and no official raw→scaled conversion**, because items are weighted by difficulty.
- EE: 60 min, 3 tasks. T1 60–120 words, T2 120–150, T3 120–180. FEI sample T3 split: about **40–60 words** presenting the two documents' views, plus about **80–120 words** of personal opinion. EE gets one overall score /20; there are no published per-task scores.
- EO: 12 min, face-to-face with an examiner. **T1** *Entretien dirigé*, 2 min, **no preparation**. **T2** interaction, **2 min preparation + 3 min 30**. **T3** *expression d'un point de vue*, 4 min 30, no preparation, and **the examiner may intervene**. It is not an adversarial debate. EO gets one overall score /20.
- Word counting: the FEI/DELF convention is that a word is **any string between two spaces** (*j'ai* = 1, *c'est-à-dire* = 1). Confirm against the current TCF Canada candidate guide and cite it.
- Proportions of Canadian accents in the audio, preview/answer windows in seconds, auto-advance chimes, flag tools, back-navigation, break lengths, keyboard layouts at centres, sanctions: **none are published**. Don't state numbers; tell learners to check their *convocation* and the FEI candidate rules.

**Immigration**
- CRS French bonus: requires **NCLC 7+ in all four French skills**. It is **50 points** if English is CLB 5+, and **25 points** if English is CLB 4 or lower. The two amounts don't stack, so the maximum is 50.
- NCLC 7 is the **threshold** for the French bonus, French category-based draws and FSW eligibility. It is **not "maximum CRS points"**, because language points keep rising up to CLB 10.
- *Mobilité francophone* is a **temporary work-permit** stream (NCLC 5), not a PR pathway.
- TEF Canada is run by **CCI Paris Île-de-France**, not FEI.

---

## Part 2 — Errors repeated across many files (fix globally)

| # | Error | Fix | Where it occurs |
|---|---|---|---|
| S1 | **Wrong NCLC bands.** Most often EE/EO "NCLC 7 = 10–13 / 12–13 / 10–12 / 12–15.5"; "C1 = NCLC 8–9"; CO/CE bands like "503–568 = NCLC 8–9", "300–397 = NCLC 5", "569+ = C2". | Replace every table with Part 1. Remove CEFR↔NCLC claims not backed by IRCC. | b2_safety: every file (C1 = NCLC 8–9), `project_c1_argumentative_essay.md:187–213`, `project_c1_spoken_defense_challenge.md:174–200`, `project_safety_margin_final_mock.md:17–20, 79–82, 177–195, 205` · b2_advanced: `project_tcf_listening_sprint.md:265–274`, `project_tcf_reading_marathon.md:236–251`, `project_b2_milestone_mock.md:17–18, 44–47, 163–166`, `writing_task1_perfection.md:16` · tcf_prep: `project_timed_mcq_sprint.md:125–138`, `the_five_second_drop_rule.md:100–120`, `rehearsal_exam_1_protocol.md:105–110, 195–209`, `project_full_speaking_simulation.md:13, 137–144`, `project_full_timed_writing_simulation.md:13, 128–135` · a2: `project_a2_milestone_mock.md:5, 12, 193`, `project_apartment_inquiry_roleplay.md:80–82`, `project_past_vacation_recount.md:74–75`, `project_career_profile_and_goals.md:73` · a1: `project_introduce_yourself.md:69–70`, `project_a1_capstone.md:95–97` |
| S2 | **Invented raw-score conversions** ("29/39 = 458", "28/39 = 452", "+1 raw item = +15 pts", "allowable errors"). The files also contradict each other (28 vs 29). | Delete every raw-correct-answer column and claim. | `the_five_second_drop_rule.md:100–120`, `project_final_readiness_audit.md:41, 46, 72, 84`, `project_timed_mcq_sprint.md:125–138`, `rehearsal_exam_2_protocol.md:131–133`, `project_tcf_listening_sprint.md:265–280`, `project_tcf_reading_marathon.md:5, 236–251`, `project_b2_milestone_mock.md:44–45`, `project_safety_margin_final_mock.md:17–20` |
| S3 | **Invented item-number→level/genre maps** ("items 1–8 test spelled names", "items 13–24 = B1", "items 26–39 = editorials", "300–450-word texts"). They contradict each other across files. | Replace with "early items are easier, later items harder". No numbers. | Nearly every lesson with an Exam tip. Key spots: a1 `alphabet_and_accents.md:5, 197`, `vowels_and_nasals.md:205–210`, `numbers_time_dates.md:5, 257`, `everyday_objects_and_gender.md:5, 195`, `places_in_town_and_prepositions.md:221` · a2 `tcf_a2_reading_signage_notices.md:3, 27–39, 83, 128`, `apartment_features_and_ads.md:6, 141`, `tcf_listening_short_announcements.md:5` · b1 `quebec_lexicon_and_phonology.md:166`, `tcf_b1_listening_reading_tactics.md:18–30, 70–78`, `radio_bulletins_rfi_radiocanada.md:7, 19, 106, 120`, `reading_francophone_press.md:10–22, 149–151, 264` · b2 `canadian_accents_and_idioms.md:5, 19, 86, 189`, `decoding_rapid_spontaneous_speech.md:5, 90, 125`, `tcf_listening_advanced_drills.md:3–55`, `radiocanada_podcasts_analysis.md:7, 120`, all `editorial_reading/*` files · tcf_prep `distractor_dissection_negatives_friends.md:84, 127`, `listening_prediction_and_choice_scanning.md:113–117`, `project_timed_mcq_sprint.md:53–92`, `reading_pacing_blueprint.md:8–46`, `project_final_readiness_audit.md:74–75` · b2_safety `cultural_metaphors_and_idioms.md:5`, `passe_simple_recognition.md:11` |
| S4 | **Invented interface mechanics and timings**: "10-second preview", "chime + 5 s auto-advance", "10–20 s to answer", "adaptive difficulty", flag tool, back-navigation, "10-minute intermission". They're also impossible (39 × 80 s > 35 min). | Say: audio plays once, read the question, answer, move on. Hedge anything about navigation ("check the FEI candidate guide"). | `listening_prediction_and_choice_scanning.md:9–11, 30–33, 125`, `the_five_second_drop_rule.md` (whole premise: 8, 12, 63, 92), `reading_pacing_blueprint.md:25, 61, 86–90, 114`, `rehearsal_exam_1_protocol.md:12, 23, 72, 88`, `tcf_b1_listening_reading_tactics.md:6, 15, 40`, `project_b1_milestone_mock.md:35`, `radio_bulletins_rfi_radiocanada.md:8, 132`, `tcf_listening_short_announcements.md:9–11, 136`, `imparfait_descriptions_habits.md:184`, `vowels_and_nasals.md:205–210`, `project_tcf_listening_sprint.md:5, 11` |
| S5 | **Invented statistics** ("30–40% of tracks are Canadian", "80% of questions answered in the chapô", "70% of subjunctive contexts", "60% of upper-tier errors", "TCF audio systematically includes Acadian/Franco-Ontarian speakers"). | Delete. At most: "you may hear varied francophone accents." | `radio_bulletins_rfi_radiocanada.md:99`, `reading_francophone_press.md:89`, `subjonctif_present_triggers.md:84`, `distractor_dissection_negatives_friends.md:7`, `listening_prediction_and_choice_scanning.md:94, 187`, `canadian_accents_and_idioms.md:3, 350`, `quebec_lexicon_and_phonology.md:3–5`, `vowels_and_nasals.md:185, 194`, `sophisticated_rhetorical_connectors.md:3` (25%) |
| S6 | **Fabricated "official" documents**: "official FEI evaluation grids" with invented criteria and point splits, a quoted FEI jury report, a "Règlement général des sessions TCF Canada — Article 4", a "Règlement officiel TCF-SO", an FEI quote about striking copied words, and invented criterion names (*Aisance phonologique…*, *Correction phonétique*, *Prise d'initiative…*). | Relabel every grid as an "unofficial self-assessment rubric". Label invented texts "fictional practice text". Remove fake quotations and criterion names. | `project_c1_argumentative_essay.md:187–213`, `project_c1_spoken_defense_challenge.md:174–200`, `pronunciation_intonation_cadence.md:3`, `project_b2_milestone_mock.md:150–157`, `writing_task3_perfection.md:64–69`, `diagnostic_recovery_blueprint.md:235–241`, `test_day_logistics_and_psychology.md:210–215`, `typing_french_under_exam_conditions.md:289–293`, `tcf_speaking_task2_negotiation.md:16, 26–33`, `project_a2_milestone_mock.md:186–188, 210–216`, `project_apartment_inquiry_roleplay.md:70`, `project_past_vacation_recount.md:63`, `project_career_profile_and_goals.md:61`, `project_pronunciation_benchmark.md:5`, plus "official FEI 4-criteria matrix" in most projects |
| S7 | **Invented penalty rules**: "elisions count as 2 words", "copied 3-word strings struck from the word count", "words beyond 120/150/180 crossed out", "caps your score at A1", "éliminatoire", "cuts task mark by 50%", "automated scoring". | Use the Part 1 word-count rule. Rephrase penalties as advice: "length and copying affect task completion." | Elision rule: `canadian_immigration_integration.md:213`, `project_b1_milestone_mock.md:166`, `project_current_event_digest.md:61, 116, 191`, `project_writing_task2_letter.md:9, 50, 93, 173`, `project_a2_milestone_mock.md:211`, `project_past_vacation_recount.md:43, 92`, `project_career_profile_and_goals.md:43, 179`, `project_a1_capstone.md:62, 89`, `project_daily_routine_and_neighborhood.md:40–43, 87`, `project_c1_argumentative_essay.md:142`, `writing_task1_perfection.md:11–12, 66–99, 283`, `writing_task1_speed_drill.md:7, 42–63`, `project_full_timed_writing_simulation.md:162–166` · Copy strike-out: `writing_task3_speed_drill.md:3, 11, 53–59`, `writing_task3_perfection.md:64–69, 101–116`, `writing_task2_perfection.md:63–78`, `diagnostic_recovery_blueprint.md:5, 191, 205, 251` · "Caps at A1/A2": `project_apartment_inquiry_roleplay.md:9–10`, `narrative_chronology_connectors.md:165`, `professions_and_workplace_tasks.md:6, 27`, `structuring_arguments_concession.md:12`, `conditionnel_present.md:161`, `tcf.md:81`, `greetings_and_politeness.md:5`, `silent_letters_and_liaisons.md:7, 202` |
| S8 | **Speaking tasks misdescribed.** T1 given "1 minute preparation"; T2 "no preparation"; T3 as an adversarial debate with a "hostile persona" or "mandatory interruptions"; T3 "without interruption" / "examiner stays silent"; T2 "10–12 questions mandated" with "deliberate objection"; *Entretien guidé*. | Use the Part 1 descriptions. | T1 prep: `project_past_vacation_recount.md:24, 29`, `project_career_profile_and_goals.md:24, 29` · T2 no prep: `project_a2_milestone_mock.md:165`, `tcf_speaking_task2_negotiation.md:3, 7` · T3 debate: `counter_intuitive_prompt_defense.md:3, 141`, `project_safety_margin_final_mock.md:132–134`, `project_c1_spoken_defense_challenge.md:3, 7–12`, `project_current_event_digest.md:7` · T3 silent: `project_speaking_task3_simulator.md:5`, `project_b2_milestone_mock.md:115, 127`, `speaking_task2_3_b2_tactics.md:6, 12`, `project_full_speaking_simulation.md:93`, `task3_sustaining_the_monologue.md:13, 57` · T1/T2 protocol: `task1_modular_intro_framework.md:3, 50–52`, `project_final_readiness_audit.md:120`, `project_full_speaking_simulation.md:83, 126, 181`, `task2_two_minute_prep_template.md:5, 22`, `test_day_logistics_and_psychology.md:181` |
| S9 | **CRS / immigration facts wrong**: "+50 for French plus up to 25 for bilingual", "+50–75", "+50 per skill", "NCLC 7 = maximum CRS points", "NCLC 6 = competitive Express Entry level", Mobilité francophone as a PR pathway. | Use Part 1. | `tcf.md:63`, `project_safety_margin_final_mock.md:5, 8–10, 43`, `project_b2_milestone_mock.md:20`, `project_tcf_listening_sprint.md:272, 280`, `project_tcf_reading_marathon.md:5`, `project_timed_mcq_sprint.md:129, 135`, `the_five_second_drop_rule.md:120`, `project_final_readiness_audit.md:172–175`, `project_full_speaking_simulation.md:13`, `project_career_profile_and_goals.md:73` |
| S10 | **Model-answer word counts inflated.** Several models are below their own floor. | Recount every model answer by space-delimited words. Lengthen any that fall under the floor. | **Below floor:** `writing_task2_perfection.md:140–175, 240–248` (all 3), `writing_task2_speed_drill.md:123–131, 250–252` (answer key gives the wrong verdict), `canadian_immigration_integration.md:232`, `project_current_event_digest.md:156`, `structuring_arguments_concession.md:234–236`, `project_career_profile_and_goals.md:136` · **Inflated:** `writing_task1_perfection.md:184–198, 347–362`, `writing_task3_perfection.md:160–186, 261–267`, `writing_task1_speed_drill.md:114, 146, 280`, `writing_task3_speed_drill.md:155–160, 208–210, 241–260`, `discourse_connectors_b1.md:275`, `project_speaking_task3_simulator.md:118–136`, `task1_modular_intro_framework.md:223, 229`, `task3_sustaining_the_monologue.md:51` |
| S11 | **Writing Task 3 structure wrong** (65–75-word synthesis + 75–95 opinion). | Teach 40–60 + 80–120. | `writing_task3_perfection.md:9, 38–44`, `writing_task3_speed_drill.md:34, 114`, `diagnostic_recovery_blueprint.md:107` |
| S12 | **Pan-French words tagged (QC)** or given a false Québec/France contrast. | Remove the (QC) tag or the false contrast. Keep (QC) only on genuine québécismes. | *pourboire, café allongé* (`cafe_and_transactions.md:190, 246, 257`) · *tempête de neige, pelleter* (`weather_and_seasons.md:152, 155`) · *électroménagers* (`apartment_features_and_ads.md:195`) · *tout d'un coup* (`narrative_chronology_connectors.md:145`) · *boîte vocale* vs *répondeur* (`tcf_listening_short_announcements.md:125`) · *bien pire* (`comparisons_and_superlatives.md:168`) · *concertation sociale* (`analyzing_academic_journalistic_texts.md:132`) · *un beau gâchis, tempête dans un verre d'eau* (`detecting_bias_irony_implied_meaning.md:106–108`; the second is also mis-glossed) · *transport collectif, titre de transport* (`tcf_reading_advanced_drills.md:192–195`) · *consultation citoyenne, collecte sélective, usager* (`writing_task2_perfection.md:123–125`) · *densification urbaine, transition juste* (`writing_task3_perfection.md:193–195`) · *trottoir en travaux* (`reading_pacing_blueprint.md:173`) · *heure de pointe* (`writing_task2_speed_drill.md:143`) · *inscription, pièce d'identité, vestiaire…* (`rehearsal_exam_2_protocol.md:140–143`) · *stationner* intransitive (`listening_prediction_and_choice_scanning.md:181, 189`) · journalistic conditional, *avoir des remords, s'en vouloir* (`conditionnel_passe_regrets.md:177–178`) · *avoir le dos large, mettre le feu aux poudres* (`cultural_metaphors_and_idioms.md:272–273`) · *frais de scolarité, débrayage* (`counter_intuitive_prompt_defense.md:253–254`) · *au demeurant, à cet égard, force est de constater…* (`sophisticated_rhetorical_connectors.md:253–254`) |
| S13 | **Québec affrication applied wrongly.** /t d/ → [ts dz] **only before /i y j ɥ/**, but the lessons apply it to *député, équipe, déficitaire, -té, tout, décidé, bureau, ticket*. | Fix every transcription to follow the rule. Use valid examples: *tu, dire, partir, dur, dictature*. | `canadian_accents_and_idioms.md:44–45, 201, 273–274`, `radiocanada_podcasts_analysis.md:99, 109, 111–112, 267`, `decoding_rapid_spontaneous_speech.md:54–56, 83–86, 112`, `quebec_lexicon_and_phonology.md:170, 181, 183, 228, 236` |
| S14 | **Pronominal past-participle agreement** taught as "always agrees with the subject". | Add the rule: agreement follows a preceding direct object. With indirect *se* (*se téléphoner, se parler*) there is none: *elles se sont téléphoné*. | `passe_compose_etre.md:31, 138, 163–165`, `conditionnel_passe_regrets.md:63`, `subjonctif_passe_concordance.md:73` |
| S15 | **Missing [z] liaison** in *ils/qu'ils* + vowel-initial verb. | /il.z‿o.ʁɛ/, /kil.z‿ɛ/, /kil.z‿a.tɑ̃d/ | `conditionnel_passe_regrets.md:48, 59`, `subjonctif_passe_concordance.md:42, 54, 234`, `subjonctif_present_triggers.md:42` |
| S16 | **Calques/anglicisms presented as standard** with no register note: *bienvenue* (reply to *merci*), *breuvage*, *canne*, *liqueur*. | Mark them as familiar Québec usage that the OQLF advises against, and give the standard term (*de rien / je vous en prie*, *boisson*, *boîte de conserve*, *boisson gazeuse*). | `greetings_and_politeness.md:197`, `administrative_interactions.md:39, 49`, `cafe_and_transactions.md:194`, `food_and_partitives.md:220, 222`, `quebec_lexicon_and_phonology.md:28–29` |

---

## Part 3 — File-specific errors

Severity: **H** = teaches wrong French or a wrong fact · **M** = misleading or partly wrong · **L** = minor. Confidence is *Certain* unless marked *Likely* or **Check**. Rows already covered by Part 2 are omitted.

### Path 01 — A1 Basics (`curriculum/a1_basics/`, `tcf.md`, `about.md`)

| File:Line | Sev | Problem | Fix |
|---|---|---|---|
| `foundations_and_pronunciation/alphabet_and_accents.md:72` | H | Letter E /ə/ described as "rounded lips" (contradicts l.33) | "a neutral, relaxed vowel /ə/" |
| `…/alphabet_and_accents.md:128` | H | ô called "open"; *hôtel* given as /lo.tɛl/ | ê = open /ɛ/; ô = closed /o/ (/o.tɛl/); î, û unchanged |
| `…/alphabet_and_accents.md:140, 221` | L | Without the cédille *français* would sound "franka" | "frankè" /fʁɑ̃.kɛ/ |
| `…/alphabet_and_accents.md:189` | M | Canadian French (CA-FR) and Canadian Multilingual Standard (CMS) keyboards merged into one (*Likely*) | Name them as two layouts |
| `…/vowels_and_nasals.md:170, 239` | L | "ll is silent" in *-ille* | *ill* = /ij/ |
| `…/vowels_and_nasals.md:180` | L | Merged *un brin/un brun* as /œ̃ bʁɛ̃/ | /ɛ̃ bʁɛ̃/ |
| `…/vowels_and_nasals.md:188` | L | *père* given a circumflex; *midi* used as a laxing example (*Likely*) | Laxing occurs in closed syllables: *vite, musique* |
| `…/silent_letters_and_liaisons.md:3` | L | "*ils parlent* … /paʁl/" | "*parlent* = 4 sounds" |
| `…/silent_letters_and_liaisons.md:31` | L | Silent-S example *les amis* shows a pronounced liaison | *les chats* /le ʃa/ |
| `…/silent_letters_and_liaisons.md:157` | L | *héros*, *haricot* called Germanic h (*Likely*) | Drop "Germanic", or use *haut, hache, honte* |
| `…/numbers_time_dates.md:32` | L | "un ami" called a contraction | Liaison |
| `…/numbers_time_dates.md:148–149` | M | "Never say *douze heures* / *zéro heure*" (both are standard in the 24-hour system) | Restrict to 12-hour style |
| `…/project_pronunciation_benchmark.md:46–47` | L | *ont‿un* listed as a mandatory liaison (*Likely*) | Optional |
| `greetings_and_introductions/greetings_and_politeness.md:40, 50` | M | "No *bonjour* on the phone"; *allô* "never face to face" | *Allô, bonjour* is normal; *allô* is an informal in-person greeting in Québec |
| `…/personal_identity_and_verbs.md:51` | M | "je suis d'origine [pays]" (*Likely*) | *d'origine brésilienne* / *je viens du Brésil* |
| `…/personal_identity_and_verbs.md:157` | L | "Je suis un ingénieur" marked ungrammatical (*Likely*) | "Unnatural" |
| `…/everyday_objects_and_gender.md:69` | L | *une* "with liaison" | *une* = enchaînement |
| `…/everyday_objects_and_gender.md:147` | L | -ode/-ade/-ude "90% feminine" with no exceptions (*Likely*) | Add *le code, l'épisode, le stade* |
| `…/family_and_relationships.md:46` | M | *parents* "only mother and father"; *proches* = relatives | *parent* can mean any relative; *la parenté* (QC) |
| `food_shopping_needs/cafe_and_transactions.md:136` | M | *quatre euros* /katʁ.z‿ø.ʁo/ | /ka.tʁø.ʁo/ |
| `…/cafe_and_transactions.md:166–168, 195` | M | "Never ask for *l'addition* in Québec" (*Likely*) | *L'addition* is normal; *facture* is also heard |
| `…/cafe_and_transactions.md:189` | M | France: "by law a 15% service charge" (*Likely*) | The law requires *service compris* pricing; no 15% rate is set |
| `…/cafe_and_transactions.md:190` | M | Lower tipped minimum wage "in Canada" (*Likely*) | Québec only (Ontario and B.C. abolished theirs) |
| `…/food_and_partitives.md:75` | L | *alors elle* /a.lɔʁ.z‿ɛl/ (*Likely*) | /a.lɔʁ ɛl/ |
| `…/food_and_partitives.md:218` | M | *l'arabe du coin* taught with no warning | Remove, or flag as a potentially offensive colloquialism |
| `…/food_and_partitives.md:219` | H | *cabaret* (QC) = shopping cart | *cabaret* (QC) = serving tray; cart = *panier d'épicerie* / *carrosse* (fam.) |
| `…/food_and_partitives.md:232` | L | Price asked per *livre*, answered per *kilo* | Use the same unit |
| `…/clothing_and_agreements.md:155` | L | Noun-derived colours "invariable", with no exceptions | Add *rose, mauve, fauve, écarlate* |
| `…/weather_and_seasons.md:66` | L | *geler* "only 3rd person" | Only *pleuvoir, neiger, grêler* |
| `…/weather_and_seasons.md:153, 223` | L | *verglas* = freezing rain (*Likely*) | *verglas* = black ice; *pluie verglaçante* = freezing rain |
| `…/weather_and_seasons.md:151` | L | *bordée* "15–30 cm" (**Check**) | "a heavy snowfall" |
| `daily_routine_and_places/regular_er_verbs.md:170` | L | "j'utilise le métro" (*Likely*) | "je prends le métro" |
| `…/irregular_verbs_triad.md:23` | L | *ira* listed as a present-tense stem | "stems across tenses" |
| `…/irregular_verbs_triad.md:174` | M | "*de la* for feminine countries" | *venir de France* (no article) |
| `…/irregular_verbs_triad.md:203` | L | "nous faisons une réunion" (*Likely*) | "nous avons une réunion" |
| `…/asking_questions_basics.md:121` | M | *Quand arrive-t-il* with a [t] liaison (*Likely*) | /kɑ̃ a.ʁiv.til/; use *quand est-ce que* for the liaison |
| `…/asking_questions_basics.md:5` | L | Ask the examiner "10–15 questions" (**Check**) | "relevant questions" |
| `…/places_in_town_and_prepositions.md:48` | L | *la mairie* labelled masculine | f. (*mairie*) / m. (*hôtel de ville*) |

### Path 02 — A2 Survival (`curriculum/a2_survival/`)

| File:Line | Sev | Problem | Fix |
|---|---|---|---|
| `housing_and_transit/formal_questioning_techniques.md:136–137` | H | Correct French "Pourriez-vous me dire où est l'appartement ?" marked as an error | Use a real error: "*…où est-il ?*" → "*…où il se trouve*" |
| `…/formal_questioning_techniques.md:43` | L | *Où se trouve l'appartement ?* called pronoun inversion | Stylistic inversion; use *Où se trouve-t-il ?* |
| `…/formal_questioning_techniques.md:62, 64` | L | IPA doubles the /t/ in *-t-il* | /a.bi.til/ |
| `health_and_public_services/pronouns_y_and_en.md:116` | M | "*en* cannot replace people" (contradicted by l.95) | *En* is fine for quantities and indefinites; use *de lui/d'elle* for specific people |
| `past_narratives/passe_compose_avoir.md:159` | M | "Verbs of motion take être" | Only the être-list; *marcher, courir, voyager* take avoir |
| `past_narratives/passe_compose_etre.md:103` | L | *se lever* = "wake up" | "get up" (*se réveiller* = wake up) |
| `…/passe_compose_etre.md:219` | L | *passer un examen* = "pass" (*Likely*) | "take/sit" (*réussir* = pass) |
| `…/narrative_chronology_connectors.md:123` | L | "l'électricité a coupé" (*Likely*) | "le courant a été coupé" |
| `…/narrative_chronology_connectors.md:188` | L | "un orage de neige … a commencé à tomber" (*Likely*) | "une violente tempête de neige a éclaté" |
| `work_and_daily_life/passe_compose_vs_imparfait.md:82` | L | "la connexion Internet a coupé" (*Likely*) | "a été coupée" |
| `housing_and_transit/imparfait_descriptions_habits.md:181–182` | M | *je parlais* "two syllables"; the cue given is /ɛ/ | The reliable cue is *j'ai* /ʒe/ vs *je* /ʒə/ |
| `…/apartment_features_and_ads.md:63` | L | 1½ IPA liaison misplaced (*Likely*) | /œ̃ œ̃.n‿e dmi/ |
| `…/apartment_features_and_ads.md:129, 131` | L | Deposit ban attributed to the TAL; "officially" Moving Day (*Likely*) | Civil Code art. 1904; "popularly called" |
| `health_and_public_services/administrative_interactions.md:86` | L | SAAQ IPA (*Likely*) | /ɛs.a.a.ky/ |
| `…/medical_symptoms_and_advice.md:130` | M | France walk-in = *cabinet médical / SOS Médecins* (*Likely*) | *centre de soins non programmés / maison médicale de garde* |
| `…/medical_symptoms_and_advice.md:131` | L | RAMQ card "green" (**Check**) | Drop the colour |
| `…/medical_symptoms_and_advice.md:200` | M | CO "Listening Tasks 1 & 2" | CO is 39 MCQ items; no tasks |
| `…/medical_symptoms_and_advice.md:257` | L | *prendre* called "regular" | Irregular |
| `…/tcf_a2_reading_signage_notices.md:284` | L | *récupérer* IPA syllabification | /ʁe.ky.pe.ʁe/ |
| `work_and_daily_life/comparisons_and_superlatives.md:185` | L | Superlative + "que j'ai prise" in a B2 model (*Likely*) | "que j'aie prise" |
| `…/professions_and_workplace_tasks.md:99` | L | Canada: "never *un mail*" (*Likely*) | "*courriel* is the recommended term" |
| `…/project_career_profile_and_goals.md:132–153` | L | Double closing formula; mixed salutation (*Likely*) | One closing: « Veuillez agréer, Madame, Monsieur, … » |
| `…/project_career_profile_and_goals.md:158` | L | Commentary cites superlatives and irregular stems that aren't in the model | Fix the commentary |

### Path 03 — B1 Independent (`curriculum/b1_independent/`)

| File:Line | Sev | Problem | Fix |
|---|---|---|---|
| `media_and_society/relative_pronouns_qui_que_ou_dont.md:245` | H | "*dont les écologistes doutent de l'efficacité*" is ungrammatical, and the explanation is wrong (*Likely*) | "…dont les écologistes mettent en doute l'efficacité" |
| `…/relative_pronouns_qui_que_ou_dont.md:149` | M | "Strict order: dont + possessed noun + verb" | Give both patterns (noun as subject vs as object) |
| `politeness_and_hypotheses/conditionnel_present.md:180, 192` | H | Answer key "nous **aurions** plus souvent avec nos collègues" is nonsense | Rewrite the item so *avoir* has an object |
| `canadian_realities/discourse_connectors_b1.md:245–247` | H | Writing Task 3 given as 120–150 words | 120–180 |
| `…/discourse_connectors_b1.md:82, 88` | M | *à cause de* "strictly negative"; positive use marked ❌ | Neutral or negative; *grâce à* is the natural positive choice |
| `…/discourse_connectors_b1.md:166` | L | *en effet* glossed "in fact" (*Likely*) | Drop "in fact" (it conflicts with the *en fait* contrast) |
| `…/discourse_connectors_b1.md:271` | L | *Toutefois* misused in the model (*Likely*) | *En effet* / *Or* |
| `media_and_society/reported_speech_present.md:59` | M | "L'animatrice interroge s'ils…" (*Likely*) | "demande s'ils…" |
| `…/reported_speech_present.md:273, 284` | M | "explique si" (*Likely*) | "Lorsqu'on lui demande si…, l'élu répond que non" |
| `…/reported_speech_present.md:66` | L | *on* called "impersonal" | Indefinite |
| `opinions_and_social_debates/subjonctif_present_triggers.md:128` | M | "Subjunctive ONLY with two different subjects" | Applies only to will/emotion verbs (*Bien que je sois…* is fine) |
| `…/subjonctif_present_triggers.md:37` | L | "qu'j'" given as a form | "que j'" |
| `…/indicative_vs_subjunctive.md:79–81` | M | Opinion-verb questions "strictly take the subjunctive" (*Likely*) | Optional with inversion; indicative is also correct |
| `…/indicative_vs_subjunctive.md:163–164` | M | "Je ne doute pas qu'il **est** compétent" taught as the norm (*Likely*) | The norm is *qu'il soit*; the indicative is a variant |
| `…/indicative_vs_subjunctive.md:125` | L | "sans que personne **ne**…" (*Likely*) | Drop *ne* |
| `…/expressing_viewpoints_nuance.md:70–72, 242` | L | Overstated subjunctive rule; "Rien n'est moins sûr quant à…" (*Likely*) | Soften; use the phrase on its own |
| `…/structuring_arguments_concession.md:127, 132` | M | "OQLF recommends *en revanche* over *par contre*" | The OQLF says *par contre* is fully correct (same at `discourse_connectors_b1.md:158`) |
| `…/structuring_arguments_concession.md:234` | L | Carpooling called *transport collectif* | "mode de déplacement partagé" |
| `…/project_speaking_task3_simulator.md:140, 143, 144, 163` | M | Annotations: *bâtiront* called conditional; subjunctive cited that isn't in the text; *de surcroît* called contrast; *bien que… néanmoins* pleonasm | Fix the annotations |
| `canadian_realities/quebec_lexicon_and_phonology.md:53` | M | *le fun* /fœn/ (*Likely*) | /fɔn/ |
| `…/quebec_lexicon_and_phonology.md:127` | L | "*tu* drops elision" (backwards) | *tu* → *t'* informally |
| `…/quebec_lexicon_and_phonology.md:148, 155` | M | Sacres "exclusively" religious; originating in the Quiet Revolution | "Characteristically"; attested since the 19th century |
| `…/quebec_lexicon_and_phonology.md:31` | M | France: *pourboire* "obligatoire/15%" | *Service compris*; tip optional |
| `…/quebec_lexicon_and_phonology.md:17` | L | Canadian French "systematically" avoids anglicisms (*Likely*) | Limit to OQLF terminology |
| `…/canadian_immigration_integration.md:31` | M | "Outside Québec, immigration is managed by IRCC" | IRCC everywhere; Québec selects economic immigrants (CSQ) |
| `…/canadian_immigration_integration.md:98, 122` | L | Invented *tronc commun* metaphor; Québec law on Canadian experience (**Check**) | Remove or source |
| `…/project_b1_milestone_mock.md:39` | M | Exo Saint-Jérôme line → Gare Centrale / Cartier / TRAM pass (*Likely*) | Lucien-L'Allier / De la Concorde / zone pass |
| `…/tcf_b1_listening_reading_tactics.md:147, 161` | M | *dîner* answer key valid only in one dialect | Make it unambiguous ("dîner de demain midi") |
| `…/tcf_b1_listening_reading_tactics.md:34` | M | "Missing easy questions drags down your score" (*Likely*) | Remove (easy items carry the least weight) |
| `…/tcf_b1_listening_reading_tactics.md:168` | L | Saint-Michel / Pie-IX called "avenues" | Boulevards |
| `media_and_society/radio_bulletins_rfi_radiocanada.md:78, 81–82` | L | Syllables numbered 1–4 for a 5-syllable word; *autorités‿ont* called mandatory | Fix the count; the liaison is optional |
| `…/radio_bulletins_rfi_radiocanada.md:142` | L | "Nous ne sommes pas sans savoir" used as a false-negation trap | Use "Ce n'est guère réglé" |
| `…/reading_francophone_press.md:64–65` | L | "Refus gouvernemental de la proposition"; "Disparition du premier ministre" for leaving politics (*Likely*) | "Refus du gouvernement"; "Retrait du premier ministre" |
| `…/project_current_event_digest.md:181–182` | L | Transcript "~380 words / 130 wpm"; liaison example not in the text | ~275 words; fix the example |
| `politeness_and_hypotheses/project_writing_task2_letter.md:157` and `workplace_negotiation_disputes.md:114` | L | *Alternativement* (anglicism) | *Sinon* |
| `…/workplace_negotiation_disputes.md:80` | M | Canadian workplaces "governed by CNESST or federal standards" | Provincial employment standards; Canada Labour Code only for federal sectors |
| `…/si_clauses_structures_1_2.md:80, 197` | L | *loyer* /lwa.jɛ/; "Immigration Canada" | /lwa.je/; IRCC |

### Path 04 — B2 Advanced (`curriculum/b2_advanced/`)

`argumentation_mastery/` is clean.

| File:Line | Sev | Problem | Fix |
|---|---|---|---|
| `complex_audio_and_voices/canadian_accents_and_idioms.md:156, 270, 281–282` | H | *donner son voyage* = "to fire" (unattested) | *avoir son voyage* = be fed up; "to fire" = *mettre à la porte* |
| `…/canadian_accents_and_idioms.md:289` | H | "J'ai pantoute compris" / "Je n'ai pantoute compris" | "J'ai pas compris pantoute" |
| `…/canadian_accents_and_idioms.md:284` | M | *un brun* = milky coffee (invented, *Likely*) | Replace the item |
| `…/canadian_accents_and_idioms.md:304` | M | *pourboire* "gratification obligatoire" | Optional (~15% in Québec); also not a Canadianism |
| `…/canadian_accents_and_idioms.md:300` (also `high_stakes_production/speaking_task2_3_b2_tactics.md:83`) | L | *magasiner* = *faire les courses* | *faire du shopping / lèche-vitrine* |
| `…/canadian_accents_and_idioms.md:218` | L | "faire passer un sapin" (**Check**) | "passer un sapin à qqn" |
| `…/canadian_accents_and_idioms.md:46, 58, 60, 71, 78` | M | Laxing/diphthongization examples break their own rules (*partir, minute, sûr, jeune, maison*) | *lutte* [lʏt], *jeûne* [ʒøʏ̯n], *fête/père/neige* |
| `…/canadian_accents_and_idioms.md:269–270` | M | [tsy **ve**] for *veux*; [kɔ̃**p**.tabl] | [vø]; [kɔ̃.tabl] |
| `…/decoding_rapid_spontaneous_speech.md:164/172` | H | [ja **plys** d‿plas] = "il n'y a plus de place" | [ply] (negative *plus*) |
| `…/decoding_rapid_spontaneous_speech.md:165` | M | *je suis allé* [ʃɥi **t**‿a.le] (wrong liaison) | [ʃɥi a.le] / [ʃɥi.z‿a.le] |
| `…/decoding_rapid_spontaneous_speech.md:119, 221` | L | Two stressed syllables shown; *j'vous* called assimilation | Final-syllable stress; schwa deletion |
| `…/radiocanada_podcasts_analysis.md:58` | M | STM called a *société d'État*; wrong name | Use Hydro-Québec / Loto-Québec / SAQ; the name is "Société de transport de Montréal" |
| `…/radiocanada_podcasts_analysis.md:102, 236` | L | *fait* diphthongized; *alors que* called concessive | Remove; use *bien que / quoique* |
| `editorial_reading/detecting_bias_irony_implied_meaning.md:9` | M | Litotes defined as praise-for-condemnation | Litotes = understatement (*Va, je ne te hais point*) |
| `…/detecting_bias_irony_implied_meaning.md:47–60` | M | Journalistic conditional = "suspected falsehood / author skepticism" | Marks unconfirmed information only |
| `…/fast_elimination_keyword_traps.md:140` | L | *invalider* given as a false friend | Use *éventuellement / librairie / location* |
| `…/fast_elimination_keyword_traps.md:229` | L | Option A "contradicted" (it's unstated) | "unstated" |
| `…/fast_elimination_keyword_traps.md:271` (also `tcf_prep/…/distractor_dissection_negatives_friends.md:102–104`) | M | *ignorer* = "disregard" and *opportunité* = "chance" called wrong (*Likely*) | Both senses are in dictionaries but criticized; give both |
| `…/analyzing_academic_journalistic_texts.md:91–98` | L | *Faute d'avoir anticipé* called a participial clause | Prepositional infinitive phrase |
| `…/tcf_reading_advanced_drills.md:203` | L | "Revue québécoise de droit international **et comparé**" (*Likely*) | Remove "et comparé" |
| `high_stakes_production/writing_task1_perfection.md:357` | M | "Donne-m'en des nouvelles" (double pronoun) | "Donne-moi de leurs nouvelles" |
| `…/writing_task2_perfection.md:116` | L | Suggestion conditional labelled "journalistic" | Conditional of suggestion |
| `…/writing_task3_perfection.md:263–267` | M | Model copies 3–4-word chunks while claiming "zéro terme recopié"; "inculquer l'apprentissage" | Paraphrase; "favoriser l'apprentissage de l'altérité" |
| `…/project_b2_milestone_mock.md:115` | L | *Entretien guidé* | *Entretien dirigé* |

### Path 05 — TCF Canada Prep (`curriculum/tcf_prep/`)

| File:Line | Sev | Problem | Fix |
|---|---|---|---|
| `full_rehearsals/project_final_readiness_audit.md:141` (also `test_day_logistics_and_psychology.md:6, 37, 178`) | H | "Passport only; driver's licence rejected by IRCC" (*Likely*) | Original valid photo ID used at registration; check the centre's list |
| `…/test_day_logistics_and_psychology.md:8, 47, 65, 179` | M | Invented sanctions ("multi-year ban reported to IRCC"), entry cut-offs, crash procedure | Point to the convocation and the FEI rules |
| `…/test_day_logistics_and_psychology.md:199` | M | *attestation de comparution* (= court appearance) | *attestation de présence* |
| `…/rehearsal_exam_1_protocol.md:175, 178` | M | *note éliminatoire* (none exists); *choc thermique cognitif* (nonsense) | *seuil requis*; *fatigue cognitive* |
| `…/rehearsal_exam_1_protocol.md:36, 136` | M | "no backspace"; "centres use CMS/US-Intl, not AZERTY" (**Check**) | Backspace works; ask the centre |
| `…/rehearsal_exam_2_protocol.md:223` | M | EE/EO margins called "+19 to +30" (they're +3/+2 out of 20); verdict contradicts the SMI table | Restate per skill |
| `…/rehearsal_exam_2_protocol.md:60` | L | "TV5Monde TCF simulator Series B/C" (invented) | Remove |
| `…/diagnostic_recovery_blueprint.md:61` | L | *nonobstant* called a negative adverb | Preposition; use *guère* |
| `exam_mechanics/distractor_dissection_negatives_friends.md:118` | M | *bâtisse* "standard administrative QC term" (*Likely*) | Familiar; standard is *bâtiment/immeuble* |
| `…/distractor_dissection_negatives_friends.md:154` | L | "tambour et trompette" | "en grande pompe" |
| `…/distractor_dissection_negatives_friends.md:234/245` | L | Answer key uses *ne* in a "without *ne*" drill | "au lieu de démissionner, a réaffirmé…" |
| `…/listening_prediction_and_choice_scanning.md:5` (and others) | L | 458 called "upper B2" | NCLC 7 (mid-B2; TCF B2 = 400–499) |
| `…/project_timed_mcq_sprint.md:25, 186` | L | TV5Monde "official FEI partner / real past items" (**Check**) | Remove |
| `…/reading_pacing_blueprint.md:40, 224` | L | 15 min ÷ 14 items = "40–50 s" | ~60 s |
| `…/reading_pacing_blueprint.md:150` | M | "tout trajet … sera obligatoire en remplacement de l'avion" | "le train sera obligatoire pour tout trajet de moins de 4 h" |
| `…/the_five_second_drop_rule.md:136` | L | "4-7-8" breathing described as 2/5 | Rename, or give the correct counts |
| `speaking_pressure/task1_modular_intro_framework.md:7, 127` | M | *vos* /ve/; *en plein air* /plɛ̃n‿ɛʁ/ | /vo/; /plɛ.n‿ɛʁ/ |
| `…/task2_two_minute_prep_template.md:222` | M | *Y a-t-il* garbled IPA | /j‿a.t‿il/ |
| `…/task2_two_minute_prep_template.md:169, 228` | L | *concluant* = "convincing" (*Likely*) | "Tout cela me convient parfaitement" |
| `…/overcoming_hesitations_and_recovery.md:233/240` | L | Key cites English fillers that aren't in the transcript; "comment dit" | Fix the question or the transcript |
| `writing_speed/typing_french_under_exam_conditions.md:110` | M | CMS *é* key "right of l" (contradicts l.55) | On the "/" key |
| `…/typing_french_under_exam_conditions.md:150` | M | "Je suis sûr de la poser" = "I'm sure I put it" | "…de l'avoir posée" |
| `…/typing_french_under_exam_conditions.md:255, 272` | M | Answer key: wrong sentence number; *préférons* "grave"; *aigu* IPA | Acute accents; /ak.sɑ̃.t‿e.ɡy/ |
| `…/writing_task1_speed_drill.md:181` | L | "Élisisions" | "Élisions" |
| `…/writing_task2_speed_drill.md:6, 42–46` | M | "Equal-weight civic stance"; "examiner stops counting at 150" (*Likely*) | Present as a study tip only |

### Path 06 — B2+ Safety Margin (`curriculum/b2_safety/`)

| File:Line | Sev | Problem | Fix |
|---|---|---|---|
| `advanced_grammar/passe_simple_recognition.md:174` | M | "L'histoire commence qu'y arrive…" (ungrammatical, meaningless) | Delete |
| `…/passe_simple_recognition.md:164` | L | *sut* and *sur* called homophones | *su / sû* |
| `…/passe_simple_recognition.md:124` | L | -int called a "nasal diphthong" | Nasal vowel |
| `…/project_c1_argumentative_essay.md:115` | M | "automated decision-making (*décisions discrétionnaires*)" | *décisions automatisées* |
| `…/subjonctif_passe_concordance.md:111–113, 295` | M | *avant que / jusqu'à ce que* "demand" the subjonctif passé | They can take présent or passé |
| `…/subjonctif_passe_concordance.md:211` | M | Answer key breaks its own concordance rule (*Likely*) | "…à ce que le projet de loi soit voté" |
| `…/subjonctif_passe_concordance.md:228` | M | "Avant qu'il n'ait été trop tard" | "Avant qu'il ne soit trop tard" |
| `…/subjonctif_passe_concordance.md:235` | L | *à supposer que* called counterfactual | Hypothetical |
| `…/cultural_metaphors_and_idioms.md:45–47` | M | *tirer la sonnette d'alarme chez les économistes* (misused, *Likely*) | "…suscitant l'inquiétude des économistes, qui tirent la sonnette d'alarme" |
| `…/cultural_metaphors_and_idioms.md:141, 180` | L | *mordicus* in a high-register table; *faire la part des choses* called "transitive" | Familiar; used absolutely or with *entre… et* |
| `…/cultural_metaphors_and_idioms.md:273` | M | *brasser la cage* = "sow discord" (**Check**) | "shake things up" (fam., QC) |
| `spontaneous_debate/pronunciation_intonation_cadence.md:89–93, 243–252` | M | Syllable counts wrong throughout | Recount (e.g. 9, 5, 4, 10, 5, 12, 9) |
| `…/pronunciation_intonation_cadence.md:180, 206–208, 311` | L | *ont‿affirmé* called mandatory; *inacceptable* syllabification; schwa deletion in *développement* forbidden | Optional; fix; e-caduc deletion is native |
| `…/sophisticated_rhetorical_connectors.md:74, 111` | L | *qui plus est* [plys] as the rule; *récents accords* [t] liaison | [ply.z‿ɛ] / [plys]; [z] |
| `…/sophisticated_rhetorical_connectors.md:209/218` | M | Answer key blames *d'autant que* for a subjunctive that follows *tellement que* | Rewrite the drill |
| `…/counter_intuitive_prompt_defense.md:121` | L | *adoptée* transcribed as [adapte] | [adɔpte] |
| `…/project_c1_spoken_defense_challenge.md:147, 158` | L | *captées* has no antecedent; garbled IPA | Rephrase; use a real group from the transcript |

---

## Part 4 — Needs native-speaker or source confirmation

These were flagged **Check**. Confirm them before changing, or remove them if they can't be sourced:

- Québec usage: *brasser la cage* (meaning), *faire passer un sapin*, *bordée* (cm figure), *un brun* (coffee), *bâtisse* (register).
- Facts: RAMQ card colour; Québec law on "Canadian experience" requirements; the *tronc commun* metaphor; TV5Monde/FEI partnership claims; centre keyboard layouts; reading-section back-navigation on TCF-SO.
- The word-count convention: cite the current TCF Canada candidate guide explicitly once it's confirmed.

**Recommended:** after these fixes, have a native Québécois speaker review every **(QC)** item and every file in `b2_advanced/complex_audio_and_voices/` and `b1_independent/canadian_realities/`, and record the result in a separate "Native review" column in PROGRESS.md.
