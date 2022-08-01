# Cuke4Data
## Gherkin (cucumber) language for data

![](https://github.com/igponce/cuke4data/workflows/Tests/badge.svg)


This project contains PoC for using the gherkin language as a cucumber-like
way to do data manipulation (not just software testing like cucumber does).

Possible use cases:

- ETL (triggered by something else)
- Master Data Management (for rule definition in plain english)
- Data Quality

# Testing

Test are in the 'test' directory. To run 'em just do:
```{bash}
poetry run pytest
```

# Roadmap

- Implement simple Gherkin language parser
- Parse Gherkin on a data stream
- Make runnable code... (maybe from Spark / Spark Streaming / Etc ...)

