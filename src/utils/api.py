import pandas as pd
import plotly.express as px
import pycountry_convert as pc

# Common data frames
#

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

# Data functions
#

def fake_bars_values():
    # Isolate countries names from playlists titles.
    # Exemple : From playlist "Top 50 - India" returns "India"
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Delete global playlist
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)

    popularity = topsData["popularity"].values.flatten().tolist()
    popularity.pop(0)

    df = pd.DataFrame({
        "Pays": countries_names,
        "Popularité":    popularity
    })
    return df

def fake_table_values(): # Return a tuple of headers/values
    headers = dict(values=[
        'Genre',
        'Popularité (%)',
        'Durée moyenne (min)'
    ])
    values = dict(values=[
        genresData["genre_name"],
        genresData["popularity"],
        genresData["average_duration"]
    ])
    return (headers, values)

def fake_map_values():
    # Isolate countries names from playlists titles.
    # Exemple : From playlist "Top 50 - India" returns "India"
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Delete global playlist
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)

    # Convert countries codes from countries names.
    countries_codes = []
    for i in range ( len(countries_names) ):
        country_code = pc.country_name_to_country_alpha3(countries_names[i], cn_name_format="default")
        countries_codes.append(country_code)

    # Convert countries names to continents names.
    continents_names = []
    for i in range ( len(countries_codes) ):
        country_alpha_2 = pc.country_alpha3_to_country_alpha2(countries_codes[i])
        continent_code = pc.country_alpha2_to_continent_code(country_alpha_2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        continents_names.append(continent_name)

    #Filter top artists for each countries
    top_artists = topsData["top_artist"].values.flatten().tolist()
    top_artists.pop(0)

    #Filter average BPM for each countries
    averages_BPM = topsData["average_BPM"].values.flatten().tolist()
    averages_BPM.pop(0)

    # Create data frame
    df = pd.DataFrame({
        "countries_codes":  countries_codes,
        "countries_names":  countries_names,
        "continents_names": continents_names,
        "top_artists":      top_artists,
        "averages_BPM":     averages_BPM
    })
    return df

def fake_duration_by_genre():
    df = pd.DataFrame({
        "Genre": genresData["genre_name"],
        "Durée": genresData["average_duration"]
    })
    return df

def fake_bpm_by_country():
    # Isolate countries names from playlists titles.
    # Exemple : From playlist "Top 50 - India" returns "India"
    playlist_titles = topsData["playlist_name"].values.flatten().tolist()
    playlist_titles.pop(0) # Delete global playlist
    countries_names = []
    for i in range ( len(playlist_titles) ):
        country_name = playlist_titles[i].replace("Top 50 - ", '')
        countries_names.append(country_name)

    bpm = topsData["average_BPM"].values.flatten().tolist()
    bpm.pop(0)

    df = pd.DataFrame({
        "Pays": countries_names,
        "BPM":  bpm
    })
    return df

def fake_loudness_by_energy():
    df = pd.DataFrame({
        "Volume": topsData["average_loudness"],
        "Energie": topsData["average_energy"]
    })
    return df