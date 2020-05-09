from bs4 import BeautifulSoup
import requests
import re
import webbrowser

def find_links(page_source):
	regex = re.compile(r'<a href="(.+?)" target')
	result = regex.findall(page_source)
	return result

res = requests.get('https://theuselessweb.site/')

links = find_links(res.text)
top_links = links[:5]

for link in top_links:
	webbrowser.open(link)



