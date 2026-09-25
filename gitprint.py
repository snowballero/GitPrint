import urllib.request
import json

print()
print("\033[32mGitPrint v1.0.0\033[0m")
user = input("Enter username: ")

def getuser(name):
    global request
    print()
    print("\033[90m[*] Fetching username...\033[0m")
    print()
    url = f"https://api.github.com/users/{name}"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    pinfo = json.loads(response.read().decode())
    return response.status, pinfo

status, uinfo = getuser(user)

if status == 404:
    print("User could not be found. Try again")
else:
    print("\033[34m[*] ACCOUNT\033[0m")
    print(f"├─  Name: {uinfo['name']}")
    print(f"├─  Username: {uinfo['login']}")
    print(f"├─  ID: {uinfo['id']}")
    print(f"├─  Location: {uinfo['location']}")
    print(f"└─  Bio: '{uinfo['bio']}' ")
    print()
    print("\033[35m[*] SOCIALS\033[0m")
    print(f"├─  Email: {uinfo['email']}")
    print(f"├─  Twitter (X): {uinfo['twitter_username']}")
    print(f"└─  Company: {uinfo['company']}")
    print()
    print("\033[33m[*] MISC / INFO\033[0m")
    cdate = uinfo["created_at"]
    print(f"├─   Account created at: {cdate.replace('T',' ').replace('Z','')}")
    update = uinfo["updated_at"]
    print(f"├─   Account updated at: {update.replace('T',' ').replace('Z','')}")
    print(f"├─   Followers: {uinfo['followers']}")
    print(f"├─   Following: {uinfo['following']}")
    print(f"├─   Public repo(s): {uinfo['public_repos']}")
    print(f"└─   Public gist(s): {uinfo['public_gists']}")
    print()
