import urllib.request,json
from pprint import pprint

def startWebRequest (url):
    opener = urllib.request.FancyURLopener({})
    url = link
    html = opener.open(url)
    content = str(html.read())
    return content

def getURLs (content):
    links = []
    content = content.split("<link>")[3:]
    for x in content:
        links.append(x.split("</link>")[0])
    pprint(links)
    return links

def scrapeWebPage (link):
    html = startWebRequest(link)


with open("settings.json") as f:
    settings = json.load(f)

opener = urllib.request.FancyURLopener({})
url = settings["RSS Feed Location"]
print("RSS Feed URL: " + url)
html = opener.open(url)
content = str(html.read())

links = getURLs(content)
for link in links:
    scrapeWebPage(link)