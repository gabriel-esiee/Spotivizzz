# api.py est reponsable de la récupération des données sur la database Azure
# et de leur traitement.

import pandas as pd
import pycountry_convert as pc
import pypopulation as pp
from .azure_cosmos_db_linker import get_item_from_azure_database

# ID des databases stockés dans Cosmos DB:
id_top_playlists = "0f5cf919-3e2f-470c-a96c-8d64e1c56c51"
id_genre_playlists = "df6c4fcf-8cb1-4985-9002-aa80c483dc97"
id_everything_playlist = "e25741cc-bfe3-4fa6-b6c4-948d3410934c"

# Les dataframes finaux sont enregistrés dans des variables global ici
# pour pouvoir être ré-utilisés dans les fonctions des graphiques.

topsData = get_item_from_azure_database("spotivizzz", "top_playlist", id_top_playlists)
genresData = get_item_from_azure_database("spotivizzz", "genre_playlist", id_genre_playlists)
everythingData = get_item_from_azure_database("spotivizzz", "everything_playlist", id_everything_playlist)

# Les fonctions des graphiques sont définie ci-dessous.
# Chaque graphique a une fonction associé qui lui permets
# de recevoir les données nécéssaire dans le bon format.

# Graphique à barres popularité moyenne par pays.
def popularity_by_countries():
    """Get the popularity by countries data
    Returns:
        pandas DataFrame: Le dataFrame filtré pour l'utilisation de la fonction
    """
    # Récupération du nom du pays via le titre de la playlist.
    # Par exemple, la playlist "Top 50 - France" retourne "France"
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Suppression de la playlist mondiale car seul les pays nous intéressent.
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)
    
    # Conversion des noms des pays en code ISO.
    # Par exemple, si le pays "France" retourne "FRA".
    countries_codes = []
    for i in range ( len(countries_names) ):
        if(countries_names[i] == "UAE"):
            country_code = "ARE"
        else:
            country_code = pc.country_name_to_country_alpha3(countries_names[i], cn_name_format="default")
        
        countries_codes.append(country_code)
    
    # Countries Population
    population = []
    for country in countries_codes:
        if(country == 'TWN'):
            population.append(23570000)
        else:
            population.append(pp.get_population_a3(country))

    # Popularité.
    popularity = topsData["popularity"].values.flatten().tolist()
    popularity.pop(0)

    # Top Genres
    top_genres = topsData["top_genre"].values.flatten().tolist()
    top_genres.pop(0)

    genres = []

    for genre in top_genres:
        genre = genre.replace(" ", "-")
        words = genre.split("-")
        words = [word.capitalize() for word in words]
        genre = "-".join(words)
        genres.append(genre)

    # Popularity by Population
    popularity_by_population = []
    counter = 0
    for item in population:
        popularity_by_population.append(round(item*popularity[counter]/1000000000))
        counter +=1


    # Construction du dataframe.
    df = pd.DataFrame({
        "countries":  countries_names,
        "popularity": popularity,
        "population": population,
        "genre": genres,
        "popularity_by_population": popularity_by_population,
    })
    return df

# Graphique carte du monde.
def map_values():
    """Get the worldwide map data
    Returns:
        pandas DataFrame: Le dataFrame filtré pour l'utilisation de la fonction
    """
    # Récupération du nom du pays via le titre de la playlist.
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0)
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)

    # Conversion des noms des pays en code ISO.
    # Par exemple, si le pays "France" retourne "FRA".
    countries_codes = []
    for i in range ( len(countries_names) ):
        if(countries_names[i] == "UAE"):
            country_code = "ARE"
        else:
            country_code = pc.country_name_to_country_alpha3(countries_names[i], cn_name_format="default")
        
        countries_codes.append(country_code)

    # Conversion des noms des pays en nom de continent associés.
    continents_names = []
    for i in range ( len(countries_codes) ):
        country_alpha_2 = pc.country_alpha3_to_country_alpha2(countries_codes[i])
        continent_code = pc.country_alpha2_to_continent_code(country_alpha_2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        continents_names.append(continent_name)

    # Top artistes.
    top_artists = topsData["top_artist"].values.flatten().tolist()
    top_artists.pop(0)

    # BPM moyen.
    averages_BPM = topsData["average_BPM"].values.flatten().tolist()
    averages_BPM.pop(0)

    # Top Tracks
    top_tracks = topsData["top_track"].values.flatten().tolist()
    top_tracks.pop(0)

    # Top Tracks and Artists
    top_tracks_and_artists = topsData["top_track_and_artist"].values.flatten().tolist()
    top_tracks_and_artists.pop(0)

    # Average Duration
    average_duration = topsData["average_duration"].values.flatten().tolist()
    average_duration.pop(0)

    # Top Genres
    top_genres = topsData["top_genre"].values.flatten().tolist()
    top_genres.pop(0)

    # Average Formated Duration
    average_formated_duration = topsData["average_formated_duration"].values.flatten().tolist()
    average_formated_duration.pop(0)

    # Popularity
    popularity = topsData["popularity"].values.flatten().tolist()
    popularity.pop(0)

    # Construction du dataframe.
    df = pd.DataFrame({
        "countries_codes":           countries_codes,
        "countries_names":           countries_names,
        "continents_names":          continents_names,
        "top_artists":               top_artists,
        "averages_BPM":              averages_BPM,
        "top_tracks":                top_tracks,
        "top_tracks_and_artists":    top_tracks_and_artists,
        "average_duration":          average_duration,
        "average_formated_duration": average_formated_duration,
        "top_genre":                 top_genres,
        "popularity":                popularity,
    })
    return df

# Graphique à barres horizontales durée moyenne en fonction du genre.
def duration_by_genre():
    """Get the duration by genre data
    Returns:
        pandas DataFrame: Le dataFrame filtré pour l'utilisation de la fonction
    """
    #traitement des noms de genre
    genres = []

    for genre in genresData['genres']:
        genre = genre.replace("_", "-")
        words = genre.split("-")
        words = [word.capitalize() for word in words]
        genre = "-".join(words)
        genres.append(genre)
    
    # Construction du dataframe.
    df = pd.DataFrame({
        "genre":    genres,
        "duration": genresData["average_duration"],
        "formated_duration": genresData["average_formated_duration"],
    })
    return df

# Graphique à points bpm par pays.
def bpm_by_country():
    """Get the bpm by countries data
    Returns:
        pandas DataFrame: Le dataFrame filtré pour l'utilisation de la fonction
    """
    # Récupération du nom du pays via le titre de la playlist.
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Delete global playlist
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)
    
    # Conversion des noms des pays en code ISO.
    # Par exemple, si le pays "France" retourne "FRA".
    countries_codes = []
    for i in range ( len(countries_names) ):
        if(countries_names[i] == "UAE"):
            country_code = "ARE"
        else:
            country_code = pc.country_name_to_country_alpha3(countries_names[i], cn_name_format="default")
        
        countries_codes.append(country_code)

    # Conversion des noms des pays en nom de continent associés.
    continents_names = []
    for i in range ( len(countries_codes) ):
        country_alpha_2 = pc.country_alpha3_to_country_alpha2(countries_codes[i])
        continent_code = pc.country_alpha2_to_continent_code(country_alpha_2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        continents_names.append(continent_name)

    # BPM moyen.
    bpm = topsData["average_BPM"].values.flatten().tolist()
    bpm.pop(0)

    # Average Duration.
    duration = topsData["average_duration"].values.flatten().tolist()
    duration.pop(0)

    # Average Formated Duration
    formated_duration = topsData["average_formated_duration"].values.flatten().tolist()
    formated_duration.pop(0)

    # Countries Population
    population = []
    for country in countries_codes:
        if(country == 'TWN'):
            population.append(23570000)
        else:
            population.append(pp.get_population_a3(country))

    # Construction du dataframe.
    df = pd.DataFrame({
        "country":                   countries_names,
        "continents_names":          continents_names,
        "bpm":                       bpm,
        "duration":                  duration,
        "population":                population,
        "formated_duration":         formated_duration,
    })
    return df

# Graphique à points volume / energie.
def loudness_by_energy():
    """Get the loudness by energy data
    Returns:
        pandas DataFrame: Le dataFrame filtré pour l'utilisation de la fonction
    """

    top_genres = []
    genres = everythingData["genres"].values.flatten().tolist()
    for genrelist in genres:
        if len(genrelist) >0:
            genrelist[0] = genrelist[0].replace(" ", "-")
            words = genrelist[0].split("-")
            words = [word.capitalize() for word in words]
            genrelist[0] = "-".join(words)
            top_genres.append(genrelist[0])
        else:
            top_genres.append("no_genre_data")

    # Construction du dataframe.
    df = pd.DataFrame({
        "loudness": everythingData["loudness"],
        "energy": everythingData["energy"],
        "title_and_artist": everythingData["title_and_artist"],
        "genres": top_genres,
        "loudness_energy_ratio": (round((everythingData["loudness"]+100)* everythingData["energy"]))
    })
    return df


# Comparaison Genres
def dual_genre_comparaison():
    """Get the dual genre data
    Returns:
        pandas DataFrame: Le dataFrame filtré pour l'utilisation de la fonction
    """
    #traitement des noms de genre
    genres = []

    for genre in genresData['genres']:
        genre = genre.replace("_", "-")
        words = genre.split("-")
        words = [word.capitalize() for word in words]
        genre = "-".join(words)
        genres.append(genre)
    
    # Construction du dataframe.
    df = pd.DataFrame({
        "formated_genre":    genres,
        'genre': genresData["genres"],
        "duration": genresData["average_duration"],
        "formated_duration": genresData["average_formated_duration"],
        "bpm": genresData["average_BPM"],
        "key": genresData["top_key"],
        "danceability": genresData["average_danceability"],
        "energy":genresData["average_energy"],
        "speechiness":genresData["average_speechiness"],
        "acousticness":genresData["average_acousticness"],
        "instrumentalness":genresData["average_instrumentalness"],
        "liveness":genresData["average_liveness"],
        "valence":genresData["average_valence"],
    })
    return df