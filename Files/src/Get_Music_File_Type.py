'''
Created on Jun 2, 2022

@author: rduvalwa2
'''
import os, platform


class Music_Functions:

    def __init__(self):
        print("*************** Node Name is ", platform.uname().node)

        self.hostname = platform.uname().node
        if platform.uname().node == "Macbook16.local":
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized/Music"
    
        elif platform.uname().node == 'OSXAir.local':
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized/Music"
           
        else:
            print("Host is " , 'default')
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized/Music"

    def get_albums(self):
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        artists = self.get_music_artist()
        for a in artists:
            artist = a
#            print(artist)
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
#                print(artist_albums)
                for album in artist_albums:
#                    print(album)
                    if album != '.DS_Store':
                        albums.append((artist, album))
#        for album in albums:
#                print(album)
        return albums

    def get_music_artist(self):
        artist = []
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                if(directory != "."):
                    artist.append(directory)
#        for art in artist:
#            print(art)
        return artist

    def get_all_songs(self):
        albums = []
        songs = []
        artist = self.get_music_artist()
        artist.sort()
        print(artist)
        for a in artist:
#            print(a)
            if os.path.isdir(self.base + "/" + a):
                artist_albums = os.listdir(self.base + "/" + a)
                artist_albums.sort()
                for album in artist_albums:
                    if album != '.DS_Store':
                        print(a, album)
                        albums.append((a, album))
                        album_songs = os.listdir(self.base + "/" + a + "/" + album)
                        for song in album_songs:
                            if song != '.DS_Store' and song != 'side1.mp3' and song != 'side2.mp3' and song != 'side3.mp3' and song != 'side4.mp3':
                                songs.append(( artist, album, song))
        for sng in songs:
             print(sng)                       
#        print(songs)                        
#        return songs

        
if __name__ == '__main__':
    x = Music_Functions()
    
    artist = x.get_music_artist()
    artist.sort()
#    for art in artist:
#        print(art)
    albums = x.get_albums()
    albums.sort()
#    for album in albums:
#       print(album)
    mysongs = x.get_all_songs()
    mysongs.sort()
    for song in mysongs:
        print(song) 
    