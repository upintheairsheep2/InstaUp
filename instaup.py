import instaloader
import datetime
from internetarchive import upload
from internetarchive import get_item
from os import rmdir
from os import path

currentTime = datetime.datetime.now(datetime.timezone.utc)
fixedTime = str(currentTime.strftime("%Y%m%d%H%M%S"))
loader = instaloader.Instaloader(dirname_pattern='{profile}-' + fixedTime)
username = '<PROFILE>'
loader.load_session_from_file('<YOUR INSTAGRAM USERNAME>')
profile = instaloader.Profile.from_username(loader.context, username)
loader.download_profiles([profile], igtv=True, highlights=True, stories=True)
fullName = username + '-' + fixedTime
item = get_item('instagram-' + fullName)
try:
    item.upload('./' + fullName + '/', verbose=True, delete=True, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
except:
    print ("An error occurred, trying again.")
    item.upload('./' + fullName + '/', verbose=True, delete=True, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
rmdir(fullName)
