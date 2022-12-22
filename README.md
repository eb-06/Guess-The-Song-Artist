## How the game works:
  * The player gets to choose what game mode they wanna play.
    * `1` - Guess the song 
    * `2` - Guess the artist
  * The game goes on until the player guesses the artist/song incorrectly.
    * `gameSpeed` - Change how quickly the game moves on. (Seconds.)
    * `artists` - Change the artists to whoever relating to the songs.
    * `songs` - Change the songs to whatever relating to the artits.
      * Make sure the song/artist are alligned correctly next to their artist/song. Example:
          ```py
          artists = ["0", "1", "2", "3"]
          songs = ["0", "1", "2", "3"]
          ```
  * The player gets to guess the song/artist twice.
    * If the player guesses the song/artist correct first go they get 2 points added to their score.
    * If the player guesses the song/artist correct second go they get 1 point added to their score.
    * If the player fails to the guess the song/artist correct after the 2 goes the game ends.
      * Each guess the first letter of each word of the song/artist is revealed.
      
![Python](https://img.shields.io/badge/python-yellow?style=for-the-badge&logo=python&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/VisualㅤStudioㅤCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
