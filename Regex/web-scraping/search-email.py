# find the phone number from Nusaiba template website

import re
import urllib.request

openurl = urllib.request.urlopen(
    "https://rapidthemes.net/nusaiba/index-2.html")
readUrl = openurl.read()

phoneNumbers = re.findall(r'[a-z\._]+@[a-z]+[.][a-z]{3}', str(readUrl))
for num in phoneNumbers:
    print(num)
