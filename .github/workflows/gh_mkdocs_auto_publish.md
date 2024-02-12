
# *Build & Publishing* mkdocs site with GitHub Actions

<small>*Reference:* `https://squidfunk.github.io/mkdocs-material/publishing-your-site/#with-github-actions`</small>



Using GitHub Actions you can automate the deployment of your project documentation. At the root of your repository, create a new GitHub Actions workflow, e.g. .github/workflows/ci.yml.


>...for *original* content see `ci.yml.txt` in this directory...






## Notes

* **2.** in order to `mkdocs gh-deploy` command to work, *ensure that the publishing source branch* for your GitHub Page **is set to `gh-pages`**. This branch need to be created if not exists. Actual (@240210) solutions use `publishing` branch.

* **3.** install your stable environment used when build locally (on your computer)



