$Response = Invoke-WebRequest https://chromedriver.storage.googleapis.com/LATEST_RELEASE 
Invoke-WebRequest "https://chromedriver.storage.googleapis.com/$Response/chromedriver_win32.zip" -o latestdriver.zip
tar -xf latestdriver.zip
rm latestdriver.zip