import re

emailAddress = input()
username = "(\w+)@(\w+)\.+(\w+)"
r2 = re.match(username, emailAddress)
print(r2.group(2))
