# Release QA activities checklist

[TOC]

## Mandatory QA checklist

Before to publuc release a version check and do the following:

* [ ] full chk / review for FIXME & TODOs
* [ ] change release name from ".dev" to final one (change all occurrences)
* [ ] update version string files ref:
    * **xl2roefact** `.../xl2roefact/__version__.py`
    * **INVOICEtoROefact** `/__version__`
    * ...not yet rdy, future web2roefact...
    * **site** `/mkdocs.yml` section `extra`
* [ ] build all: app, documentations, site (git branch `build-xl2roefact` or run `pdm build_all`)
* [ ] publish xl2roefact on PyPi (git branch `pypi-publish`)
* [ ] build site (git branch `build-site`)
* [ ] publish site (git branch `publishing`)
* [ ] clean if necessary the `.../dist/` directory



## Optional (if possible) checklist:

* [ ] archive CHANGELOG old releases in `changelog_history/` (pattern for file name is `CHANGELOG-<version>.md`)
* [ ] archive locally (in `880-RLSE/.../` directory) all resulted deliverable





