from dash import Dash
from src import app as my_app

app = Dash(
    name = __name__,
    use_pages = False, # use Dash pages
    external_stylesheets = [],
    suppress_callback_exceptions = True,
    title = 'Spotivizzz'
)

app.layout = my_app.app_layout()

if __name__ == "__main__":
    app.run_server(
        debug = True
    )