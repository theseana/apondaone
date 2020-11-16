import urllib.request
import re


contents = urllib.request.urlopen("https://www.nytimes.com/").read()
re.findall("^a.+", "askjdbjafbjhfbjlasdfbjasdfbjlasdfbjaf")
print(contents)