"""
Teddy Bousquet
HW 5
Keith Bagely
10/18/20
"""


CHOICES = ["L","T","S","R","X","Q","P"]




def remove_brackets(song):
    """
    function: remove_brackets 
    parameters: element of a list 
    return: a string with brackets removed  
    """


    song = str(song)
    song = song.replace("[","")
    song = song.replace("]","")
    return song 
   
        

def menu():
    """
    function: menu
    does: validates user chouce
    returns nothing
    """

    answer = input("ReMix_Master:\n"  
                   "L: to Load a different song\n"
                   "T: title of current song\n"
                   "S: Substitute a word\n"
                   "R: reverse it!\n"
                   "P: Playback current song!\n"
                   "X: reset to orginal song\n"
                   "Q: to quit\n")
    answer = answer.upper()
    while answer not in CHOICES:
        answer = input("sorry! invalid input ")
    return answer





def reverse_song(sentence):
    """
    function: reverse_song
    parameters: a string
    returns: a string with the words in reverse order

    """

    
    words = sentence.split(' ')


    reverse_song = ' '.join(reversed(words))

    return reverse_song




def replace_words(sentence,old,new):

    """
    function: replace_words
    parameters: sentence(string), old(string), new(string)
    returns: string with word replaces 
    """

    sentence = sentence.replace(old,new)
    return sentence





