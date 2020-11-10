# Python-Wallpaper_Changer
This program changes wallpaper.

I've coded this small python program in python using the selenium module. 
What it does : 
- Go to stocksnap.io
- Randomly gets a number of page to scroll down range(1,12)
- Get's the ID of the photo
- Run it again the photos that have already downloaded to avoid duplicates
- If ID found then it randomly chooses another number from a range of 0 , amount of    pictures found 
- Downloads the picture
- It always checks to see if picture is found and if not it waits 
- After picture found, it sets it as wallpaper. :) 


Program used : Python , Cyberlink , chromium webdriver
Modules          : selenium , time, os, random and cytypes


PS : I'm new to python and took lot of googling to get it to work *wink
