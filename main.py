import typer
import connect
from datetime import datetime

app = typer.Typer()
#forecast = typer.Typer()
#astronomy = typer.Typer()
#app.add_typer(forecast, name="forecast")
#app.add_typer(astronomy, name="astronomy")

# Get real-time current weather
@app.command()
def now(location: str = typer.Argument(None)):
    # Call API
    connect.get_now(location)

# Get today's weather forecast
@app.command()
def today(location: str):
    # Call API
    connect.get_real_time(location)

if __name__ == "__main__":
    app()