import instaloader
import datetime
from internetarchive import upload
from internetarchive import get_item
from os import rmdir

currentTime = datetime.datetime.now(datetime.timezone.utc)
fixedTime = str(currentTime.strftime("%Y%m%d%H%M%S"))
loader = instaloader.Instaloader(dirname_pattern='{target}-' + fixedTime)
username = '<PROFILE>'
loader.load_session_from_file('<YOUR INSTAGRAM USERNAME>')
profile = instaloader.Profile.from_username(loader.context, username)
loader.download_profiles([profile], igtv=True, highlights=True, stories=True)
fullName = username + '-' + fixedTime
item = get_item('instagram-' + fullName)
item.upload('./' + fullName + '/', verbose=True, delete=True, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'))
rmdir(fullName)
