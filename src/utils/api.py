# api.py est reponsable de la récupération des données
# et de leurs traitement.

import pandas as pd
import pycountry_convert as pc

# Les dataframes finaux sont enregistrés dans des variables global ici
# pour pouvoir être ré-utilisés dans les fonctions des graphiques.

topsData = pd.DataFrame({
    "playlist_name":    ["Top 50 - Global", "Top 50 - France", "Top 50 - India", "Top 50 - Japan"],
    "popularity":       [90, 78, 79, 75],
    "average_duration": [3.14, 3.8, 3.31, 4.4],
    "average_BPM":      [124, 130, 112, 120],
    "average_loudness": [-7.7, -6.2, -7.0, -7.1],
    "average_energy":   [0.51, 0.623, 0.524, 0.451],
    "top_artist":       ["The Weeknd", "Gazo", "Michael Jackson", "BB Jacques"]
})

genresData = pd.DataFrame({
    "genre_name":    ["Rap", "Rock", "Hip Hop", "Trap Latino"],
    "popularity":       [90, 78, 79, 75],
    "average_duration": [3.14, 3.8, 3.31, 4.4]
})

# Les fonctions des graphiques sont définie ci-dessous.
# Chaque graphique a une fonction associé qui lui permets
# de recevoir les données nécéssaire dans le bon format.

# Graphique à barres popularité moyenne par pays.
def fake_popularity_by_countries():
    # Récupération du nom du pays via le titre de la playlist.
    # Par exemple, la playlist "Top 50 - France" retourne "France".
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Suppression de la playlist mondiale car seul les pays nous intéressent.
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)

    # Popularité.
    popularity = topsData["popularity"].values.flatten().tolist()
    popularity.pop(0)

    # Construction du dataframe.
    df = pd.DataFrame({
        "countries":  countries_names,
        "popularity": popularity
    })
    return df

# Graphique carte du monde.
def fake_map_values():
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

    # Construction du dataframe.
    df = pd.DataFrame({
        "countries_codes":  countries_codes,
        "countries_names":  countries_names,
        "continents_names": continents_names,
        "top_artists":      top_artists,
        "averages_BPM":     averages_BPM
    })
    return df

# Graphique à barres horizontales durée moyenne en fonction du genre.
def fake_duration_by_genre():
    # Construction du dataframe.
    df = pd.DataFrame({
        "genre":    genresData["genre_name"],
        "duration": genresData["average_duration"]
    })
    return df

# Graphique à points bpm par pays.
def fake_bpm_by_country():
    # Récupération du nom du pays via le titre de la playlist.
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Delete global playlist
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)

    # BPM moyen.
    bpm = topsData["average_BPM"].values.flatten().tolist()
    bpm.pop(0)

    # Construction du dataframe.
    df = pd.DataFrame({
        "Pays": countries_names,
        "BPM":  bpm
    })
    return df

# Graphique à points volume / energie.
def fake_loudness_by_energy():
    # Construction du dataframe.
    df = pd.DataFrame({
        "loudness": topsData["average_loudness"],
        "energy": topsData["average_energy"]
    })
    return df