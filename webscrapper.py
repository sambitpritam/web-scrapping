"""
Web scrapper to scrape for available header content in the wikipedia page
"""

import requests as res
import bs4

res = res.get('https://en.wikipedia.org/wiki/Web_scraping')
print('request type is : %s' % type(res))

# converting the response to beautiful Soup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# now fetching the title
title = soup.select('title')
print('The Title of the page is: %s' % title)

# Now fetching all the header in the page: <span class="mw-headline" id="Techniques">Techniques</span>
headers = soup.select('span.mw-headline')
for eachElem in headers:
    print('Printing Element: %s' % eachElem.getText())