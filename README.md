<!-- dhriman / github profile -->

<picture>
  <source media="(max-width: 650px)" srcset="./assets/field-hero-mobile.svg">
  <img src="./assets/field-hero.svg" alt="Dhriman Deka: ML engineer. Live stats for merged upstream PRs, resolved PR rate, median merge time and open PRs." width="100%">
</picture>

hi, i’m dhriman.

i studied economics at IISER Bhopal and ended up working on machine learning systems. lately i’ve spent a lot of time in other people’s repositories. i like finding out why something broke, fixing it, and seeing whether the fix survives review.

**what i work on:** machine learning systems, LLM tooling, vector search, and retrieval pipelines. i’m open to ML engineering and retrieval infrastructure roles. you can [start a conversation here](https://github.com/astroknot-sheep/astroknot-sheep/discussions).

and yes, the sheep in [@astroknot-sheep](https://github.com/astroknot-sheep) was deliberate. 🐑

---

## some fixes that made it upstream

these are the kind of contributions i enjoy: specific bugs, readable changes, and a review thread where someone makes the code better.

- **[MLflow](https://github.com/mlflow/mlflow/pull/27018)** — Gemini safety blocks weren’t being reported as content-filter events. fixed how the gateway handles them.
- **[Qdrant Client](https://github.com/qdrant/qdrant-client/pull/1617)** — the default tokenizer for a gRPC text index wasn’t matching the expected `word` default.
- **[Haystack](https://github.com/deepset-ai/haystack/pull/13437)** — corrected line ranges when `PythonCodeSplitter` makes secondary splits.
- **[Logfire](https://github.com/pydantic/logfire/pull/2785)** — closing a generator early shouldn’t look like an application error.
- **[Docling](https://github.com/docling-project/docling/pull/5309)** — fixed document conversion when a table comes immediately after a list.
- **[Haystack Core Integrations](https://github.com/deepset-ai/haystack-core-integrations/pull/4149)** — corrected numeric metadata filters in the pgvector integration.
- **[Sentence Transformers](https://github.com/huggingface/sentence-transformers/pull/4246)** — fixed a broken training-arguments import in the examples.

there are more. the code and reviews are linked, so you don’t have to take my word for any of it.

## things i’m making

**[KONARQ_MATRI](https://github.com/astroknot-sheep/KONARQ_MATRI)**  
a mental-health support project. i’m thinking about privacy, referrals, and where software should step aside for a human.

**[finance_transformer](https://github.com/astroknot-sheep/finance_transformer)**  
trying transformer models on financial time series. mostly a lesson in how convincing noise can look.

**[DQN for Ludo](https://github.com/astroknot-sheep/Reinforcement_Learning_DQN_for_Ludo)**  
double DQN, prioritized experience replay, and a game that makes the experiments less abstract.

<details>
<summary>older experiments and side projects</summary>

- [TWS_WriterAgent](https://github.com/astroknot-sheep/TWS_WriterAgent) — experimenting with agents.
- [ML_project_final](https://github.com/astroknot-sheep/ML_project_final) — an earlier machine learning project.
- [mlproject](https://github.com/astroknot-sheep/mlproject) — an old sandbox.
- [data-gravity-portfolio](https://github.com/astroknot-sheep/data-gravity-portfolio) — another work in progress.

</details>

---

## the PR record

a running count of **upstream merges since september 2026**, not a year of mostly empty bars.

<img src="./assets/field-pulse.svg" alt="Cumulative count of merged upstream PRs since September 2026" width="100%">

<details>
<summary><strong>where the PRs went — top six upstream repositories</strong></summary>

<img src="./assets/field-atlas.svg" alt="Top six repositories by opened PR count, out of all upstream repositories" width="100%">

</details>

<sub>all numbers come from public GitHub PRs to repositories i don’t own. the hero shows the percentage of **resolved** PRs that merged; PRs still under review aren’t counted as failures. statistics and the tables below are updated daily by GitHub Actions.</sub>

### merged upstream

actual merge timestamps are in UTC. the last column is how long each PR spent between opening and merging.

<!-- MERGED_HISTORY_START -->
_the merged-PR record is updated by the dashboard workflow._
<!-- MERGED_HISTORY_END -->

### in review

open upstream PRs only. closed and merged PRs are deliberately excluded from this list.

<!-- LIVE_PRS_START -->
_the open-PR record is updated by the dashboard workflow._
<!-- LIVE_PRS_END -->

[all authored PRs](https://github.com/pulls?q=is%3Apr+author%3Aastroknot-sheep) · [merged upstream](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aastroknot-sheep) · [open PRs](https://github.com/pulls?q=is%3Apr+is%3Aopen+author%3Aastroknot-sheep)

---

## technologies i’ve worked with

**Python · PyTorch · LLM gateways · retrieval / vector search · Qdrant · MLflow · pgvector / PostgreSQL · FastAPI · Docker · Git**

i’ve worked on some of these in projects and sent patches to others. links to the actual changes are above.

## say hello

working on something in ML systems or retrieval, or want to talk about a PR? [start a discussion](https://github.com/astroknot-sheep/astroknot-sheep/discussions).

<sub>the graphics are generated in this repository with Python and GitHub Actions. [source code](./scripts/generate_pr_dashboard.py).</sub>
