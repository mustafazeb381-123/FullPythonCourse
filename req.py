import requests
r = requests.get("http://www.facebook.com")
print(r.text)
url = "www.anything.com"
data = {
    "p1=4,"
    "p1=8"
}
r2 = requests.post(url=url, data=data)