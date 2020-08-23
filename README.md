# V01D-Terminal

[![GitHub](https://img.shields.io/github/license/Stax124/V01D-Terminal?style=for-the-badge)](https://github.com/Stax124/V01D-Terminal/blob/master/LICENSE)
[![GitHub](https://img.shields.io/github/last-commit/Stax124/V01D-Terminal?style=for-the-badge)](https://github.com/Stax124/Void-Terminal/commits/master)
![GitHub](https://img.shields.io/github/downloads/Stax124/V01D-Terminal/total?color=%230000ff&logo=GitHub&style=for-the-badge)
[![GitHub](https://img.shields.io/github/v/release/Stax124/V01D-Terminal?label=Stable&style=for-the-badge)](https://github.com/Stax124/V01D-Terminal/releases)
[![GitHub](https://img.shields.io/github/v/release/Stax124/V01D-Terminal?include_prereleases&label=latest&style=for-the-badge)](https://github.com/Stax124/V01D-Terminal/releases)


<p align="center">
  <img src="img/Autocompletion.png">
</p>

Easy to use **Windows** terminal made by **Stax124**

V01D-Terminal is **Python** based terminal application build on prompt-toolkit library.

Can be runned as individual or you can pass arguments

# Functions
  - Execute wide range of commands from cmd and powershell
  - Calculator
  - Aliases
  - Audio file conversion
  - Temperature conversion
  - Color name to HEX or RGB values
  - URL file download
  - Hashing (md5,sha)
  - Wifi password recovery
  - Quick access to administrative functions
  - Get component info (cpu, gpu ... )
  - Weather data
  - Stocks
  - Cryptocurrency
  - QRCode generator
  - GUID generator
  - Geolocation of IP
  - Public IP
  - Get last youtube video, tweet
  - Check if twitch streamer is online
  - Shortening URL
  - Temporary cloud storage
  - Covid19 stats
  - File conversion
  - Dns check

# Void
  - Show config: **void config**
  - Select mode: **void mode [CMD,POWERSHELL]**
  - Install optional files or programs: **void install [name]**
  - Toggle multithreading: **void multithreading [true,false]**
  - Toggle fuzzy completion: **void fuzzycomplete [true,false]**
  - Toggle wraping lines: **void wrapLines [true,false]**
  - Toggle mouse support: **void mouseSupport [true,false]**
  - Toggle completion while typing: **void completeWhileTyping [true,false]**
  - Show welcome screen: **void welcome**
  - Show license: **void license {full}**
  - Start new window: **void start**
  - Update all python packages: **void updatePythonPackages**
  - Set title: **void title [string]**

# Calculator:
  - Basic math operations can be typed right into the terminal: **2+2-(6/9)**
  - More complicated operations can be called as functions: **sin(2)+ceil(max([1,2,3,4]))**
  - Some basic constants are available out of the box: **pi, tau, e**...
  - Greatest common divisor: **gcd float,float**
  - Lowest common multiplier: **lcm float,float**
  - Random number generator: **rng min,max[not included]**

# Components
  - Get all information about your rig: **component**
  - Get separate information about hardware: **cpu, gpu, ram, disk, network, bootinfo, motherboard, pagefile**

# Function commands
  - Clear window content: **clear, cls**
  - Run shell as administrator: **admin, elevate**
  - Exit application: **exit, quit**
  - Get os name: **os**
  - Open current directory: **open**
  - Read file contents: **read [file]**
  - Shutdown machine: **poweroff**
  - Reboot machine: **reboot**
  - Go back one directory: **back**
  - Change brightness or get it´s value: **brightness {value}**
  - Evaluate string as python code (Requires Python): **eval**
  - Get size of folder: **sizeof [folder]**
  - Open Windows 10 God mode control panels: **godmode**
  - Grant access administrative privileges to all files in current directory: **grantfiles**

# Alias
  - Make new alias, if alias is found in user's input, it will be replaced by value': **alias [name] [value]**
  - List all local aliases: **alias -list**
  - Remove alias: **delalias [name]**

# Music player
  - Initialize player and play file: **music-play [file]**
  - Pause current track: **music-pause**
  - Resume current track: **music-resume**
  - Stop current track: **music-stop**
  - Set volume: **music-volume [taget(0-100)]**

# Curl commands
  - Get DNS information: **dns**
  - Get external ip: **ip**
  - Check last youtube video of channel: **checklastvid [channel]**
  - Check last twitter post: **checklasttweet [user]**
  - Check if streamer is online on Twitch: **checktwitchonline [name]**
  - Convert file like pdf into HTML: **fileconverter [input file type] [output file type] [file] [new filename]**
  - Monitor your server: **ping.gg {query}**
  - Generate random GUID: **guid**
  - Shorten URL: **shorten [URL]**
  - Transfer file to temporary cloud storage: **transfer [file]**
  - Test your internet connection (Requires Python): **speedtest**
  - Check weather in location: **weather {location or query}**
  - Get statistics about Covid19: **covid19 {location}**
  - Get geolocation of IP address: **geoip {IP}**
  - Generate QRCode from string: **qrcode [string]**
  - Cheat sheet: **cheat {query}**
  - Get stock information of company: **stonks {short company name(Intel > INTL)}**
  - Cryptocurrency trading information: **cryptocurrency {currency or query}**

# Hashing
  - Available hashing algorithms: **md5, sha1, sha224, sha256, sha384, sha512**
  - Hash string: **[hash function] [string]**
  - Hash file **[hash function]sum [file]**

# Convert
  - Convert currency: **currencyconverter [Base] [Target] [Value]**
  - Temperature: **convert [Base] [Target] [Value]**
  - Color to HEX or RGB: **convert color [rgb,hex,list] {color name}**
  - Decimal - Hexadecimal: **convert decimal hexadecimal [value]**
  - Decimal - Octal: **convert decimal octal [value]**
  - Decimal - Binary: **convert decimal binary [value]**
  - Roman - Integer: **convert roman int [string]**
  - Audio (ffmpeg must be installed and on PATH): **convert [audio format(mp3,m4a,wav)] [file to be formatted]**

# Windows 10
  - Open startup folder: **startup**
  - Open setting: **settings**
  - Change power scheme: **power**
  - Get localy saved Wifi password: **password**

# Other
  - Check if your password is in leaked databases: **pwned [string]**
  - Download file from internet: **download [-list,URL,dictionary key]**
  - Download YouTube video: **ytdown [URL]**
  - Search web: **search [querry]**
  - Open auto-py-to-exe Python compiler (must be installed and on PATH): **compile**
  - Convert file or string into list of strings: **plain2string [line,file,fileline] {file}**
  - Get ETA of downloading: **downloadeta [target][suffix] [download speed][suffix]**
