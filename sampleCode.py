import urllib.request

opener = urllib.request.FancyURLopener({})
url = "https://www.cnn.com/2018/06/09/politics/trump-north-korea-g7/index.html"
html = opener.open(url)
content = str(html.read())

tagsList = content.split("<")[1:]
titlesList = []
content = ""

for tag in tagsList:
    try:
        if tag.startswith("title"):
            titlesList.append(tag.split(">")[1])
        elif not tag.startswith("/"):
            content += tag.split(">")[1]
    except (Exception):
        pass

print(content)
print(titlesList)
#f = open("html.html","w+").write(content)