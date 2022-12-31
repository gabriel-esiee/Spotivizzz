import urllib.request
import spotipy
import pandas as pd
import datetime
from spotipy.oauth2 import SpotifyClientCredentials
import azure_cosmos_db_linker as cosmos_db
cid = 'bbdb43e42d854517a9a3699dabd72322'
secret = 'crypted-for-public-upload'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



def get_playlist_URI(playlist_link):
    """Retrieves the playlist URI from a spotify playlist link

    Args:
        playlist_link (str): the link of the spotify playlist

    Returns:
        str: the URI of the spotify playlist
    """
    return playlist_link.split("/")[-1].split("?")[0]

def get_playlist_name(playlist_link):
    """Retrieves the name of a spotify playlist from its sharing link

    Args:
        playlist_link (str): the link of the spotify playlist

    Returns:
        str: the name of the playlist
    """
    return sp.playlist(get_playlist_URI(playlist_link))["name"]

def get_artist_id(artist_link):
    """Get the ID of an artist from its sharing link

    Args:
        artist_link (str): sharing link of an artist page

    Returns:
        str: the id of the artist page
    """
    return artist_link.split("/")[-1].split("?")[0]

def get_artist_genres(artist_link):
    """Retrieves the list of genres an artist is associated with

    Args:
        artist_link (str): sharing link of an artist

    Returns:
        str[]: The list of the genres the artist is associated with
    """
    return sp.artist(get_artist_id(artist_link))["genres"]

def get_artist_genres_from_id(artist_id):
    """Retrieves the list of genres an artist is associated with

    Args:
        artist_id (str): the artist ID

    Returns:
        str[]: The list of the genres the artist is associated with
    """
    return sp.artist(artist_id)["genres"] 

def get_playlist_tracks(playlist_link):
    """Get all the tracks of a playlist even if it has more than 100 tracks

    Args:
        playlist_link (str): The playlist share link

    Returns:
        json: the Spotify API response with infos about tracks as JSON
    """
    playlist_URI = get_playlist_URI(playlist_link)
    results = sp.playlist_tracks(playlist_URI)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def get_tracks_popularity(tracks):
    """Get the average popularity of a track list

    Args:
        tracks (list): the track list

    Returns:
        int: the popularity (between 0 and 100)
    """
    tracks_popularity = 0
    track_counter = 0
    for track in tracks:
        track_pop = track["track"]["popularity"]
        tracks_popularity += track_pop
        track_counter += 1
    tracks_popularity = round(tracks_popularity/(track_counter-1))
    return tracks_popularity

# retrives the star emoji ranking from a scale from 0 to 100
def pop_emoji(track_pop):
    """Transform a popularity score into a out of five stars rating

    Args:
        track_pop (int): the popularity

    Returns:
        str: the five star rating
    """
    if track_pop < 10:
        return "⭐"
    elif track_pop < 30:
        return "⭐⭐"
    elif track_pop < 60:
        return "⭐⭐⭐"
    elif track_pop < 90:
        return "⭐⭐⭐⭐"
    elif track_pop <= 100:
        return "⭐⭐⭐⭐⭐"

## dictionnary to convert spotify key numbers to real life music keys
key_conversion_dic =   {0: "C", 
                        1: "C♯/D♭",
                        2: "D",
                        3: "D♯/E♭",
                        4: "E",
                        5: "F",
                        6: "F♯/G♭",
                        7: "G",
                        8: "G♯/A♭",
                        9: "A",
                        10: "A♯/B♭",
                        11: "B"}


## TOP WORLDWIDE PLAYLISTS
top_50_world_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=d37902778eea45d9"

top_50_south_africa_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMH2jvi6jvjk?si=ae867aced3d54c28"
top_50_germany_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJiZcmkrIHGU?si=431ab926214a4806"
top_50_saudi_arabia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLrQBcXqUtaC?si=106d8be2cd9a4520"
top_50_argentina_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMMy2roB9myp?si=2cf5c0f3fd2f49da"
top_50_australia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJPcfkRz0wJ0?si=c1e83b8938e84131"
top_50_austria_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKNHh6NIXu36?si=1aecef614e194900"
top_50_belgium_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJNSeeHswcKB?si=84554e568de54805"
top_50_belarus_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbIYfjSLbWr4V?si=b5cb1f737362444d"
top_50_bolivia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJqfMFK4d691?si=d997dd4a5fb143ce"
top_50_brazil_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMXbN3EUUhlg?si=5d19c25571624737"
top_50_bulgaria_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNfM2w2mq1B8?si=70068c3a50fb4396"
top_50_canada_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKj23U1GF4IR?si=df8a5ca5fa6247e8"
top_50_chile_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbL0GavIqMTeb?si=61b27083babb4803"
top_50_colombia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbOa2lmxNORXQ?si=f30ae8d2f65b4c9c"
top_50_south_korea_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNxXF4SkHj9F?si=297102cd0d14466d"
top_50_costa_rica_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMZAjGMynsQX?si=1fb76ae3705344c3"
top_50_denmark_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbL3J0k32lWnN?si=c71a3718f7ad4250"
top_50_spain_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNFJfN1Vw8d9?si=e62d73272fe34546"
top_50_estonia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLesry2Qw2xS?si=59e97c2379464fa0"
top_50_finland_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMxcczTSoGwZ?si=4cb7b5b7d7ff4547"
top_50_france_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbIPWwFssbupI?si=c417d0d75b4f4479"
top_50_greece_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJqdarpmTJDL?si=b8446dabc48b406a"
top_50_guatemala_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLy5tBFyQvd4?si=1e99a90785954b72"
top_50_honduras_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJp9wcIM9Eo5?si=e0f4a348367943fd"
top_50_hong_kong_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLwpL8TjsxOG?si=796912723ce2408a"
top_50_hungary_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNHwMxAkvmF8?si=2cf3b500a3194d17"
top_50_india_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg?si=79beb8c4328f4599"
top_50_indonesia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbObFQZ3JLcXt?si=b97edbfea5fa45c7"
top_50_ireland_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKM896FDX8L1?si=3879df73debe4fa2"
top_50_iceland_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKMzVsSGQ49S?si=57bd15625a664b16"
top_50_israel_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJ6IpvItkve3?si=228f4157e73e4555"
top_50_italia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbIQnj7RRhdSX?si=6a674a7d24674e10"
top_50_japan_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKXQ4mDTEBXq?si=dcb33d123e8a42e2"
top_50_kazakhstan_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbM472oKPNKzS?si=b524c9adce5e4a39"
top_50_latvia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJWuzDrTxbKS?si=b94f4f9173cb4ae4"
top_50_lithuania_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMx56Rdq5lwc?si=bb64a1d245944833"
top_50_luxembourg_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKGcyg6TFGx6?si=14cd4a98bdd0459c"
top_50_malaysia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJlfUljuZExa?si=0b7c2dc586d14a4a"
top_50_morocco_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJU9eQpX8gPT?si=084df7e2e7ba45bb"
top_50_mexico_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbO3qyFxbkOE1?si=60f42aaa85704593"
top_50_nicaragua_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbISk8kxnzfCq?si=768b63ac8271407c"
top_50_nigeria_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKY7jLzlJ11V?si=d611cc1232094a2d"
top_50_norway_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJvfa0Yxg7E7?si=d502b703618049db"
top_50_new_zealand_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbM8SIrkERIYl?si=a87f97bcc5e74060"
top_50_pakistan_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJkgIdfsJyTw?si=f28e3e77844e4ae5"
top_50_panama_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKypXHVwk1f0?si=6aa701008cb54f71"
top_50_paraguay_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNOUPGj7tW6T?si=64d6015c8d4f4f67"
top_50_netherlands_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKCF6dqVpDkS?si=fc28325a2ae0481b"
top_50_philippines_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNBz9cRCSFkY?si=ee21faf81e514ac7"
top_50_poland_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbN6itCcaL3Tt?si=02fa01fd6b544512"
top_50_portugal_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKyJS56d1pgi?si=f0fd21d92cac48aa"
top_50_peru_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJfdy5b0KP7W?si=c68ead53962e4391"
top_50_romania_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNZbJ6TZelCq?si=090b9293c2ff4341"
top_50_uk_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLnolsZ8PSNw?si=f1138d69b97a4fb4"
top_50_dominican_republic_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKAbrMR8uuf7?si=274e03ca25614044"
top_50_czech_republic_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbIP3c3fqVrJY?si=d7b23a4409354ceb"
top_50_el_salvador_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLxoIml4MYkT?si=41a2afc3d21b4a21"
top_50_singapore_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbK4gjvS1FjPY?si=869e438215064979"
top_50_slovakia_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKIVTPX9a2Sb?si=32dd36e98407490c"
top_50_switzerland_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJiyhoAPEfMK?si=5a97b7d22e324965"
top_50_sweden_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLoATJ81JYXz?si=d1902f3ef4d949f0"
top_50_taiwan_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMnZEatlMSiu?si=302da464693e451c"
top_50_thailand_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMnz8KIWsvf9?si=b6f44b60873e4516"
top_50_turkey_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbIVYVBNw9D5K?si=6b07602525df4328"
top_50_ukraine_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKkidEfWYRuD?si=f45955cf966d4b70"
top_50_uruguay_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMJJi3wgRbAy?si=63942b3c2cbd4584"
top_50_venezuela_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNLrliB10ZnX?si=1e38ccd80f3d429a"
top_50_vietnam_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLdGSmz6xilI?si=3224080acd09412a"
top_50_egypt_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLn7RQmT5Xv2?si=754f1b88bc064977"
top_50_united_emirates_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbM4UZuIrvHvA?si=5ecce907d0564b47"
top_50_ecuador_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbJlM6nvL1nD1?si=b8790e67fd1646e3"
top_50_usa_playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp?si=97f2037ffbda4f4b"


# get the data from a playlist link as a panda DataFrame
def get_playlist_data(playlist_link):
    """Get all the Data of a playlist

    Args:
        playlist_link (str): the playlist share link

    Returns:
        pandas DataFrame: The ordered data of each track of the playlist
    """

    IDs = []
    titles = []
    artists = []
    popularities = []
    durations = []
    BPMs = []
    loudnesses = []
    keys = []
    danceabilities = []
    energies = []
    speechinesses = []
    acousticnesses = []
    instrumentalnesses = []
    livenesses = []
    valences = []
    artist_genres_lists = []
    titles_and_artists = []

    columns = {"trackID": IDs,
                "title": titles,
                "artist": artists,
                "title_and_artist": titles_and_artists,
                "popularity": popularities,
                "genres": artist_genres_lists,
                "BPM": BPMs,
                "duration_s": durations,
                "loudness": loudnesses,
                "key": keys,
                "danceability": danceabilities,
                "energy": energies,
                "speechiness": speechinesses,
                "acousticness": acousticnesses,
                "instrumentalness": instrumentalnesses,
                "liveness": livenesses,
                "valence": valences}

    tracklist = get_playlist_tracks(playlist_link)
    for track in tracklist:
        id = track["track"]["id"]
        
        IDs.append(id)
        title = track["track"]["name"]
        titles.append(title)
        artist = track["track"]["artists"][0]["name"]
        artists.append(artist)
        titles_and_artists.append(f"{title} - {artist}")
        popularities.append(track["track"]["popularity"])
        artist_genres_lists.append(get_artist_genres_from_id( track["track"]["artists"][0]["id"]))
        #artist_genres_lists.append(["edm"])
        
        durations.append(round(track["track"]["duration_ms"]/1000))
        audio_features = sp.audio_features(id)
        try: BPMs.append(round(audio_features[0]["tempo"]))
        except: BPMs.append(120)
        try: loudnesses.append(audio_features[0]["loudness"])
        except: loudnesses.append(0.5)
        try: danceabilities.append(audio_features[0]["danceability"])
        except: loudnesses.append(0.5)
        try: energies.append(audio_features[0]["energy"])
        except: energies.append(0.5)
        try: speechinesses.append(audio_features[0]["speechiness"])
        except: speechinesses.append(0.5)
        try: acousticnesses.append(audio_features[0]["acousticness"])
        except: acousticnesses.append(0.5)
        try: instrumentalnesses.append(audio_features[0]["instrumentalness"])
        except: instrumentalnesses.append(0.5)
        try: livenesses.append(audio_features[0]["liveness"])
        except: livenesses.append(0.5)
        try: valences.append(audio_features[0]["valence"])
        except: valences.append(0.5)
        

        try: 
            key = audio_features[0]["key"]
            mode = audio_features[0]["mode"]
            if (key != -1):
                converted_key = key_conversion_dic[key]
                if(mode == 0): converted_key += ' Minor'
                else: converted_key += ' Major'
            else:
                converted_key = "not found"
            keys.append(converted_key)
        except: keys.append(key_conversion_dic[0] + ' Major')

    current_playlist_data = pd.DataFrame(columns)
    return current_playlist_data

## --------------------------------------------------------------

def get_top_playlists_data(top_playlists_links_list):
    """Get the Data from multiple Playlists

    Args:
        top_playlists_links_list (list): list of the playlists to analyse

    Returns:
        pandas DataFrame: The average Data of each playlist
    """
    playlists_names = []
    popularities = []
    average_durations = []
    average_formated_durations = []
    top_artists = []
    top_tracks = []
    top_tracks_and_artists = []
    average_BPMs = []
    average_loudnesses = []
    top_keys = []
    most_represented_artists = []
    average_danceabilities = []
    average_energies = []
    average_speechinesses = []
    average_acousticnesses = []
    average_instrumentalnesses = []
    average_livenesses = []
    average_valences = []
    top_genres = []

    columns = {"playlist_name": playlists_names,
                "popularity": popularities,
                "average_duration": average_durations,
                "average_formated_duration": average_formated_durations,
                "top_artist": top_artists,
                "top_genre": top_genres,
                "average_BPM": average_BPMs,
                "top_track": top_tracks,
                "top_track_and_artist": top_tracks_and_artists,
                "average_loudness": average_loudnesses,
                "top_key": top_keys,
                "most_represented_artist": most_represented_artists,
                "average_danceability": average_danceabilities,
                "average_energy": average_energies,
                "average_speechiness": average_speechinesses,
                "average_acousticness": average_acousticnesses,
                "average_instrumentalness": average_instrumentalnesses,
                "average_liveness": average_livenesses,
                "average_valence": average_valences}

    genres_dict = {}

    for top_playlist_link in top_playlists_links_list:
        top_playlist_data = get_playlist_data(top_playlist_link)
        top_playlist_name = get_playlist_name(top_playlist_link)
        print(f"Trying to fetch data of: {top_playlist_name}")

        playlists_names.append(top_playlist_name)
        popularities.append(round(top_playlist_data["popularity"].mean()))
        average_durations.append(round(top_playlist_data["duration_s"].mean()))
        average_formated_durations.append(str(datetime.timedelta(seconds = round(top_playlist_data["duration_s"].mean()))))
        top_artist = top_playlist_data["artist"][0]
        top_artists.append(top_artist)
        average_BPMs.append(round(top_playlist_data["BPM"].mean()))
        top_track = top_playlist_data["title"][0]
        top_tracks.append(top_track)
        top_tracks_and_artists.append(f"{top_track} - {top_artist}")
        average_loudnesses.append(top_playlist_data["loudness"].mean())
        average_danceabilities.append(top_playlist_data["danceability"].mean())
        average_energies.append(top_playlist_data["energy"].mean())
        average_speechinesses.append(top_playlist_data["speechiness"].mean())
        average_acousticnesses.append(top_playlist_data["acousticness"].mean())
        average_instrumentalnesses.append(top_playlist_data["instrumentalness"].mean())
        average_livenesses.append(top_playlist_data["liveness"].mean())
        average_valences.append(top_playlist_data["valence"].mean())

        most_represented_artist = top_playlist_data["artist"].value_counts()
        most_represented_artist_name = most_represented_artist.index[0]
        most_represented_artist_frequency = most_represented_artist[0]
        most_represented_artists.append(f"{most_represented_artist_name} ({most_represented_artist_frequency} tracks)")

        #updating genres dict:
        df_exploded = top_playlist_data.explode("genres")

        genre_counts = df_exploded["genres"].value_counts()
        genre_counts = genre_counts.sort_values(ascending=False)
        most_common_genre = genre_counts.index[0]

        top_genres.append(most_common_genre)

        top_keys.append(top_playlist_data["key"].value_counts().index[0])
        print(f"✅ Successfully fetched data of: {top_playlist_name}")
    
    current_top_playlists_data = pd.DataFrame(columns)
    return current_top_playlists_data

top_playlists_link_list = [ top_50_south_africa_playlist_link,
                            top_50_germany_playlist_link,
                            top_50_saudi_arabia_playlist_link,
                            top_50_argentina_playlist_link,
                            top_50_australia_playlist_link,
                            top_50_austria_playlist_link,
                            top_50_belgium_playlist_link,
                            top_50_belarus_playlist_link,
                            top_50_bolivia_playlist_link,
                            top_50_brazil_playlist_link,
                            top_50_bulgaria_playlist_link,
                            top_50_canada_playlist_link,
                            top_50_chile_playlist_link,
                            top_50_colombia_playlist_link,
                            top_50_south_korea_playlist_link,
                            top_50_costa_rica_playlist_link,
                            top_50_denmark_playlist_link,
                            top_50_spain_playlist_link,
                            top_50_estonia_playlist_link,
                            top_50_finland_playlist_link,
                            top_50_france_playlist_link,
                            top_50_greece_playlist_link,
                            top_50_guatemala_playlist_link,
                            top_50_honduras_playlist_link,
                            top_50_hong_kong_playlist_link,
                            top_50_hungary_playlist_link,
                            top_50_india_playlist_link,
                            top_50_indonesia_playlist_link,
                            top_50_ireland_playlist_link,
                            top_50_iceland_playlist_link,
                            top_50_israel_playlist_link,
                            top_50_italia_playlist_link,
                            top_50_japan_playlist_link,
                            top_50_kazakhstan_playlist_link,
                            top_50_latvia_playlist_link,
                            top_50_lithuania_playlist_link,
                            top_50_luxembourg_playlist_link,
                            top_50_malaysia_playlist_link,
                            top_50_mexico_playlist_link,
                            top_50_nicaragua_playlist_link,
                            top_50_nigeria_playlist_link,
                            top_50_norway_playlist_link,
                            top_50_new_zealand_playlist_link,
                            top_50_pakistan_playlist_link,
                            top_50_panama_playlist_link,
                            top_50_paraguay_playlist_link,
                            top_50_netherlands_playlist_link,
                            top_50_philippines_playlist_link,
                            top_50_poland_playlist_link,
                            top_50_portugal_playlist_link,
                            top_50_peru_playlist_link,
                            top_50_romania_playlist_link,
                            top_50_uk_playlist_link,
                            top_50_dominican_republic_playlist_link,
                            top_50_czech_republic_playlist_link,
                            top_50_el_salvador_playlist_link,
                            top_50_singapore_playlist_link,
                            top_50_slovakia_playlist_link,
                            top_50_switzerland_playlist_link,
                            top_50_sweden_playlist_link,
                            top_50_taiwan_playlist_link,
                            top_50_thailand_playlist_link,
                            top_50_turkey_playlist_link,
                            top_50_ukraine_playlist_link,
                            top_50_uruguay_playlist_link,
                            top_50_venezuela_playlist_link,
                            top_50_vietnam_playlist_link,
                            top_50_egypt_playlist_link,
                            top_50_united_emirates_playlist_link,
                            top_50_ecuador_playlist_link,
                            top_50_usa_playlist_link
                          ]

top_playlists_data = get_top_playlists_data(top_playlists_link_list)

top_playlist_cosmos_db_id = "0f5cf919-3e2f-470c-a96c-8d64e1c56c51"
database_name = "spotivizzz"
container_name = "top_playlist"

cosmos_db.replace_item_in_azure_data_base(top_playlist_cosmos_db_id, top_playlists_data, database_name, container_name)