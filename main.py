import typer
import connect
from datetime import datetime

app = typer.Typer()
forecast = typer.Typer()
astronomy = typer.Typer()
app.add_typer(forecast, name="forecast")
app.add_typer(astronomy, name="astronomy")

# Get real-time weather
@app.command()
def today(location: str):
    # Make API call
    connect.get_real_time(location)
    # Parse data from API

    # Display nicely

if __name__ == "__main__":
    app()
