
# Useful TODOs 

[TOC]

## RELEASE QA checklist

Before to publuc release a version check and do the following:

* [ ] full chk / review for FIXME & run `pdm build_all`
* [ ] change release name from ".dev" to final one (change all occurrences)
* [ ] build all: app, documentations, site
* [ ] clean if necessary the `.../dist/` directory

Optional if possible do:

* extract version items in a dedicated file in `changelog_history/`. The pattern for name is `CHANGELOG-<version>.md`
* archive locally (in `880-RLSE/.../` directory) all resulted deliverable








## How to Install `xl2roefact` as local in project package

In master project root (ie, not `xl2roefact/` directory, but main project directory) execute `pip install -e xl2roefact`. Now package is installed and all its modules are available.





