from Config.Singleton import Singleton
from Config.Configs import BConfigs


class Helper(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = BConfigs()
            self.HELP_SKIP = 'skip skip skip a beat'
            self.HELP_SKIP_LONG = 'Skips current song. Won\'t work if "loop one" is on'
            self.HELP_RESUME = 'Resumes the song player.'
            self.HELP_RESUME_LONG = 'Resume if paused'
            self.HELP_CLEAR = 'Clear the queue and songs history.'
            self.HELP_CLEAR_LONG = 'Clear queue and history'
            self.HELP_STOP = 'Make the bot kill itself.'
            self.HELP_STOP_LONG = 'Make the bot kill itself.'
            self.HELP_LOOP = 'Loop functionality'
            self.HELP_LOOP_LONG = 'Loop functionality.\nArgs: one, off, all, ""'
            self.HELP_NP = 'Show the info of the current song.'
            self.HELP_NP_LONG = 'Show "Now Playing"'
            self.HELP_QUEUE = f'Show the first {config.MAX_SONGS_IN_PAGE} songs in queue.'
            self.HELP_QUEUE_LONG = f'Show the first {config.MAX_SONGS_IN_PAGE} songs in the queue.'
            self.HELP_PAUSE = 'Pauses the song player.'
            self.HELP_PAUSE_LONG = 'Pauses.'
            self.HELP_PREV = 'Play the previous song.'
            self.HELP_PREV_LONG = 'Plays previous song. If a song is playing, it will return to the previous song.'
            self.HELP_SHUFFLE = 'Shuffle the songs playing.'
            self.HELP_SHUFFLE_LONG = 'Shuffles.'
            self.HELP_PLAY = 'Plays a song.'
            self.CHANGE_VOLUME = 'Set volume'
            self.CHANGE_VOLUME_LONG = 'Set volume between 0 and 100.'
            self.HELP_PLAY_LONG = 'Plays a song.'
            self.HELP_HISTORY = f'Show song history.'
            self.HELP_HISTORY_LONG = f'Show the last {config.MAX_SONGS_HISTORY} played songs'
            self.HELP_MOVE = 'Moves a song from position pos1 to pos2 in queue.'
            self.HELP_MOVE_LONG = 'Moves a song from position pos1 to pos2 in queue.'
            self.HELP_REMOVE = 'Remove a song at position x.'
            self.HELP_REMOVE_LONG = 'Remove a song at position x.'
            self.HELP_RESET = 'Reset the Player of the server.'
            self.HELP_RESET_LONG = 'Reset the Player of the server. Useful for debugging'
            self.HELP_HELP = f'Use {config.BOT_PREFIX}help <command> for more info.'
            self.HELP_HELP_LONG = f'Nice recursion bro'
            self.HELP_INVITE = 'Send invite URL'
            self.HELP_INVITE_LONG = 'Sends bot invite link'
            self.HELP_WAHL = 'Ask the "Heilige Wahlkommission" a question'
            self.HELP_WAHL_LONG = 'Asks the "Heilige Wahlkommission" for salvation and enlightenment.'
            self.HELP_ALERT = 'Pings you after some time.'
            self.HELP_ALERT_LONG = 'Pings you after some time. Format: [1-60][s,m,h,d] (ID/Message) (Message).'
            self.HELP_CLEAN = 'Cleans messages sent by bot and bot commands'
            self.HELP_CLEAN_LONG = (f'Cleans messages sent by bot and bot commands.\nFormat: {config.BOT_PREFIX}clean [(user,bot,all,any,saul) (n)]'
                                    f', defaults are all, 20.\nArgument order doesn\'t matter.\nQueries the last {config.CLEAN_AMOUNT} messages.\n\n'
                                    f'user = messages that start with "{config.BOT_PREFIX}"\nbot = messages by bot\nall = both\n'
                                    f'any = any message (effectively a purge command)\nsaul = messages from saul goodman as he likes to spam')
            self.HELP_RESTART = 'Restart the bot.'
            self.HELP_RESTART_LONG = 'Restarts the bot. Can only be used by bot admins.'
            self.HELP_BAN = 'Bans a user from using Blueshellbot.'
            self.HELP_BAN_LONG = ('Bans a user from using the bot. Any command they run will not work and will not be executed.'
                                  'This command is admin only')
            self.HELP_FEET = 'laal.'
            self.HELP_FEET_LONG = 'Maggda loves feets and loves briar imagine he had brier feets aka YOU CANT PLURALS YOU CAKE SNAKE SKIBIDI SEVERUS SNAPE'

            self.SLASH_QUEUE_DESCRIPTION = f'Number of queue page, there are only {config.MAX_SONGS_IN_PAGE} songs by page'
            self.SLASH_MOVE_HELP = 'Moves a song from position pos1 to pos2 in queue.'
