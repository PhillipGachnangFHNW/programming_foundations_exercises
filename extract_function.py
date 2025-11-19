data = {
    "www.google.ch": "pw2",
    "www.gmx.ch": "pw"
}

search = "goo"
for key in data.keys():
    if search in key:
        print(key)

if "www.facebook.com" not in data:
    data["www.facebook.com"] = []
data["www.facebook.com"].append("pw3476")

