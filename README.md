# FIE-Scraper


## Introduction
FIE-Scraper is a Web Scraper designed to scrape the data of all International Fencing Federation (FIE) athletes from https://fie.org/athletes and store that data into a .csv file

## Description of Equipment
### Requirements
* Python 3.8
* FIE-Scraper file 
  + Go to https://github.com/CMEdwards22/FIE-Scraper
  + Click Code > download ZIP
  + Extract FIE-Scraper-main.zip
 * Firefox version 60 or higher

## Directions
* Move into FIE-Scraper-main directory
* Run main.py
  + This will open a firefox browser. DO NOT CLOSE, TYPE IN, OR CLICK ON ANYTHING IN THIS BROWSER.
  + Wait until the program fully runs through all pages on the browser. This process will take around 10+ minutes
  + Once the program is finished running, the browser will automatically close.
* Once the program is finished running there will be a fencer_data.csv found inside the FIE-Scraper-main directory containing the rank, number of points, name, country the fencer is representing (abbreviated down to three letters), if the fencer is left or right handed, age, weapon, and gender of every individual senior fencer registered in the FIE for the current year.

## FAQs
### Can I move/delete the fencer_data.csv?
Yes, the fencer_data.csv file can be moved, deleted, or modified safely once the program is finished running.
### Can I run this program multiple times?
Yes, if there is currently a fencer_data.csv file in the directory then it will be overwritten with the new one but otherwise will create a new fencer_data.csv file.
### How do I run the main.py file?
You can run the main.py file using any python IDE or by moving into the FIE-Scraper-main directory and running the command ```python main.py ```

## Support
If in need of support then contact the developer at edwardscm6@appstate.edu
