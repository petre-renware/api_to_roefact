
# Automation tools

## Build site

Merge branch which contains `mkdocs` site to build into branch **`build-site`**.
The site will be built according to `mkdocs.yml` specs.


## Build xl2roefact CLI app, library packages and DLD doc

Merge to branch **`build-xl2roefact`**. The building process will execute `pdm run build_all` command.
Get back results by merging `build-xl2roefact` branch back to your initial branch.


