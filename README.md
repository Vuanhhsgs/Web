# My Geometry Website - Overview

Official website (GitHub Pages): https://vuanhhsgs.github.io/Web/  
Testing / experimental deployment (Render): https://art-of-euclidean-geometry.onrender.com

This is my personal-but-public Euclidean geometry website: a curated archive of Olympiad-style problems with diagrams, solutions, and interactive constructions. I built it to document my problem-solving journey and make advanced geometry more approachable for others.

---

## What’s inside

### 1) Selected Exercises — Competition / Exam Problems (dethi.html)
A curated set of competition-style problems with:
- difficulty labels
- a diagram image
- links to Try It Yourself + My Solution

Sources include team selection tests, DGO/DJGO sets, provincial/national exams, and IGO Advanced problems.

### 2) Selected Exercises — Vietnamese Euclidean Geometry Forum (group_hinhhocphang.html)
Problems credited to teachers and community contributors (often from the Vietnamese Euclidean Geometry community), with the same structure:
- difficulty
- statement
- diagram
- Try It Yourself + My Solution

### 3) Selected Exercises — AoPS Forum Problems I Solved (baitapAoPs.html)
Problems collected from AoPS threads (plus credited problem authors), again with:
- diagram
- Try It Yourself + My Solution

### 4) Technique problem sets (method-first learning)
Each technique page includes:
- a “Common Approach” explanation
- an illustrative example
- a practice list with diagrams and links

Current technique sets include:
- Inversion (nghich_dao.html)
- Ratio chasing (bien_doi_ti_le.html)
- Vectors (vector.html)

---

## What each problem page provides

Each problem is presented with:
- difficulty tag (from very easy to extremely hard)
- problem statement
- diagram image
- Try It Yourself: downloadable .gsp (Geometer’s Sketchpad) construction so users can explore the figure
- My Solution: LaTeX-style writeups (and a feedback layout on solution pages)

I also maintain manual metadata to support structured practice:
- configuration tags (objects/relationships that appear)
- method tags (lemmas/techniques used)
- difficulty tags (practice targeting)

---

## Search and practice workflow

The homepage includes a tag-based search overlay so users can filter problems by:
- configuration tags
- method tags
- difficulty

This supports targeted practice, for example: “altitudes + Ceva + hard”.

---

## Experimental direction: automated diagram generation from text

A long-term goal (and the reason for the testing deployment) is a “Generate Diagram” tool:
- user pastes a geometry problem statement
- the system outputs a structured representation and eventually a diagram (GeoGebra-style construction)

Why this is hard:
- nested language (“line through H parallel to the bisector of angle XLO” contains objects inside objects)
- constraints and equations define objects indirectly (“such that…”, distance/ratio conditions)
- intersections can be ambiguous unless you specify which point is intended

---

## Current progress and planned features

My website began as a curated Euclidean geometry archive (problems, diagrams, solutions, and interactive files). The next three upgrades are still the core plan: smart search, hint visualization, automated diagram generation. What has changed is how I approach them after getting stuck on the hardest step: turning natural language geometry into something a system can execute reliably.

### What I have built so far
- A curated repository of ~60 Olympiad-style Euclidean geometry problems with diagrams, solutions, and downloadable Geometer’s Sketchpad (.gsp) files for hands-on exploration
- A manually curated metadata system:
  - configuration tags (objects/configurations appearing in a problem)
  - method tags (techniques/lemmas used)
  - difficulty labels  
  This already supports targeted practice and basic filtering
- An initial NLP prototype:
  - fine-tuned a spaCy transformer-based extraction model to identify geometry-related entities from problem statements
  - used this extraction in an early prototype pipeline to explore “text to structure” and expose where the hard cases break

### Why the research papers mattered (the mental model I adopted)
I originally assumed “problem text → correct construction code” could be done in one shot. Prototyping showed why that fails: geometry language is nested, constraint-heavy, and many constructions are ambiguous unless you encode a selection rule.

Studying recent work (AlphaGeometry, autoformalization papers, and geometry DSL/diagram-generation work like GMBL) gave me a clearer mindset:
- In messy domains like geometry text, the hardest step is semantic parsing (natural language to structured meaning)
- LLMs are powerful here, but they should be treated as proposal generators, not truth
- Reliability comes from verification loops: schema/type checks, repair retries, multi-sampling, and downstream solvers/checkers
- Autoformalization uses formal systems as filters (only what parses/verifies counts), which can also produce verified training data
- Diagram-generation DSL work shows the value of a well-designed representation: you can compile constraints into a solver/optimization and use feasibility/non-degeneracy as a “diagram exists” check
- A key surprise: natural language to DSL is still difficult even in state-of-the-art systems and is often not fully included in public pipelines

This reframed my plan: the system needs structure and checking, not just better prompting.

---

## Planned features (and how I am building toward them)

### 1) Smart search (tags + geometry-aware indexing)
Goal: help users find problems by configuration and technique, even when wording differs.

Progress:
- manual tags already enable targeted practice
- entity extraction provides an additional geometry-aware signal for indexing

Next steps:
- use entity extraction to build a rough “configuration signature” for each problem (objects/relations mentioned)
- auto-suggest tags for new problems and support similarity search beyond exact tag matching
- longer-term: as structured representations improve, enable more semantic queries (for example, “orthocenter + parallel line + circumcircle”)

---

### 2) Hint visualization (step-by-step figures)
Goal: turn solutions into an interactive sequence of figure states so learners can see the construction and key relationships.

Progress:
- many problems already include a downloadable interactive figure (.gsp), which supports hands-on exploration

Next steps:
- represent solutions as a sequence of structured steps (construction steps and/or claim nodes)
- render each step by adding a new object or highlighting important objects/relations
- support highlighting multiple components at once for comparative reasoning
- export steps as SVG (web-native) and eventually GeoGebra-compatible formats

---

### 3) Automated diagram generation (text → executable construction)
Goal: paste a problem statement and get a reproducible interactive diagram.

Progress:
- built early prototypes that map extracted structure into preliminary constructions (useful for simple cases)
- identified failure modes that matter most:
  - nested entities
  - constraint-defined objects (“such that…”, ratios/distances)
  - ambiguous constructions (choosing the intended intersection point)

Next steps:
- design a small DSL-like intermediate representation for geometry:
  - explicit objects, relations, constraints, and selectors for ambiguity
- use models/LLMs to generate multiple candidate structured parses
- apply deterministic validation:
  - schema/type checks, symbol consistency, dependency ordering
  - repair/retry loops when candidates fail
- compile only verified structures into construction steps (GeoGebra-style commands / SVG)
- longer-term: add a feasibility / anti-degeneracy check (solver-style), inspired by numeric diagram-generation research

---

## Status
This is still early and imperfect. My current focus is learning from these papers and translating their ideas into a more plausible design, because the hard part is exactly where research is still evolving: reliable natural language to structured geometry.

---

## Credits and attribution
This site is built from problems and ideas influenced by:
- teachers and friends who helped discuss solutions
- community sources (Vietnamese Euclidean Geometry groups, AoPS)
- national, regional, and international Olympiad-style contests

Whenever possible, I credit problem sources and authors on the pages themselves.

---

## Notes
- The GitHub Pages site is the stable public version.
- The Render deployment is where I test features that may require server-side logic.

If you find errors, broken links, or want to suggest problems/technique sets, feel free to open an issue or message me.
