
# Scraping a vRealize Log Insight Dashboard

Export vRealize Log Insight Dashboards with Python.

## Installation

pip install -r requirements.txt

Install the Mozilla Geckodriver and make sure it's in your PATH: https://github.com/mozilla/geckodriver/releases

## Configuration

Change the follow variables to your vRealize Log Insight details:

* vRLI_HOST = "vrli.lab.corp"
* vRLI_USER = "my-user"
* vRLI_PASS = "my-password"
* vRLI_DASHBOARD_PAGE = "home?contextId=shared&viewId=2"

The last variable points to the page in vRLI that you want to export. Copy and paste that from your browser when you're looking at the dashboard.

Lastly, by default the script takes the last weeks worth of data. If you want to change that time window, change this line:

`fromTimeDate = (date.today() - timedelta(days=7)).strftime("%d/%m/%Y")`

## Run!

```
➜  vrli-export-dashboard git:(main) ✗ python vrli-export-dashboard.py
Logging into vRLI!
Heading to dashboard..
Taking screenshot!
You now have 2 options: use the vrli-dashboard.png file and send it somewhere, or parse the HTML in the html_content variable to pull out data that you want to process.
```