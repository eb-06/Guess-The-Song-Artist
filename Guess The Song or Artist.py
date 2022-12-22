# Settings
gameSpeed = 1
artists = ["Kanye West", "Jay Z", "Raye", "Drake", "Soolking", "Sainte"]
songs = ["Bound 2", "Legacy", "All Of My Love", "Champagne Poetry", "Dalida", "Envy Me"]

"""
    How the game works:
    * The player gets to choose what game mode they wanna play.
        * 1 - Guess the song 
        * 2 - Guess the artist
    * The game goes on until the player guesses the artist/song incorrectly.
        * "gameSpeed" - Change how quickly the game moves on. (Seconds.)
        * "artists" - Change the artists to whoever relating to the songs.
        * "songs" - Change the songs to whatever relating to the artits.
            * Make sure the song/artist are alligned correctly next to their artist/song. Example:
                artists = ["0", "1", "2", "3"]
                songs = ["0", "1", "2", "3"]
    * The player gets to guess the song/artist twice.
        * If the player guesses the song/artist correct first go they get 2 points added to their score.
        * If the player guesses the song/artist correct second go they get 1 point added to their score.
        * If the player fails to the guess the song/artist correct after the 2 goes the game ends.
            * Each guess the first letter of each word of the song/artist is revealed.
"""

import random
import time

def cut(song, leftOver):
    if len(song) <= leftOver: return song
    else: return song[:-(len(song)-leftOver)]

def split(song, leftOver):
    splitWords = []
    for length in range(len(song.split())):
        splitWords.append(cut(song.split()[length], leftOver))
    return " ".join(splitWords)

def guess(addedPoints):
    global playerScore
    playerScore = playerScore + addedPoints
    print("Current score:", playerScore)
    time.sleep(gameSpeed)

gameMode = int(input("Which game mode would you like to play? Guess the song - 1 | Guess the artist - 2 : "))
playerScore = 0

while True:
    randomSelect = random.randint(0, (len(artists and songs) -1))
    selectedArtist = artists[randomSelect]
    selectedSong = songs[randomSelect]
    if gameMode == 1:
        print("Randomly selecting a song and its artist...")
        time.sleep(gameSpeed)
        print("The artist of the song is:", selectedArtist)
        print("First letter of each word in the song title:", split(selectedSong, 1))
        time.sleep(gameSpeed)
        playerGuess = input("First guess: ")
        if playerGuess == selectedSong: guess(3)
        else:
            print("Second letter of each word in the song title:", split(selectedSong, 2))
            time.sleep(gameSpeed)
            playerGuess = input("Second guess: ")
            if playerGuess == selectedSong: guess(1)
            else:
                print("The song was:", selectedSong)
                print("Score:", playerScore)
                break
    elif gameMode == 2:
        print("Randomly selecting an artist and their song...")
        time.sleep(gameSpeed)
        print("The song made by the artist is:", selectedSong)
        print("First letter of each word in the artist's name:", split(selectedArtist, 1))
        time.sleep(gameSpeed)
        playerGuess = input("First guess: ")
        if playerGuess == selectedArtist: guess(3)
        else:
            print("Second letter of each word in the artist's name:", split(selectedArtist, 2))
            time.sleep(gameSpeed)
            playerGuess = input("Second guess: ")
            if playerGuess == selectedArtist: guess(1)
            else:
                print("The artist was:", selectedArtist)
                print("Score:", playerScore)
                break
    else:
        print("Unknown game mode!")
        break
