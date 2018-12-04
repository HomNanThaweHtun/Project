def menu():
    print ("Menu:\nL - List Songs\nA - Add new song\nC - Complete a song\nQ - Quit\n")
    choice = input(prompt).upper()
    while choice not in list("LACQ"):
        print("Invalid menu choice")
        choice = input(prompt).upper()
    return choice

"""
loading songs
    list_of_songs = list
    in_file = open songs.csv (r)
    for line in in_file
        remove new character
        song_artist_year_list = split line for ","
        list_of_song = append song_artist_year_list
    return list_of_song
"""
def load_songs():
    list_of_songs = []
    in_file = open(Filename, 'r')
    for line in in_file:
        song_artist_year_list = line.split(",")
        list_of_song.append(song_artist_year_list)
    in_file.close()
    return list_of_songs

def display_songs(list of song):
count = 0
for i in range(len(list_of_song[i]) - 2):
