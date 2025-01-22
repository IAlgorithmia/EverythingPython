from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

response = requests.get('https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/')
html_text = response.text
soup = BeautifulSoup(html_text, 'lxml')
article_title = soup.find('title').text[:-23]
article_text = soup.find('div', class_='td-post-content tagdiv-type')
if not (article_text) : 
    article_text = soup.find_all('div', class_='tdb-block-inner td-fix-index')[14]
last_paragraph = article_text.find('pre')
if (last_paragraph):
    last_paragraph.extract()
article_text = "\n\n".join(stripped_string for stripped_string in article_text.stripped_strings)
print(article_text)