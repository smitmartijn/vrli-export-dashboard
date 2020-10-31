# Scraping a vRealize Log Insight Dashboard
#   vRLI doesn't support exporting dashboards and I wanted a weekly report, so this script uses browser control via Selenium
#   to create a screenshot of a dashboard page. It also saves the page HTML into a variable, so you can parse that and grab
#   interesting data from it.
#
# Martijn Smit <@smitmartijn>
# 2020-10-31

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from datetime import date
from datetime import timedelta

# Configure here

# vRLI hostname & credentials
vRLI_HOST = "vrli.lab.corp"
vRLI_USER = "my-user"
vRLI_PASS = "my-password"

# https://vrli.lab.corp/home?contextId=shared&viewId=2
#                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vRLI_DASHBOARD_PAGE = "home?contextId=shared&viewId=2"

# This adds the start and end time on the data to get. This does the last 7 days (using timedelta below)
fromTimeDate = (date.today() - timedelta(days=7)).strftime("%d/%m/%Y")
fromTimeTS = int(time.mktime(datetime.datetime.strptime(fromTimeDate, "%d/%m/%Y").timetuple()) * 1000)
vRLI_DASHBOARD_PAGE = vRLI_DASHBOARD_PAGE + "&customStartMillis=%d&customEndMillis=%d" % (fromTimeTS, int(round(time.time() * 1000)))

# Stop configuring here

opts = Options()
opts.set_headless() # Comment this, if you want to see the browser in action

browser = Firefox(options=opts)
browser.set_window_size(1920, 1200) # You could change this to different dimensions, to get a different screenshot size

print("Logging into vRLI!")
browser.get("https://%s/login" % vRLI_HOST)
browser.find_element_by_id('auth-login').send_keys(vRLI_USER)
time.sleep(1)
browser.find_element_by_id('auth-password').send_keys(vRLI_PASS)
time.sleep(2)
browser.find_element_by_id('login-button').click()

WebDriverWait(browser, 30).until(EC.title_contains("vRealize Log Insight"))
print("Heading to dashboard..")

browser.get("https://%s/%s" % (vRLI_HOST, vRLI_DASHBOARD_PAGE))

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'add-widget-info')))

# Wait 10 seconds for the dashboard to load
time.sleep(10)

print("Taking screenshot!")
root = browser.find_element_by_id('home-content') # This is the main content div in vRLI. Using this skips the menu and navigation
root.screenshot('vrli-dashboard.png')

# Save HTML
html_content = browser.page_source

# Browser is not needed anymore
browser.quit()

print("You now have 2 options: use the vrli-dashboard.png file and send it somewhere, or parse the HTML in the html_content variable to pull out data that you want to process.")



