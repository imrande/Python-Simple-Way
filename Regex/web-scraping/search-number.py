# find the phone number from redbus.in website

import re
import urllib.request

openUrl = urllib.request.urlopen(
    "https://www.redbus.in/info/contactus")
readUrl = str(openUrl.read())

phoneNumbers = re.findall(
    r'[+]91[6-9]\d{9}', readUrl)

print(phoneNumbers)
