import instaloader
from internetarchive import upload
from internetarchive import get_item
from os import rmdir
from os import path

def downloadUser(username, respectPrivacy):
    loader = instaloader.Instaloader(dirname_pattern='{profile}', compress_json=False)
    loader.load_session_from_file(<YOUR INSTAGRAM USERNAME>)
    profile = instaloader.Profile.from_username(loader.context, username)
    if ((profile.is_private == True) and (respectPrivacy == ('yes' or 'Yes' or 'Y' or 'y'))):
        print (username + " is a private profile. Exiting...")
        return False
    loader.download_profiles([profile], igtv=True, highlights=True, stories=True)
    return True

def uploadUser(username, shouldDelete):
    if (shouldDelete == ('yes' or 'Yes' or 'Y' or 'y')):
        deletionStatus = True
    else:
        deletionStatus = False
    item = get_item('instagram-' + username)
    try:
        item.upload('./' + username + '/', verbose=True, checksum=True, delete=deletionStatus, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
    except:
        print ("An error occurred, trying again.")
        item.upload('./' + username + '/', verbose=True, checksum=True, delete=deletionStatus, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
    try:
        rmdir(username)
        print ("Deleted folder " + username)
    except:
        print ("Didn't delete " + username)

user = input('Enter in an Instagram username: ')
privacy = input('Should I respect the user\'s privacy? ')
deletion = input('Do you want to delete files when done? ')
didItWork = downloadUser(user, privacy)
if (didItWork == True):
    uploadUser(user, deletion)
