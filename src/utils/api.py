import pandas as pd
import plotly.express as px

topsData = pd.DataFrame({
    "playlist_name":    ["Top 50 - Global", "Top 50 - France", "Top 50 - India", "Top 50 - Japan"],
    "popularity":       [90, 78, 79, 75],
    "average_duration": [3.14, 3.8, 3.31, 4.4],
    "average_BPM":      [124, 130, 112, 120],
    "average_loudness": [-7.7, -6.2, -7.0, -7.1],
    "average_energy":   [0.51, 0.623, 0.524, 0.451]
})

genresData = pd.DataFrame({
    "genre_name":    ["Rap", "Rock", "Hip Hop", "Trap Latino"],
    "popularity":       [90, 78, 79, 75],
    "average_duration": [3.14, 3.8, 3.31, 4.4]
})

def fake_bars_values():
    df = pd.DataFrame({
        "playlist_name": topsData["playlist_name"],
        "popularity": topsData["popularity"]
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

def fake_line_values():
    return px.data.gapminder().query("country=='Canada'")

def fake_pie_values():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 40.e6, 'country'] = 'Other countries' # Represent only large countries
    return df

def fake_map_values():
    df = px.data.gapminder().query("year==2007")
    return df

def fake_duration_by_genre():
    df = pd.DataFrame({
        "Genre": genresData["genre_name"],
        "Durée": genresData["average_duration"]
    })
    return df

def fake_bpm_by_country():
    df = pd.DataFrame({
        "Pays": topsData["playlist_name"],
        "BPM": topsData["average_BPM"]
    })
    return df

def fake_loudness_by_energy():
    df = pd.DataFrame({
        "Volume": topsData["average_loudness"],
        "Energie": topsData["average_energy"]
    })
    return df