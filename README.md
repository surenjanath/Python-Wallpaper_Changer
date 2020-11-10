# Python-Wallpaper_Changer
This program changes wallpaper.

I've coded this small python program in python using the selenium module. 

What it does : 
- Go to stocksnap.io
- Randomly gets a number of page to scroll down range(1,12)
- Get's the ID of the photo
- Run it against the photos that have already downloaded to avoid duplicates
- If ID found then it randomly chooses another number from a range of 0 , amount of  pictures found 
- Downloads the picture
- It then always checks to see if picture is found and if not it waits < this means it's downloading >
- After picture found, it sets it as wallpaper. :) 


Program used : Python , Cyberlink , chromium webdriver
Modules          : selenium , time, os, random and cytypes


I will assume python users will download this so 
there are two (2) codes you will need to change 
that is being your directory for chrome to download the file and the directory for the wallpaper to find the folder that the pictures are located in.
Also use "pip install selenium" if you don't have the selenium module.

PS : I'm new to python and took lot of googling to get it to work *wink



Link to youtube video : https://youtu.be/lLHOnyOKA2E
