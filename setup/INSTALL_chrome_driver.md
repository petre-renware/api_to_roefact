# Setup Chrome Driver on WSL



## Installing ChromeDriver

Find the URL of the ChromeDriver version that matches your Chrome version on the ChromeDriver website. It should be a zip file; in my case it’s

`wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip`

Download, unzip, and put it in your bin directory:

```
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip
unzip chrome-linux64.zip
cd  chrome-linux64/
sudo cp chrome /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

Double check it worked:

`chromedriver --version`

If was previously installed drivers, check version

`which chromedriver`












