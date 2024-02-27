
# Useful TODOs 

[TOC]

## RELEASE QA checklist

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


Optional if possible do:

* [ ] extract version items in a dedicated file in `changelog_history/`. The pattern for name is `CHANGELOG-<version>.md`
* [ ] in main CHANGELOG refer thet file (archives section) and clean it from not achieved entries
* [ ] archive locally (in `880-RLSE/.../` directory) all resulted deliverable








## How to Install `xl2roefact` as local in project package

In master project root (ie, not `xl2roefact/` directory, but main project directory) execute `pip install -e xl2roefact`. Now package is installed and all its modules are available.





