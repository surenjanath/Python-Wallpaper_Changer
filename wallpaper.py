import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import os
import ctypes




def setting_Wallpaper(location):
    SPI_WALLPAPER = 20
    SPIF_UPDATINGFILE = 3
    ctypes.windll.user32.SystemParametersInfoW(SPI_WALLPAPER, 0,location, SPIF_UPDATINGFILE)
    
def main():
    
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {

        #Change DOWNLOAD DIRECTION HERE :  
      "download.default_directory": r"C:\Users\Surenjanath\Desktop\Project CovID -19\Wallpaper Changer\Pictures",
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
    })
    chrome_options.headless = True
    chrome_options.add_argument('window-size=1920x1080')
    chromedriver_path = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(executable_path = chromedriver_path, options = chrome_options)

    print("-------------------------------")
    print("\t  Wallpaper")
    print("-------------------------------")

    print('\n\n Loading Website')
    
    url = "https://stocksnap.io/search/"
    search = 'landscape'
    driver.get('https://stocksnap.io/view-photos/sort/trending/desc')
    time.sleep(3)

    print(" \n Loading More Pictures ",end ="",flush=True)
    for i in range(1,random.randint(1, 8)):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        print('.', end="",flush=True)
        time.sleep(1)
    print('\n')    
            
    photos_1 = driver.find_elements_by_class_name('photo-grid-item')

    val = random.randint(0, len(photos_1))
    print(' Picture Number  : '+str(val)+'\n')
    time.sleep(1)
    print(' Amount of Pictures Found : '+str(len(photos_1))+'\n')


#-------------------------------------------------------------------
    # Check if File Exist
    Filename = 'StockSnap_'
    Downloaded = False

    #Get picture ID

    while True:
        
        ID = photos_1[val].find_element_by_class_name('favo ').get_attribute('data-imgid')
    
        if os.path.exists('./Pictures/'  +  Filename  +  ID  +'.jpg'):
            
            val = random.randint(0, len(photos_1))
            print(' New Picture ID : '+str(val)+'\n')
            
        else:
            print(' All Good. No DUPLICATES')
            break





    #Getting Link
    pic = photos_1[val].find_element_by_tag_name('a').get_attribute('href')
    driver.get(pic)
    


    
    #clicking Download
    driver.find_element_by_class_name('btn.download-btn').click()
    

    
    print('\n Downloading Picture. ')
    print('\n Please Wait ',end="",flush=True)
    time.sleep(5)
    while Downloaded==False:
        if os.path.exists('./Pictures/'  +  Filename  +  ID  +'.jpg'):
            time.sleep(2)
            print('\n\n File Downloaded \n')
            Downloaded = True
            time.sleep(2)
            driver.close()
            break
                
        else:
            print('.',end="",flush=True)
            time.sleep(4)
    time.sleep(1)
    print("-------------------------------")
    print( ' Setting Wallpaper')
    print("-------------------------------")
    #Change TO DOWNLOAD FOLDER FROM ABOVE HERE :  
    setting_Wallpaper("C:\\Users\\Surenjanath\\Desktop\\Project CovID -19\\Wallpaper Changer\\Pictures\\"+  Filename  +  ID  +'.jpg')
    time.sleep(3)
    print('\n DONE !')
    print("-------------------------------")
    

main()
