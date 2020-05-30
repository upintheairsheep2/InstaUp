import instaloader
import datetime
from internetarchive import upload
from internetarchive import get_item
from os import rmdir
from os import path

def getTime():
    currentTime = datetime.datetime.now(datetime.timezone.utc)
    return str(currentTime.strftime("%Y%m%d%H%M%S"))

def downloadUser(username, respectPrivacy, time):
    loader = instaloader.Instaloader(dirname_pattern='{profile}-' + time)
    loader.load_session_from_file(<YOUR INSTAGRAM USERNAME>)
    profile = instaloader.Profile.from_username(loader.context, username)
    if ((profile.is_private == True) and (respectPrivacy == ('yes' or 'Yes' or 'Y' or 'y'))):
        print (username + " is a private profile. Exiting...")
        return False
    loader.download_profiles([profile], igtv=True, highlights=True, stories=True)
    return True

def uploadUser(username, time):
    fullName = username + '-' + time
    item = get_item('instagram-' + fullName)
    try:
        item.upload('./' + fullName + '/', verbose=True, delete=True, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
    except:
        print ("An error occurred, trying again.")
        item.upload('./' + fullName + '/', verbose=True, delete=True, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
    rmdir(fullName)

fullTime = getTime()
user = input('Enter in an Instagram username: ')
privacy = input('Should I respect people\'s privacy? ')
didItWork = downloadUser(user, privacy, fullTime)
if (didItWork == True):
    uploadUser(user, fullTime)
