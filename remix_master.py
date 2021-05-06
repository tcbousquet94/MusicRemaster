"""
Teddy Bousquet
HW 5
Keith Bagely
10/18/20
"""



CHOICES = ["L","T","S","R","X","Q"]


import remix_master_functions as r

from music import PLAYLIST as original_playlists

from music import SONGS as orginal_songs 


def main():
    
   # creates copy of list 
   playlists = original_playlists
   songs = orginal_songs
   
   # keeps track of current position in list
   song_position = 0

   # element 0 is the first song title
   playlist = playlists[song_position]
   
   # element 0 is the first song lyrics
   song = songs[song_position]
   
   # function that converts list to string and removes "[ ]"
   song = r.remove_brackets(song)
   
   while True:
        # validates user input
        answer = r.menu()
        if answer == "L":
            
                # increases position of list by one
                song_position +=1
                song = songs[song_position]
                
                # increases position of list by one
                playlist = playlists[song_position]

                # removes brackets
                song = r.remove_brackets(song)
                print(song)
                
        elif answer == "T":
            
            # prints current song
            print(playlist)
            
        elif answer == "S":
            
            old = input("what word would you like to replace")
            new = input("what word would you like to replace it with?")
            # replaces old word with user input and return string
            song = r.replace_words(song,old,new)
            print(song)
            
        elif answer == "R":

            # function that reverses song
            song = r.reverse_song(song)
            print(song)
            
        elif answer == "X":

            # prints orginal song from orginal list
            song = songs[song_position]
            song = r.remove_brackets(song)
            print(song)
            
        elif answer == "P":

           # prints current version of the song
            print(song)
            
        elif answer == "Q":

            # quits application
            print("thanks for using the remix master!")
            break 
            
        
            
main()
