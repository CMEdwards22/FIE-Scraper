# FIE-Scraper


## Introduction
FIE-Scraper is a Web Scraper designed to scrape the data of all International Fencing Federation (FIE) athletes from https://fie.org/athletes and store that data into a .csv file

## Description of Equipment
### Requirements
* Python 3.8
* Firefox version 60 or higher
* FIE-Scraper file 
  + Go to https://github.com/CMEdwards22/FIE-Scraper
  + Click Code > download ZIP
   ![downloadImage](https://user-images.githubusercontent.com/69873090/125885155-3006eb00-3413-46cf-a557-a9031765f018.png)
  + Extract FIE-Scraper-main.zip
* An IDE to run a .py file
  + PyCharm Community edition or PyCharm Professional editon are the recommeded IDEs for this program however any IDE will work
  + You can download PyCharm [here](https://www.jetbrains.com/pycharm/download/#section=windows)
  + Alternatively if you are using a linux system, you can run the program by navigating to the FIE-Scraper directory and running the command ```python3 main.py ```

## Directions
* Move into FIE-Scraper-main directory
  + If you are using PyCharm, click Open then select the FIE-Scraper-main folder
  + To run, right click on main.py > Run 'main'
  + ![runMainExampleSelected](https://user-images.githubusercontent.com/69873090/126588277-b01ab5c6-ee3a-4dd8-a18c-bf865b002ac6.png)
* Run main.py
  + This will open a firefox browser That should look similar to the one below. DO NOT CLOSE, TYPE IN, OR CLICK ON ANYTHING IN THIS BROWSER.
  ![BrowserExample](https://user-images.githubusercontent.com/69873090/125885824-7fdb3bb2-da2d-4817-9100-3fb8492dd85c.png)
  + Wait until the program fully runs through all pages on the browser. This process will take around 10+ minutes
  + Once the program is finished running, the browser will automatically close.
* Once the program is finished running there will be a fencer_data.csv found inside the FIE-Scraper-main directory containing the rank, number of points, name, country the fencer is representing (abbreviated down to three letters), if the fencer is left or right handed, age, weapon, and gender of every individual senior fencer registered in the FIE for the current year.

## FAQs
### Can I move/delete the fencer_data.csv?
Yes, the fencer_data.csv file can be moved, deleted, or modified safely once the program is finished running.
### Can I run this program multiple times?
Yes, if there is currently a fencer_data.csv file in the directory then it will be overwritten with the new one but otherwise will create a new fencer_data.csv file.

## Support
If you need support then contact the developer at edwardscm6@appstate.edu
