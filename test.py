import yaml

settings = {
    "multithreading":True,
    "fuzzycomplete":True
}

with open(r"config.yml", "w") as file:
    doc = yaml.dump(settings,file)