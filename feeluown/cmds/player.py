from .base import AbstractHandler


class PlayerHandler(AbstractHandler):
    cmds = ('play', 'pause', 'stop', 'resume', 'toggle', )

    def handle(self, cmd):
        if cmd.action == 'play':
            song_furi = cmd.args[0]
            return self.play_song(song_furi.strip())
        elif cmd.action == 'pause':
            # FIXME: please follow ``Law of Demeter``
            self.player.pause()
        elif cmd.action == 'stop':
            self.player.stop()
        elif cmd.action == 'resume':
            self.player.resume()
        elif cmd.action == 'toggle':
            self.player.toggle()

    def play_song(self, song_furi):
        song = self.model_parser.parse_line(song_furi)
        if song is not None:
            self.player.play_song(song)
