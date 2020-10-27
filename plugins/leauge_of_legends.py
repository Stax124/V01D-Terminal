import requests
import difflib
from tabulate import tabulate

champions = {
        "1": "Annie",
        "10": "Kayle",
        "101": "Xerath",
        "102": "Shyvana",
        "103": "Ahri",
        "104": "Graves",
        "105": "Fizz",
        "106": "Volibear",
        "107": "Rengar",
        "11": "MasterYi",
        "110": "Varus",
        "111": "Nautilus",
        "112": "Viktor",
        "113": "Sejuani",
        "114": "Fiora",
        "115": "Ziggs",
        "117": "Lulu",
        "119": "Draven",
        "12": "Alistar",
        "120": "Hecarim",
        "121": "Khazix",
        "122": "Darius",
        "126": "Jayce",
        "127": "Lissandra",
        "13": "Ryze",
        "131": "Diana",
        "133": "Quinn",
        "134": "Syndra",
        "136": "AurelionSol",
        "14": "Sion",
        "141": "Kayn",
        "142": "Zoe",
        "143": "Zyra",
        "145": "Kaisa",
        "15": "Sivir",
        "150": "Gnar",
        "154": "Zac",
        "157": "Yasuo",
        "16": "Soraka",
        "161": "Velkoz",
        "163": "Taliyah",
        "164": "Camille",
        "17": "Teemo",
        "18": "Tristana",
        "19": "Warwick",
        "2": "Olaf",
        "20": "Nunu",
        "201": "Braum",
        "202": "Jhin",
        "203": "Kindred",
        "21": "MissFortune",
        "22": "Ashe",
        "222": "Jinx",
        "223": "TahmKench",
        "23": "Tryndamere",
        "235": "Senna",
        "236": "Lucian",
        "238": "Zed",
        "24": "Jax",
        "240": "Kled",
        "245": "Ekko",
        "246": "Qiyana",
        "25": "Morgana",
        "254": "Vi",
        "26": "Zilean",
        "266": "Aatrox",
        "267": "Nami",
        "268": "Azir",
        "27": "Singed",
        "28": "Evelynn",
        "29": "Twitch",
        "3": "Galio",
        "30": "Karthus",
        "31": "Chogath",
        "32": "Amumu",
        "33": "Rammus",
        "34": "Anivia",
        "35": "Shaco",
        "350": "Yuumi",
        "36": "DrMundo",
        "360": "Samira",
        "37": "Sona",
        "38": "Kassadin",
        "39": "Irelia",
        "4": "TwistedFate",
        "40": "Janna",
        "41": "Gangplank",
        "412": "Thresh",
        "42": "Corki",
        "420": "Illaoi",
        "421": "RekSai",
        "427": "Ivern",
        "429": "Kalista",
        "43": "Karma",
        "432": "Bard",
        "44": "Taric",
        "45": "Veigar",
        "48": "Trundle",
        "497": "Rakan",
        "498": "Xayah",
        "5": "XinZhao",
        "50": "Swain",
        "51": "Caitlyn",
        "516": "Ornn",
        "517": "Sylas",
        "518": "Neeko",
        "523": "Aphelios",
        "53": "Blitzcrank",
        "54": "Malphite",
        "55": "Katarina",
        "555": "Pyke",
        "56": "Nocturne",
        "57": "Maokai",
        "58": "Renekton",
        "59": "JarvanIV",
        "6": "Urgot",
        "60": "Elise",
        "61": "Orianna",
        "62": "MonkeyKing",
        "63": "Brand",
        "64": "LeeSin",
        "67": "Vayne",
        "68": "Rumble",
        "69": "Cassiopeia",
        "7": "Leblanc",
        "72": "Skarner",
        "74": "Heimerdinger",
        "75": "Nasus",
        "76": "Nidalee",
        "77": "Udyr",
        "777": "Yone",
        "78": "Poppy",
        "79": "Gragas",
        "8": "Vladimir",
        "80": "Pantheon",
        "81": "Ezreal",
        "82": "Mordekaiser",
        "83": "Yorick",
        "84": "Akali",
        "85": "Kennen",
        "86": "Garen",
        "875": "Sett",
        "876": "Lillia",
        "89": "Leona",
        "9": "Fiddlesticks",
        "90": "Malzahar",
        "91": "Talon",
        "92": "Riven",
        "96": "KogMaw",
        "98": "Shen",
        "99": "Lux"
}

class c:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def get_champion_json(champion: str) -> dict:
    print("Please wait...")
    response = requests.get("https://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_GB/championFull.json").json()["data"]
    close_match = difflib.get_close_matches(champion,champions.values())
    print(close_match)
    return response[close_match[0]]

def get_champions_info(champion: str) -> str:
    ch = get_champion_json(champion)

    print(
f"""
Name: {ch["id"]}
ID: {ch["key"]}
Info:
    Attack: {ch["info"]["attack"]}
    Defense: {ch["info"]["defense"]}
    Difficulty: {ch["info"]["difficulty"]}
    Magic: {ch["info"]["magic"]}
Lore: {ch["lore"]}
""")

print(get_champion_json("Aatrox"))
