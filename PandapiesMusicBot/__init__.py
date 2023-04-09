join ko ko inifrom PandapiesMusicBot.core.bot import PandapiesBot
from PandapiesMusicBot.core.dir import dirr
from PandapiesMusicBot.core.git import git
from PandapiesMusicBot.core.userbot import Userbot
from PandapiesMusicBot.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = PandapiesBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
