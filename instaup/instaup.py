import instaloader
from internetarchive import upload
from internetarchive import get_item
from os import rmdir
from os import path
import argparse

def downloadUser(username, respectPrivacy):
    loader = instaloader.Instaloader(dirname_pattern='{profile}', compress_json=False)
    loader.load_session_from_file('rileyjnielsen')
    profile = instaloader.Profile.from_username(loader.context, username)
    if ((profile.is_private == True) and (respectPrivacy == True)):
        print (username + " is a private profile. Exiting...")
        return False
    loader.download_profiles([profile], igtv=True, highlights=True, stories=True)
    return True

def uploadUser(username, deletionStatus):
    item = get_item('instagram-' + username)
    try:
        item.upload('./' + username + '/', verbose=True, checksum=True, delete=deletionStatus, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
    except:
        print ("An error occurred, trying again.")
        item.upload('./' + username + '/', verbose=True, checksum=True, delete=deletionStatus, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 1.0'), retries=9001, retries_sleep=60)
    try:
        rmdir(username)
        print ("Deleted folder " + username)
        return
    except:
        return

def main():
    parser = argparse.ArgumentParser(description='An auto downloader and uploader for Instagram profiles.')
    parser.add_argument('user')
    parser.add_argument('--privacy', action='store_true', help="check the user's privacy settings")
    parser.add_argument('--delete', action='store_true', help="delete files when done")
    args = parser.parse_args()
    username = args.user
    privacy = args.privacy
    delete = args.delete
    didItWork = downloadUser(username, privacy)
    if (didItWork == True):
        uploadUser(username, delete)

if __name__ == '__main__':
    main()
