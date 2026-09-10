# 3 prompt url of user's twitter profile

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
username = url.removeprefix("https://twitter.com/")
print(f"{username}")