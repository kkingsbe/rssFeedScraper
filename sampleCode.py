import urllib.request

opener = urllib.request.FancyURLopener({})
url = "http://stackoverflow.com/"
html = opener.open(url)
content = html.read()

f = open("html.html","w+").write(str(content))