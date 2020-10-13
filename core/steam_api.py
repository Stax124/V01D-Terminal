from steamapi.user import SteamUser
import steamapi
from prettytable import PrettyTable

me = None

def connect(api_key: str) -> None:
    steamapi.core.APIConnection(api_key=api_key, validate_key=True)

def profile(userurl: str) -> None:
    global me
    me = steamapi.user.SteamUser(userurl=userurl)

def profileID(userID: str) -> None:
    global me
    me = steamapi.user.SteamUser(userID)

def friends() -> PrettyTable:
    t = PrettyTable(["Name", "Id"])

    friendlist = []
    for friend in me.friends:
        friendlist.append(friend.name)
        t.add_row([friend.name, friend.id])

    return t

def me() -> SteamUser:
    return me