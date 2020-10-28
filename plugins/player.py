import mpv
import yaml

class c:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

playing = False

class Player(mpv.MPV):
    def _logger(self, loglevel, component, message):
        print(f'{c.okgreen}[{loglevel}]{c.end} {c.bold}{component}:{c.end} {message}', flush=True)
    
    def __init__(self, volume: 100, volume_max: 130, _format):
        super().__init__(
            player_operation_mode='pseudo-gui',
            log_handler=self._logger,
            input_default_bindings=True,
            input_vo_keyboard=True,
            osc=True,
            load_unsafe_playlists=True,
            volume=volume,
            volume_max=volume_max,
            ytdl_format=_format)

    def global_play(self, target):
        global playing
        
        if not playing:
            print(f"{c.bold}Starting MPV session...{c.end}")
            try:
                f = open(target, "r")
                links = f.readlines()
                for link in links:
                    self.playlist_append(link)
            except:
                self.playlist_append(target)

            self.playlist_pos = 0
            playing = True
            self.wait_for_shutdown()
            self.terminate()
            playing = False
        else:
            try:
                f = open(target, "r")
                links = f.readlines()
                for link in links:
                    self.playlist_append(link)
            except:
                self.playlist_append(target)
