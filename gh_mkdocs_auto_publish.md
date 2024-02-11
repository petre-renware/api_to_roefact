
# *Build & Publishing* mkdocs site with GitHub Actions

<small>*Reference:* `https://squidfunk.github.io/mkdocs-material/publishing-your-site/#with-github-actions`</small>



Using GitHub Actions you can automate the deployment of your project documentation. At the root of your repository, create a new GitHub Actions workflow, e.g. .github/workflows/ci.yml, and copy and paste the following contents:

```
name: ci 
on:
  push:
    branches:  #NOTE see note 1
      - master 
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material  #NOTE see note 3
      - run: mkdocs gh-deploy --force  #NOTE see note 2
```



## Notes

* **1.** at *branches section* change to branch that you consider is the one when push, the site to be built and published

* **2.** in order to `mkdocs gh-deploy` command to work, *ensure that the publishing source branch* for your GitHub Page **is set to `gh-pages`**. This branch need to be created if not exists. Actual (@240210) solutions use `publishing` branch.

* **3.** install your stable environment used when build locally (on your computer)



