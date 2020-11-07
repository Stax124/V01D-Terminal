import os
from Void import Void_Terminal, c

app = Void_Terminal()
error_count = 0

for i in [
    'welcome',
    'help',
    'void license',
    "2+2",
    "2*2",
    "2/2",
    "2**2",
    "2//2",
    "pi",
    "2 * degrees(sin(6))",
    "rng 256 458",
    "lcm 562 695",
    "gcd 81 27",
    "component",
    "motherboard",
    "pagefile",
    "control",
    "os",
    "ytdown https://www.youtube.com/watch?v=iW5fN65oNls -F",
    "player volume 100",
    "player play nothing",
    "player terminate",
    "alias DSADADA start explorer",
    "alias -list",
    "delalias DSADADA",
    "stonks amd/intl/tsla",
    "ip",
    "geoip",
    "covid19 CZ",
    "weather moon",
    "qrcode HELP",
    "motherboard",
    "cryptocurrency btc@1d",
    "dns",
    "shorten https://www.youtube.com/watch?v=_pjwRvLnF0w&list=RDH4XtFifQzF0&index=2",
    "guid",
    "ping.gg",
    "checklastvid LinusTechTips",
    "cheat python lambda",
    "read .\\debug.log",
    "sha256sum Void.py",
    "open %USERPROFILE%\\Downloads",
    "sha512 password",
    "convert celsius kelvin 27",
    "currencyconverter CZK USD 20000",
    "plain2string .\\config.json",
    "downloadeta 50GB 2MB",
    "cd C:\\Users",
    "back",
    "tasklist",
    "steam game 'Team fortress 2'",
    "game-deals",
    ]:
    userInput = app.envirotize(i)
    try:
        app.switch(userInput)
    except Exception as e: 
        print(f"{c.fail}{e}{c.end}")
        error_count += 1
        os.system("pause")

print(f'\n{c.bold}Completed - {c.end}{c.warning}{error_count}{c.end} {c.bold}Errors{c.end}')