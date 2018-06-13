import urllib.request,json,smtplib
from pprint import pprint
from newspaper import Article
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    article = Article(link)
    article.download()
    article.parse()
    content = article.text
    authors = article.authors
    date = article.publish_date
    keywords = article.keywords
    #pprint(article.text)
    return {"Authors" : authors, "Date" : date, "Content" : content, "Keywords" : keywords}

def sendEmail ():
    msg = MIMEMultipart()
    msg['From'] = "rssfeedscraper@gmail.com"
    msg['To'] = "kkingsbe@gmail.com"
    password = "@Z0t6PbWZZKx"
    msg['Subject'] = "RSS Feed Scraper Successfully Run"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail("RSS Feed Scraper", msg['To'], msg.as_string())
    server.quit()

with open("settings.json") as f:
    settings = json.load(f)

opener = urllib.request.FancyURLopener({})
url = settings["RSS Feed Location"]
print("RSS Feed URL: " + url)
html = opener.open(url)
content = str(html.read())

links = getURLs(content)

for link in links:
    articleInfo = scrapeWebPage(link)
    f = open("Articles.txt", "a+")

    authorString = ""

    for author in articleInfo["Authors"]:
        authorString += author + ", "

    authorString = authorString[:-1]
    content = articleInfo["Content"].replace('\n', ' ').replace('\r', '')
    f.write(authorString + ";" + str(articleInfo["Date"]) + ";" + content + ";" + ' '.join(str(word) for word in articleInfo["Keywords"]))
    f.write("\n")
    f.close()

sendEmail()