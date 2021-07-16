"""
Author: Cody Edwards

Time of latest run of code/Test: 07/15/2021

Site Scraping data from: https://fie.org/athletes

Resources Used: Selenium documentation - https://selenium-python.readthedocs.io/api.html
                Python Data Science Handbook
                matplotlib documentation - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
                Pandas documentation - https://pandas.pydata.org/docs/reference/index.html
                Seaborn documentation - https://seaborn.pydata.org/api.html

Attributes scraped: Rank, points, name, country(abbreviated to three letters), Left or Right handed, age,
                    weapon, sex
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# checks if the xPath exists, Returns True if it exist and False if it doesn't
def xpathExists(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except NoSuchElementException:
        return False


# gets the basic info of a single fencer at specified xpath
# info includes rank, points, name, country (abbreviated to 3 letters), hand, age,
# weapon, and sex
# returns a dictionary of info
def getDetails(xpath, fencerWeapon, fencerGender):
    # Sample in xpath input
    # /html/body/section[2]/section/div/div/div/div/table/tr[2]
    # sample of what newXpath will look like
    # /html/body/section[2]/section/div/div/div/div/table/tr[2]/td[1]
    counter = 1
    newXpath = xpath + "/td[{}]".format(counter)
    if xpathExists(newXpath):
        rank = driver.find_element_by_xpath(newXpath).text
        counter += 1
        newXpath = xpath + "/td[{}]".format(counter)
        points = driver.find_element_by_xpath(newXpath).text
        counter += 1
        newXpath = xpath + "/td[{}]".format(counter)
        name = driver.find_element_by_xpath(newXpath).text
        counter += 1
        newXpath = xpath + "/td[{}]".format(counter)
        country = driver.find_element_by_xpath(newXpath).text
        counter += 1
        newXpath = xpath + "/td[{}]".format(counter)
        hand = driver.find_element_by_xpath(newXpath).text
        counter += 1
        newXpath = xpath + "/td[{}]".format(counter)
        age = driver.find_element_by_xpath(newXpath).text
        fencerDict = {
            "rank": rank,
            "points": points,
            "name": name,
            "country": country,
            "hand": hand,
            "age": age,
            "weapon": fencerWeapon,
            "gender": fencerGender
        }
        return fencerDict


# Gets all starting xpaths for getDetails from current table
# Returns list of xpath start of each line in table, or empty list if there is none
def getTableXpaths():
    tableList = []
    start = "/html/body/section[2]/section/div/div/div/div/table/tr[2]"
    if xpathExists(start):
        tableList.append(start)
        # Counter is 3 because it is next after /tr[2] and will keep counting up
        counter = 3
        nextTableLine = "/html/body/section[2]/section/div/div/div/div/table/tr[{}]".format(counter)
        # loops until there is no more lines in current table
        while xpathExists(nextTableLine):
            tableList.append(nextTableLine)
            counter += 1
            nextTableLine = "/html/body/section[2]/section/div/div/div/div/table/tr[{}]".format(counter)
    return tableList


# Gets the rank of last person on the table list of xpaths
def getLastRank(tableList):
    lastFencer = tableList[len(tableList) - 1] + "/td[1]"
    return driver.find_element_by_xpath(lastFencer).text


# Will get all fencers from current category on page
# Returns a list of dictionaries of the fencers
def getFencers(fencerWeapon, fencerGender):
    # Always the location of the next button
    nextButtonXpath = "/html/body/section[2]/section/div/div/div/div/div/ul/li[7]/a"
    # Always location of xpath for the rank of first fencer on list
    firstFencerRankXpath = "/html/body/section[2]/section/div/div/div/div/table/tr[2]/td[1]"
    # currentRank starts at 0 so loop can start
    currentRank = 0
    fencerList = []
    # Keep looping while the first fencer on list's rank is greater than the last fencer of previous page
    # Solves issue of knowing when last fencer is so not stuck in infinite loop of last page
    while int(driver.find_element_by_xpath(firstFencerRankXpath).text) > int(currentRank):
        tableFencer = getTableXpaths()
        for i in tableFencer:
            fencerList.append(getDetails(i, fencerWeapon, fencerGender))
        currentRank = getLastRank(tableFencer)
        # Clicks next button
        driver.find_element_by_xpath(nextButtonXpath).click()
        # Waits 1 second for responsible scraping
        time.sleep(1)
    return fencerList


# Gets all fencers from all categories
def getAllFencers():
    # All xpaths to buttons for each section to scrape
    epeeButtonXpath = "/html/body/section[1]/div/div/div[2]/form/div/div[2]/div[1]/div[1]/label[1]"
    foilButtonXpath = "/html/body/section[1]/div/div/div[2]/form/div/div[2]/div[1]/div[1]/label[2]"
    sabreButtonXpath = "/html/body/section[1]/div/div/div[2]/form/div/div[2]/div[1]/div[1]/label[3]"
    womenButtonXpath = "/html/body/section[1]/div/div/div[2]/form/div/div[2]/div[1]/div[4]/label[1]"
    menButtonXpath = "/html/body/section[1]/div/div/div[2]/form/div/div[2]/div[1]/div[4]/label[2]"

    # list of dictionaries of data of all fencers
    allFencersList = []

    # Scrapes every section
    # Print statement to show start of scraping
    print("Fencer scraping starting")

    # Epee women
    fencerWep = "epee"
    fencerGen = "female"
    # clicks needed buttons and waits for responsible scraping
    driver.find_element_by_xpath(epeeButtonXpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(womenButtonXpath).click()
    time.sleep(1)
    allFencersList.extend(getFencers(fencerWep, fencerGen))
    # Print statement to show completion of section
    print("Epee Women Scraped")

    # Epee men
    fencerWep = "epee"
    fencerGen = "male"
    # clicks needed buttons and waits for responsible scraping
    driver.find_element_by_xpath(epeeButtonXpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(menButtonXpath).click()
    time.sleep(1)
    allFencersList.extend(getFencers(fencerWep, fencerGen))
    # Print statement to show completion of section
    print("Epee Men Scraped")

    # Foil women
    fencerWep = "foil"
    fencerGen = "female"
    # clicks needed buttons and waits for responsible scraping
    driver.find_element_by_xpath(foilButtonXpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(womenButtonXpath).click()
    time.sleep(1)
    allFencersList.extend(getFencers(fencerWep, fencerGen))
    # Print statement to show completion of section
    print("Foil Women Scraped")

    # Foil men
    fencerWep = "foil"
    fencerGen = "male"
    # clicks needed buttons and waits for responsible scraping
    driver.find_element_by_xpath(foilButtonXpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(menButtonXpath).click()
    time.sleep(1)
    allFencersList.extend(getFencers(fencerWep, fencerGen))
    # Print statement to show completion of section
    print("Foil Men Scraped")

    # Sabre woman
    fencerWep = "sabre"
    fencerGen = "female"
    # clicks needed buttons and waits for responsible scraping
    driver.find_element_by_xpath(sabreButtonXpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(womenButtonXpath).click()
    time.sleep(1)
    allFencersList.extend(getFencers(fencerWep, fencerGen))
    # Print statement to show completion of section
    print("Sabre Women Scraped")

    # Sabre men
    fencerWep = "sabre"
    fencerGen = "male"
    # clicks needed buttons and waits for responsible scraping
    driver.find_element_by_xpath(sabreButtonXpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(menButtonXpath).click()
    time.sleep(1)
    allFencersList.extend(getFencers(fencerWep, fencerGen))
    # Print statement to show completion of section
    print("Sabre Men Scraped")

    # Print statement to show completion of scraping
    print("All Fencers Scraped")
    return allFencersList


# Opens webdriver and gets it ready to scrape
driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
# url for site to scrape from
url = "https://fie.org/athletes"
driver.get(url)
# wait for page to load
waitXPath = "/html/body/section[2]/section/div/div/div/div/table/tr[2]/td[1]"
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, waitXPath)))
# Puts fencers into list then converts list to dataframe
fencers = getAllFencers()
df = pd.DataFrame(fencers)
# Dataframe saved as fencer_data.csv
df.to_csv("fencer_data.csv")
# Driver no longer need so closes now
driver.close()
# For purposes of documentation report, the following code below will not be used
'''
# This line solves an type error later in code
df = pd.read_csv("fencer_data.csv")

plt.style.use("classic")
# Separating dataframe by weapon
epeeAll = df.loc[df["weapon"] == 'epee']
foilAll = df.loc[df["weapon"] == 'foil']
sabreAll = df.loc[df["weapon"] == 'sabre']

# New dataframe with all fencers with more than 1 point
epee = epeeAll.loc[epeeAll["points"] >= 1]
foil = foilAll.loc[foilAll["points"] >= 1]
sabre = sabreAll.loc[sabreAll["points"] >= 1]

# Assigning genders to colors for plots
colors = {'female' : 'red', 'male' : 'blue'}
# Plots
fig, ax = plt.subplots(1, 3)
# Epee
genderGroup = epee.groupby('gender')
for i, group in genderGroup:
    group.plot(ax=ax[0], kind='scatter', x='rank', y='points', label=i, color=colors[i])
ax[0].set_title("Epee")

# Foil
genderGroup = foil.groupby('gender')
for i, group in genderGroup:
    group.plot(ax=ax[1], kind='scatter', x='rank', y='points', label=i, color=colors[i])
ax[1].set_title("Foil")

# Sabre
genderGroup = sabre.groupby('gender')
for i, group in genderGroup:
    group.plot(ax=ax[2], kind='scatter', x='rank', y='points', label=i, color=colors[i])
ax[2].set_title("Sabre")

# Resizes figure be better readability
fig.set_size_inches(15, 5)
# Saves the figure as fencer_gender_plot.png
plt.savefig("fencer_gender_plot.png")


handColors = {'L' : 'yellow', 'R' : 'green'}
# Plots for points and rank by handedness
fig2, ax2 = plt.subplots(1, 3)
# Epee
handGroup = epee.groupby('hand')
for i, group in handGroup:
    group.plot(ax=ax2[0], kind='scatter', x='rank', y='points', label=i, color=handColors[i])
ax2[0].set_title("Epee")
# Foil
handGroup = foil.groupby('hand')
for i, group in handGroup:
    group.plot(ax=ax2[1], kind='scatter', x='rank', y='points', label=i, color=handColors[i])
ax2[1].set_title("Foil")
# Sabre
handGroup = sabre.groupby('hand')
for i, group in handGroup:
    group.plot(ax=ax2[2], kind='scatter', x='rank', y='points', label=i, color=handColors[i])
ax2[2].set_title("Sabre")

# Sets figure size
fig2.set_size_inches(15, 5)

# Saves figure
plt.savefig("fencer_hand_plot.png")

# In order to help with showing what I learned in the course, I decided to leave in the
# matplotlib plots and just add on the seaborn distribution plots in the end

# Seaborn plots

# Creates distribution plot for foils by gender and saves it
genderDistFoil = sns.displot(data=foil, x="points", hue="gender", kde=True).set(title="Foil Gender Distribution")
plt.savefig("Fencer_gender_dist_foil.png")
# Creates distribution plot for epees by gender and saves it
genderDistEpee = sns.displot(data=epee, x="points", hue="gender", kde=True).set(title="Epee Gender Distribution")
plt.savefig("Fencer_gender_dist_epee.png")
# Creates distribution plot for sabres by gender and saves it
genderDistSabre = sns.displot(data=sabre, x="points", hue="gender", kde=True).set(title="Sabre Gender Distribution")
plt.savefig("Fencer_gender_dist_sabre.png")

# Creates distribution plot for foils by hand and saves it
handDistFoil = sns.displot(data=foil, x="points", hue="hand", kde=True).set(title="Foil Hand Distribution")
plt.savefig("Fencer_hand_dist_foil.png")
# Creates distribution plot for epees by hand and saves it
handDistEpee = sns.displot(data=epee, x="points", hue="hand", kde=True).set(title="Epee Hand Distribution")
plt.savefig("Fencer_hand_dist_epee.png")
# Creates distribution plot for sabres by hand and saves it
handDistSabre = sns.displot(data=sabre, x="points", hue="hand", kde=True).set(title="Sabre Hand Distribution")
plt.savefig("Fencer_hand_dist_sabre.png")

# Shows plots
plt.show()

'''
