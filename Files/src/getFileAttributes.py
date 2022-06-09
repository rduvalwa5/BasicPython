'''
https://docs.python.org/3/library/os.path.html
https://www.w3resource.com/python-exercises/python-basic-exercise-107.php
'''
import glob
import os
import time

class filesAttributes:
    def __init__(self):
        self.basePath = '/Users/rduvalwa2/Music/Music/Media.localized/Music/Aerosmith/Get a Grip'
        self.artist = []
        self.albums = []
        self.fileStats = []

    def fileTypeCounter(self,path="./"):
        counts =   {}  
        files = glob.glob(os.path.join(path, "*")) # get all files in path
        for file in files:
            if os.path.isfile(file):
                path_ext = os.path.splitext(file)
                if path_ext[1] in counts:
                    counts[path_ext[1]] += 1
                else:
                    counts[path_ext[1]] = 1
        print("File Extensions in:",os.path.abspath(path))         
        for i in counts:
                print(i,":", counts[i])
        return counts

    def get_File(self,path="."):
        foundFiles = []
        allFiles = glob.glob(os.path.join(path,"*"))
        for file in allFiles:
#            print(file)
            if os.path.isfile(file):
                foundFiles.append(file)
        return foundFiles

    def get_File_stats(self,path="."):
        fileStats=[]
        for file in glob.glob(os.path.join(path,"*")):
#            print(file)
            if os.path.isfile(file):
                fileStats.append((file, os.stat(file)))
        return fileStats

    def get_File_Split(self,path="."):
        fileSplits=[]
        for file in glob.glob(os.path.join(path,"*")):
#            print(file)
#            if os.path.isfile(file):
                self.artist.append(os.path.split(file)[1])
#        return fileSplits
        
    def get_all_songs(self):
        index = 0
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        artist = self.get_music_artist()
        for a in artist:
            if os.path.isdir(self.base + "/" + a[1]):
                artist_albums = os.listdir(self.base + "/" + a[1])
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((a, album))
                        album_songs = os.listdir(self.base + "/" + a[1] + "/" + album)
                        for song in album_songs:
                            if song != '.DS_Store' and song != 'side1.mp3' and song != 'side2.mp3' and song != 'side3.mp3' and song != 'side4.mp3':
                                songs.append((index, a[1], album, song))
                                index = index + 1
        return songs
    
    def get_albums(self):
        for artist in self.get_artist():
            for artist in glob.glob(os.path.join(self.basePath , artist,"*")):
                    for file in glob.glob(os.path.join(self.basePath ,artist, "*")):
                        if os.path.isdir(file):
#                           self.albums.append(os.path.split(file)[1])
                            self.albums.append(file)
        return self.albums          

    def get_songs(self):
        albumPaths = self.get_albums()
        for file in albumPaths:
#                 if os.path.isfile(file):
#                     self.fileStats.append((file, os.stat(file)))
            for song in glob.glob(os.path.join(file, "*")):
                if os.path.isfile(song):
                    self.fileStats.append((os.path.split(song)[0],os.path.split(song)[1], os.stat(song)))
        return self.fileStats
 
if __name__ == '__main__':
    pathFiles = '/Users/rduvalwa2/Music/Music/Media.localized/Music/Aerosmith/Get a Grip'
    extension = ".mp4"
    fileObj = filesAttributes()
    results = fileObj.fileTypeCounter(pathFiles)
    print(results)
    
#    for file in fileObj.get_File(pathFiles):
#        print(file,os.path.getsize(file), time.ctime(os.path.getmtime(file)))
    
#    for file in fileObj.get_File(pathFiles):
#        print(file, os.stat(file))
        
  #  fileStats =  fileObj.get_File_stats(pathFiles) 
  #  for stat in fileStats:
  #      print(stat)
    
  #  fileObj.get_File_Split(pathFiles)
 #   allAlbums = fileObj.get_albums()
 #   for album in allAlbums:
 #       print(album)
    fileStats = fileObj.get_songs()
    for stat in fileStats:
        print(stat)
    print(len(fileStats))
 
    