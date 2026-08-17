# WWI Fabric Data Warehouse

A hands-on Microsoft Fabric data warehouse project, built while studying for the
**[DP-700: Implementing Data Engineering Solutions Using Microsoft Fabric](https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-700/)**
certification.

This project follows Microsoft's official **Wide World Importers (WWI)** end-to-end tutorial —
ingesting the WWI dimensional sample data into a Fabric Warehouse, transforming it with T-SQL and
notebooks, and surfacing it in a Power BI report — while mapping each step back to specific DP-700
exam objectives.

## Project goal

Build a working Fabric data warehouse end-to-end (ingest → transform → model → report) and use it
as a study log for DP-700, tracking which exam skills each stage of the build exercises.

## Scenario

Acting as a warehouse developer for the fictional wholesaler **Wide World Importers**, this project:

- Ingests WWI's dimensional sample data into a Fabric Warehouse via a pipeline
- Clones and transforms tables using T-SQL (stored procedures, time travel)
- Queries the warehouse from a Spark notebook and the visual query editor
- Runs cross-warehouse queries
- Builds a DirectLake semantic model and Power BI report on top

Reference: [Microsoft Learn — Data Warehouse Tutorial: Introduction](https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-introduction)

## Repo structure

> Update this section as content is added.

```
wwi_fabric_dw/
├── README.md
├── pipelines/          # Exported pipeline definitions (JSON)
├── sql/                # T-SQL scripts: table clones, stored procedures, queries
├── notebooks/           # PySpark notebooks used to analyze the warehouse
├── semantic-model/      # DirectLake semantic model / Power BI report artifacts
└── docs/                # Notes, screenshots, exam-mapping docs
```

## Prerequisites

- A Power BI account
- Microsoft Fabric enabled on your tenant, or a Fabric Trial capacity
- Git installed locally, plus a clone of this repo

## Progress tracker

| # | Step | Status | DP-700 skill area |
|---|------|--------|--------------------|
| 1 | Create a workspace | ⬜ | Configure Microsoft Fabric workspace settings |
| 2 | Create a warehouse | ⬜ | Choose an appropriate data store |
| 3 | Ingest data (pipeline) | ⬜ | Ingest data by using pipelines; full & incremental loads |
| 4 | Clone a table with T-SQL | ⬜ | Transform data by using SQL |
| 5 | Transform data with a stored procedure | ⬜ | Transform data by using SQL; group and aggregate data |
| 6 | Time travel with T-SQL | ⬜ | T-SQL warehouse features |
| 7 | Visual query editor | ⬜ | Choose between Dataflow Gen2, notebook, KQL, T-SQL |
| 8 | Analyze data in a notebook | ⬜ | Transform data by using PySpark |
| 9 | Cross-warehouse query | ⬜ | OneLake shortcuts / cross-item access |
| 10 | DirectLake semantic model + Power BI report | ⬜ | Monitor semantic model refresh |
| 11 | Report from OneLake catalog | ⬜ | Configure OneLake workspace settings |
| 12 | Clean up resources | ⬜ | Workspace lifecycle management |

*(⬜ not started · 🟨 in progress · ✅ done)*

## Notes

Fabric items (warehouses, pipelines, notebooks, semantic models) live in the Fabric service, not
in this repo. Where possible, this repo stores exported definitions (pipeline JSON, T-SQL scripts,
notebook `.ipynb` files) so the build is reproducible and reviewable outside the Fabric portal.

## References

- [DP-700 exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-700/)
- [Fabric Data Warehouse tutorial series](https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-introduction)
- [Wide World Importers sample database](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is)
