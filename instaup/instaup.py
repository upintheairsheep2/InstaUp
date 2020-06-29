import instaloader
from internetarchive import upload
from internetarchive import get_item
from os import rmdir
from os import path
from os import chdir
from os import mkdir
from os import listdir
import sys
import argparse


def downloadUser(username, respectPrivacy, login):
    loader = instaloader.Instaloader(dirname_pattern='{profile}', compress_json=False)
    x = listdir()
    for i in x:
        if login == None:
            if i.endswith('.login'):
                y = i.split('.')
                login = y[0]
            else:
                login = input('Type in an Instagram username: ')
    try:
        loader.load_session_from_file(str(login), str(login) + '.login')
    except:
        loader.interactive_login(str(login))
        loader.save_session_to_file(str(login) + '.login')
        loader.load_session_from_file(str(login), str(login) + '.login')
    profile = instaloader.Profile.from_username(loader.context, username)
    if ((profile.is_private == True) and (respectPrivacy == True)):
        print (username + " is a private profile. Exiting...")
        return False
    loader.download_profiles([profile], igtv=True, highlights=True, stories=True)
    return True

def uploadUser(username, deletionStatus):
    item = get_item('instagram-' + username)
    try:
        item.upload('./' + username + '/', verbose=True, checksum=True, delete=deletionStatus, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 2020.06.29'), retries=9001, retries_sleep=60)
    except:
        print ("An error occurred, trying again.")
        item.upload('./' + username + '/', verbose=True, checksum=True, delete=deletionStatus, metadata=dict(collection='opensource_media', subject='instagram', creator=username, title='Instagram Profile: ' + username, originalurl='https://www.instagram.com/' + username, scanner='InstaUp 2020.06.29'), retries=9001, retries_sleep=60)
    try:
        rmdir(username)
        print ("Deleted folder " + username)
        return
    except:
        return

def main():
    chdir(path.expanduser('~'))
    if (path.exists('./.instaup') == False):
        mkdir('./.instaup')
    chdir('./.instaup')
    parser = argparse.ArgumentParser(description='An auto downloader and uploader for Instagram profiles.')
    parser.add_argument('user')
    parser.add_argument('--privacy', action='store_true', help="check the user's privacy settings")
    parser.add_argument('--delete', action='store_true', help="delete files when done")
    parser.add_argument('--login', help="login with specified username")
    args = parser.parse_args()
    username = args.user
    privacy = args.privacy
    delete = args.delete
    login = args.login
    didItWork = downloadUser(username, privacy, login)
    if (didItWork == True):
        uploadUser(username, delete)

if __name__ == '__main__':
    main()
