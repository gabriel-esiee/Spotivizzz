# Run this app with `python main.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from src import fetch
from src import dashboard

datas = fetch.fetch_data()
dashboard.build_main_layout(datas)

if __name__ == '__main__':
    dashboard.start()
