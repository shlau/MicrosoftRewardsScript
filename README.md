# MicrosoftRewardsScript
1) Download Python

2) Download the chromedriver that corresponds with your version of chrome https://chromedriver.chromium.org/ and place the driver in a folder with the SearchScript.py.
   Alternatively, run the RunDriverUpdate.bat script which will download the latest stable chromedriver.

3) Edit SearchScript.py and replace $CHROME_DRIVER_PATH, $USERNAME, $PASSWORD 

4) Run the script in command prompt with python (i.e. python SearchScript.py). 
   If you would like to double click a file instead of running the script in the command prompt, you can create a batch file using the location of your python.exe and
   SearchScript.py. You can type "where python" in command prompt to get the python.exe location.

   I created a batch file called search.bat, it contains the line: 
   C:\Users\myname\AppData\Local\Programs\Python\Python38-32\python.exe "C:\Users\myname\Documents\MSFTRewards\SearchScript.py"
