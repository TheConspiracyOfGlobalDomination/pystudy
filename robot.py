import urllib.request

req = urllib.request.Request("http://www.okex.com/api/system/v3/status", headers={"User-Agent":"Magic Browser"})
con = urllib.request.urlopen(req)
print(con.read())
