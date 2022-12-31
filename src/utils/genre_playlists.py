import datetime
import urllib.request
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import azure_cosmos_db_linker as cosmos_db
cid = 'bbdb43e42d854517a9a3699dabd72322'
secret = 'crypted-for-public-upload'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


## --- GENRES PLAYLISTS --- ##

genre_playlists_dict = {"pop": "https://open.spotify.com/playlist/6gS3HhOiI17QNojjPuPzqc?si=e624b70789dd4006",
                        "disco": "https://open.spotify.com/playlist/0ZVSWcJIf7cvycEn9HUvps?si=8030d4a556d34f0c",
                        "kpop": "https://open.spotify.com/playlist/3T1Rft817cZ3pguTvaWaz3?si=05915d4f695d4cf5",
                        "edm": "https://open.spotify.com/playlist/3pDxuMpz94eDs7WFqudTbZ?si=77497ef3c8af4a99",
                        "rock": "https://open.spotify.com/playlist/7dowgSWOmvdpwNkGFMUs6e?si=6d61c388a715428d",
                        "rap": "https://open.spotify.com/playlist/6s5MoZzR70Qef7x4bVxDO1?si=6655eb6ce1f74c78",
                        "dance_pop": "https://open.spotify.com/playlist/2ZIRxkFuqNPMnlY7vL54uK?si=74e2df1a45894363",
                        "hip_hop": "https://open.spotify.com/playlist/6MXkE0uYF4XwU4VTtyrpfP?si=bfac80236d264427",
                        "trap_latino": "https://open.spotify.com/playlist/7MIkj5EbBCaUutUBEfGpEJ?si=6b5012c7486b4791",
                        "post_teen_pop": "https://open.spotify.com/playlist/10FCW9lj0NdeoYI5VVvVtY?si=900a42e8760c4afe",
                        "r&b": "https://open.spotify.com/playlist/1rLnwJimWCmjp3f0mEbnkY?si=1ee15e31403b437d",
                        "reggaeton": "https://open.spotify.com/playlist/0VKCDh1qcRXjMfDhGEXihm?si=deea4d993cea4058",
                        "latin_pop": "https://open.spotify.com/playlist/5tRvNV4dHaAbqPORml4YFS?si=165bf0a82fc7442c",
                        "trap": "https://open.spotify.com/playlist/60SHtDyagDjPnUpC7x1UD9?si=407765447df842a0",
                        "tropical_house": "https://open.spotify.com/playlist/5Z4GsFxPRJiN9Qme2P9q6H?si=726c7803267b4041",
                        "electro_pop": "https://open.spotify.com/playlist/1BYospE2cLB28m3i84dcTV?si=3bcb3960c6c04081",
                        "nigerian_pop": "https://open.spotify.com/playlist/7MwdQNmdKjQx3h1p3vP2eZ?si=3934b56ce20040fa",
                        "emo": "https://open.spotify.com/playlist/4eC7Sa1Xcy33lKn53gfiZb?si=18a1f67510cc414f",
                        "country": "https://open.spotify.com/playlist/4mijVkpSXJziPiOrK7YX4M?si=d67e0686932e4c83",
                        "electro_house": "https://open.spotify.com/playlist/4luNnGhISZdURbFcCl2dB6?si=b39d930c931c4f03",
                        "metal": "https://open.spotify.com/playlist/3pBfUFu8MkyiCYyZe849Ks?si=dfb281a2803240df",
                        "soul": "https://open.spotify.com/playlist/1YUIw9n6voqxPzawnEf3A2?si=3d3fbd29f6204321",
                        "dark_trap": "https://open.spotify.com/playlist/1lEZC1rWlusGF0IC6JxR5V?si=02ff646f2d0b486d",
                        "funk": "https://open.spotify.com/playlist/0MBvtOIm5fuBbRHEltDY8A?si=9ff85342a67f49c3",
                        "rap_francais": "https://open.spotify.com/playlist/2k8s1T3zBIerxsGyA3cFeV?si=e4739448e87f4a50",
                        "candy_pop": "https://open.spotify.com/playlist/1g2P36W1Dn9CYyegAm7Z4x?si=7edd4d5c88494df2",
                        "punk": "https://open.spotify.com/playlist/17qQT0G3yFjOJ02wWZaNCw?si=2be4815212544d23",
                        "pop_rock": "https://open.spotify.com/playlist/1voR0tqN6ZFkQ9QABvbCkZ?si=041f103f97d3437f",
                        "alternative_metal": "https://open.spotify.com/playlist/0zJrEnj3O8CohOpFFUVSo9?si=f48e99be9bd0447e",
                        "urbano_latino": "https://open.spotify.com/playlist/1kfJj9rUlOGawu2U1U4oZn?si=9d3888ab7fb146c9",
                        "modern_rock": "https://open.spotify.com/playlist/5HufsVvMDoIPr9tGzoJpW0?si=bdcfeebc63574243",
                        "mexican_pop": "https://open.spotify.com/playlist/4sghNjSZeUx5DFTADuPhPj?si=fe23730695da4ec0",
                        "lounge": "https://open.spotify.com/playlist/7jk0EKyr4Lc4jc4XPE4ycL?si=814de58cc53b4465",
                        "house" : "https://open.spotify.com/playlist/6AzCASXpbvX5o3F8yaj1y0?si=aa6455ce2c5a4872",
                        "post_grunge": "https://open.spotify.com/playlist/60NgGlktCblheYPBSSUUXz?si=bfbb25f2b25d47f2",
                        "classical": "https://open.spotify.com/playlist/3HYK6ri0GkvRcM6GkKh0hJ?si=dd4f193704bc4117",
                        "garage_rock": "https://open.spotify.com/playlist/4Wnjv0bnb6Y7Il7WhEJC3x?si=f3c0dd3f25254bdd",
                        "drift_phonk": "https://open.spotify.com/playlist/19sgQqGAcGplazJZTXeLUG?si=8daf95c66a53476b",
                        "french_pop": "https://open.spotify.com/playlist/03csHhetcFo29YHV4Z9A3g?si=c699da3323e544de",
                        "hyperpop": "https://open.spotify.com/playlist/7DrJ92Lc9UaVB1rKM2UGsg?si=6ec77aa98f354f34",
                        "vaporwave": "https://open.spotify.com/playlist/4XyF8NB0VN7XR5rDHL2lMG?si=8f61ed0a37954b56",
                        }

## retrieves the playlist URI from a playlist link
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



# get the data from a genre playlist link as a panda DataFrame
def get_genre_playlist_data(playlist_link):
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
    release_years = []
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

    columns = {"trackID": IDs,
                "title": titles,
                "artist": artists,
                "popularity": popularities,
                "release_year": release_years,
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
        titles.append(track["track"]["name"])
        artists.append(track["track"]["artists"][0]["name"])
        popularities.append(track["track"]["popularity"])
        try:
            release_years.append(int(track["track"]["release_date"].split('-', 1)[0]))
        except:
            release_years.append(2022)
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

    current_genre_playlist_data = pd.DataFrame(columns)
    return current_genre_playlist_data


def get_genres_playlists_data(genre_playlists_dict):
    """Get the Data from multiple Playlists

    Args:
        top_playlists_links_list (list): list of the playlists to analyse

    Returns:
        pandas DataFrame: The average Data of each playlist
    """
    genre_playlists_links_list = genre_playlists_dict.values()

    genre_names = genre_playlists_dict.keys()
    popularities = []
    average_release_years = []
    average_durations = []
    average_formated_durations = []
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

    columns = {"genres": genre_names,
                "popularity": popularities,
                "average_release_year": average_release_years,
                "average_duration": average_durations,
                "average_formated_duration": average_formated_durations,
                "average_BPM": average_BPMs,
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

    for top_playlist_link in genre_playlists_links_list:
        try:
            top_playlist_name = get_playlist_name(top_playlist_link)
            print(f"Trying to fetch data of: {top_playlist_name}")
            top_playlist_data = get_genre_playlist_data(top_playlist_link)

            popularities.append(round(top_playlist_data["popularity"].mean()))
            average_release_years.append(round(top_playlist_data["release_year"].mean()))
            average_formated_durations.append(str(datetime.timedelta(seconds= round(top_playlist_data["duration_s"].mean()))))
            average_durations.append(round(top_playlist_data["duration_s"].mean()))
            average_BPMs.append(round(top_playlist_data["BPM"].mean()))
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

            top_keys.append(top_playlist_data["key"].value_counts().index[0])
            print(f"✅ Successfully fetched data of: {top_playlist_name}")
        except:
            print(f"❌ Couldn't fetch data of: {top_playlist_name}")
    
    current_top_playlists_data = pd.DataFrame(columns)
    return current_top_playlists_data

test_genre_playlists_dict = {
                        "french_pop": "https://open.spotify.com/playlist/03csHhetcFo29YHV4Z9A3g?si=c699da3323e544de",
                        "hyperpop": "https://open.spotify.com/playlist/7DrJ92Lc9UaVB1rKM2UGsg?si=6ec77aa98f354f34",
                        "vaporwave": "https://open.spotify.com/playlist/4XyF8NB0VN7XR5rDHL2lMG?si=8f61ed0a37954b56",
                        }

genre_data = get_genres_playlists_data(genre_playlists_dict)
print(genre_data)

genre_playlist_cosmos_db_id = "df6c4fcf-8cb1-4985-9002-aa80c483dc97"
database_name = "spotivizzz"
container_name = "genre_playlist"

cosmos_db.replace_item_in_azure_data_base(genre_playlist_cosmos_db_id, genre_data, database_name, container_name)