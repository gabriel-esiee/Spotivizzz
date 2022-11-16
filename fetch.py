import pandas as pd

def fetch_data():
    return pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 8],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })