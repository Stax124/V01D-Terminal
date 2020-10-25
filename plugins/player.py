import mpv

playing = False

class Player(mpv.MPV):
    def _logger(self, loglevel, component, message):
        print('[{}] {}: {}'.format(
            loglevel, component, message), flush=True)
    
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
