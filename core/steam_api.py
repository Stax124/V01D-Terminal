from tabulate import tabulate
from steamapi.user import SteamUser
import steamapi

me = None

def connect(api_key: str) -> None:
    steamapi.core.APIConnection(api_key=api_key, validate_key=True)

def profile(userurl: str) -> None:
    global me
    me = steamapi.user.SteamUser(userurl=userurl)

def profileID(userID: str) -> None:
    global me
    me = steamapi.user.SteamUser(userID)

def friends() -> str:
    t = list()

    friendlist = []
    for friend in me.friends:
        friendlist.append(friend.name)
        t.append([friend.name, friend.id])

    return tabulate(t,["Name", "Id"])

def me() -> SteamUser:
    return me