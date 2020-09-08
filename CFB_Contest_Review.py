import os
import time
import pandas as pd
from time import sleep
from selenium import webdriver
from config import DK_USERNAME, DK_PASSWORD

# Opening Chrome and Going to DK
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": os.getcwd()}
chromeOptions.add_expermental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("http://www.draftkings.com")

# Sign In
sign_in = driver.find_element_by_link_text("SIGN IN")
sign_in.click()

driver.find_element_by_name('username').send_keys(DK_USERNAME)
driver.find_element_by_name('username').send_keys("\t"+DK_PASSWORD)
driver.find_element_by_xpath("//*[contains(text(), 'LOG IN')]")[0].click()

# Open live CFB contests
driver.get("https://www.draftkings/lobby#/CFB")
driver.find_elements_by_xpath("//*[contains(text(), 'View Live Contests')]").[0].click()
prize_pool = driver.find_elements_by_css_selector("div.ui-state-default.slick-header-column.grid-text-with-icon")[2]
prize_pool.click()
prize_pool.click()

# Extract contest ids and information
rows = []
for row in table.find("div", "grid-canvas").find_all("div", "slick-row"):
    row_data = {}
    for cell in row.find_all("div"):
        if cell.find("a"):
            a = cell.find("a")
            if a.get("data-tracking"):
                row_data[a.get("data-tracking")]=cell.text
            if cell.text == "Watch":
                row_data['link'] = a.get("href")
    rows.append(row_data)
live_contests = pd.dataFrame(rows)

# Download contest data
def get_lineups(link):
    sleep(4)
    BASE_URL = "https://www.draftkings.com"
    driver.get(BASE_URL+link)
    driver.find_element_by_id("export-lineups-csv").click()
get_lineups("/contest/gamecenter/90798684")

contests['link'].apply(get_lineups)
