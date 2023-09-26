# Spotify-As-Subtitles

Display Spotify Lyrics the same way Youtube Displays it's subtitles on Windows and Linux
<br>
<br>

![lyrics](https://github.com/NassimMansouri/Spotify-As-Subtitles/assets/123596322/c6e68864-6a88-4958-bf00-99b9964a370d)


# Setting up the script

## Getting your Client_ID, Client_Secret, Redirect_Uri :

<br>
1-Go to "https://developer.spotify.com/" and log-in
<br>
2-Go to the dashboard "https://developer.spotify.com/dashboard"
<br>
3-Create App and Fill the informations with what you want, For the "Redirect URI" put any link you want example "https://github.com/NassimMansouri/Spotify-Lyrics-to-Discord-Status"
<br>
4-Click Settings on the top right and it will show your client id and client secret the URI is the one you put above 
<br>

## Exporting Client_ID, Secret, URI

<br>
To set them permenantly : 
<br>
Open CMD and type : 
<br>

```

setx SPOTIPY_CLIENT_ID YourClientId /m
setx SPOTIPY_CLIENT_SECRET YourClientSecret /m
setx SPOTIPY_REDIRECT_URI YourURI /m

```

<br>
For Linux users: 

```

export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

```

<br>

# Installing requirements : 

Open cmd in the same directory as requirements.txt and type 
<br>

```
pip install -r requirements.txt
```


# Usage : 

Simply run "run.bat" file

For the first time running it you'll have to copy the redirected url into the cmd after that it'll work instantly.




