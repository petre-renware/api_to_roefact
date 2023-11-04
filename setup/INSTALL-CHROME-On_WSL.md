# Install Google Chrome on WSL



## Download and install Chrome:

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb

rm ./google-chrome-stable_current_amd64.deb
```



## Check that it’s installed ok:

```
google-chrome --version
```

Running is done with `google-chrome` command. All X-Windows graphical elements should be installed (normally if WSL is up to date, these are already installed)


