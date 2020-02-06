import urllib.request

data = urllib.request.urlopen("http://www.jd.com").read().decode("utf-8", "ignore")
print(len(data))