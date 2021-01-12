import urllib.request
contents = urllib.request.urlopen("http://www.okex.com/api/system/v3/status").read()
print(contents)