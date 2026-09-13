# 3 prompt url of user's twitter profile
import re
url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")
# print(f"{username}")

# re.sub [substitue]
# re.sub(pattern, repl, string, count=0, flags=0)
#      expression we gonna look for, replacement, on which we do substitution

usrename= re.sub(r"^(https?://)?(www\.)twitter\.com/", "", url)
print(f"{usrename}")
# re.split
# re.findall search for mul copies of mattern