import requests
import yaml
import hashtableUpdater

# Get latest server hashtable
hashtable = requests.get("https://github.com/Stax124/V01D-Terminal/hashtable-server.yml")

dictionary = yaml.safe_load(open("hashtable-server.yml"))
toUpdate = list()

try:
    for i in dictionary.keys():
        try:
            if hashtableUpdater.hash(i) == dictionary[i]:
                print(f"{i} is outdated")
                toUpdate.append(i)
        except:
            print(f"{i} is not accessible")
except:
    print("dictionaryError")

