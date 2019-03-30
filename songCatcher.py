import re, os, shutil
# from pause import pause
currentDir = os.curdir


def start():
    
    playlistFile = getPlaylist()
    os.chdir(currentDir)
    data = r'{}'.format(playlistFile.read())
    songsLocation = findSongs(data)
    # print(songsLocation[0])
    outputDir = input('\nEnter Output Directory : ')
    copySongs(songsLocation, outputDir)
    print('\nCopying Done.')


def getPlaylist():
    playlistPath = input("Enter the Path to Playlist : ")

    if os.path.isdir(playlistPath):
        playlistName = input("\nEnter the Name of the Playlist : ")
        os.chdir(playlistPath)
        try:
            playlistFile = open(playlistName, encoding="utf8")
            return playlistFile
        except:
            print("Something went wrong !!!\nCouldn't access the file {p}".format(p=playlistName))

    elif os.path.isfile(playlistPath):
        try:
            playlistFile = open(playlistPath, encoding="utf8")
            return playlistFile
        except:
            print("Something went wrong !!!\nCouldn't access the file {p}".format(p=os.path.basename(playlistPath)))
        
    else:
        print('Path provided is "INVALID"')


def findSongs(data):
    
    pattern = re.compile(r'<media\ssrc="(.+)"\salbumTitle')
    matches = pattern.finditer(data)
    songsLocation = []
    for match in matches:
        # print(match.group(0),'\n')
        songsLocation.append(match.group(1))
    # print(str(songsLocation))
    # print('\nLength of Playlist : ',songsLocation.__len__())
    return songsLocation


def copySongs(songsLocation, outputDir):
    fail_list = []
    for song in songsLocation:
        #song.replace(r'\\\\',r'\\')
        #print('\n\nNew Song : ',song)
        #pause()
        if '&amp;' in song:
            # print(song)
            song = song.replace('&amp;','&')
            # print(song)
            # pause()
        try:
            shutil.copy(os.path.join(song, song), outputDir)
        except:
            fail_list.append(song)

    if(fail_list.__len__()>0):
        print("\nCouldn't copy the following Songs : ")
        for song in fail_list:
            print('{n}. {s}'.format(n=(fail_list.index(song)+1),s=song)) 

if __name__ == '__main__':
    start()