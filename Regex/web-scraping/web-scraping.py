# process of collecting data from web page called web scraping

# web scraping with regex
import urllib.request
import re

websites = ['https://google.com', 'https://yahoo.com']

for website in websites:
    print('Searching...', website)

    open_url = urllib.request.urlopen(website)
    readUrl = open_url.read()  # by default it bytes class
    webTitle = re.findall('<title>.*</title>', str(readUrl), re.IGNORECASE)
    print(webTitle[0])

