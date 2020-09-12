import os
import sys
import requests
import platform
import yaml

class Download():
    def __init__(self, promptinstall: bool, dictionarypath: list, startifexeption: bool, returnexeption: bool):
        self.returnexeption = returnexeption
        self.promptinstall = promptinstall
        self.startifexeption = startifexeption
        self.dictionarypath = dictionarypath
        self.maindict = dict()
        self.buildmaindict()
    def buildmaindict(self):
        for i in self.dictionarypath:
            try:
                downloadDict = dict(yaml.safe_load(open(i)))
                for key in downloadDict.keys():
                    self.maindict[key] = downloadDict.get(key)
            except: print(f"{i} cannot be loaded (file doesn't exist or is empty), consider removing it from config.yml")
    def download(self,target):
        try:
            url = self.maindict.get(target)
            urlSplit = url.split("/")
        except:
            try:
                url = target
                urlSplit = url.split("/")
                requests.get(url)
            except:
                return ConnectionRefusedError

        try:
            wd = os.getcwd()
            if platform.system() == "Windows":
                os.chdir(os.environ["USERPROFILE"]+"\\Downloads")
            else:
                os.chdir("/tmp")
            fileName = urlSplit[-1]
            with open(fileName, "wb") as f:
                print(f"Downloading {fileName}")
                response = requests.get(url, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None:  # no content length header
                        f.write(response.content)
                else:
                    print(f"Filesize: {int(total_length) / 1000000} MB")
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write(f"\r#{'=' * done}{' ' * (50-done)}#   {done*2}%   {int(((dl / total_length) * total_length) / 1000000)} MB")
                        sys.stdout.flush()
            print()

            if self.promptinstall:
                fsplit = fileName.split(".")
                if fsplit[-1] == "exe" or fsplit[-1] == "msi":
                    from prompt_toolkit import confirm
                    run = confirm("Run installer ? ")
                    if run:
                        try:
                            os.system(f"start {fileName}")
                        except Exception as error:
                            print(error)

            os.chdir(wd)
                
        except Exception as e:
            if self.startifexeption:
                os.system("start " + url)
            if self.returnexeption:
                return e
            else:
                print(e)
            

if __name__ == "__main__":
    import Void
    Void.main()