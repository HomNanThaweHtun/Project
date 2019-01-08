"""
Student Name: Hom Nan Thawe Htun
Student ID: 13644108
Github: https://github.com/CP1404-2017-2/a1-YeYintThetKhine/blob/master/assignment1.py
"""
from operator import itemgetter

file_name = "songs.csv"
in_file = open("songs.csv", 'r')

#to display the main menu
def main_menu():
    prompt = "Menu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>> "
    choice = input(prompt).upper()
    while choice not in list("LACQ"):
        print("Invalid menu choice.")
        choice = input(prompt).upper()
    return choice

"""
LOADING SONGS
    list_of_song = list
    in_file = open songs.csv (r)
    for line in in_file
        song_artist_year_list = split line with ","
        list_of_song = append song_artist_year_list into the list
    return list_of_song
"""
#load songs from the csv file
def loading_songs():
    list_of_song = []
    for line in in_file:
        line = line.strip("\n")
        song_artist_year_list = line.split(",")
        list_of_song.append(song_artist_year_list)
    in_file.close()
    return list_of_song

#display the list of song
def display_songlist(list_of_song):
    count = 0
    for i in range(len(list_of_song)):
        if list_of_song[i][3] == "y":
            count += 1
            symbol = "*"
        else:
            symbol = " "
        print(" ", str(i) + ".", symbol, "", end="")
        for j in range(len(list_of_song[i]) - 2):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:40}".format(list_of_song[i][j]), end="")
        print("{:4}".format(list_of_song[i][-2]))
    print(len(list_of_song) - count, "songs learned,", count, "songs still to learn")

""" 
COMPLETED SONGS
completed_songs(list_of_song)
song_number = get_song_number("song number: ")
song_list[song_number][3] = "n"
print song_list[song_number][0]+"by"+song_list[song_number][1]+"learned"
return song_list
"""

#show the number of completed songs
def completed_songs(list_of_song):
    count = 0
    for i in range(len(list_of_song)):
        if list_of_song[i][3] == "y":
            count += 1
    if count == 0:
        print("No need to learn new songs.")

    print(len(list_of_song) - count, "songs learnt,", count, "songs still need to learn")
    songs = count_number("Enter the number of songs you want to learn\n:")
    if list_of_song[songs][3] == "n":
        print("You have already learned", list_of_song[songs][0])
    else:
        list_of_song[songs][3] = "n"
        print(list_of_song[songs][0], "by", list_of_song[songs][1], "learned")
        return list_of_song

#add songs to the list
def add_songs():
    input_song = []
    title = word_input("Title: ")
    artist = word_input("Artist: ")
    year = str(year_count("Year: "))
    input_song.append(title)
    input_song.append(artist)
    input_song.append(year)
    input_song.append("y")
    print(title, "by", artist, "({:4})".format(year), "added to the song list")
    return input_song

#get input for the songlist
def word_input(prompt):
    string_input = input(prompt)
    while len(string_input) == 0:
        print("This input can't be blank.")
        string_input = input(prompt)
    return string_input.title()

#check song
def count_number(prompt):
    valid = False
    while not valid:
        try:
            input_number = int(input(prompt))
            if input_number < 0:
                print("Number must be >= 0")
            elif input_number >= 7:
                print("Song number is not in the list")
            else:
                return input_number
        except ValueError:
            print("Enter a valid number.")


def year_count(prompt):
    valid = False
    while not valid:
        try:
            input_number = int(input(prompt))
            if input_number < 0:
                print("Number must be greater than 0")
            else:
                return input_number
        except ValueError:
            print("Invalid input; enter a valid number")

#save songs to the csv file
def final_saving_songs(list_of_song):
    final_file = open(file_name , 'w')
    for i in range(len(list_of_song)):
        if i != 0:
            print("\n", end="", file=final_file)
        for j in range(len(list_of_song[i])):
            final_file.write(list_of_song[i][j])
            if j != 3:
                print(",", end="", file= final_file)
    final_file.close()

def main():
    list_of_song = loading_songs()
    print(len(list_of_song), "songs loaded")
    choice_menu = main_menu()
    while choice_menu != "Q":
        list_of_song.sort(key=itemgetter(1, 0))
        if choice_menu == "C":
            completed_songs(list_of_song)
        elif choice_menu == "A":
            list_of_song.append(add_songs())
        else:
            display_songlist(list_of_song)
        choice_menu = main_menu()
    final_saving_songs(list_of_song)
    print(len(list_of_song), "songs saved to", file_name)


main()


