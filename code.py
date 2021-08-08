from bs4 import BeautifulSoup
import time 
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("/Users/balua/Desktop/ChromeDriver")

browser.get(START_URL)

time.sleep(10)


def scrape():
    headers = ["Name","Distance","Mass","Radius"]

    stars_data = []


    for i in range(0,97):
        soup = BeautifulSoup(browser.page_source, "html.parser")

            temp_list = []

    with open("scarpe_2.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()
    

