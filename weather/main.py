import typer
import connect

app = typer.Typer()

# Get real-time current weather
@app.command()
def now(location: str = typer.Argument(None)):
    # Call API
    connect.get_now(location)

# Get today's weather forecast
@app.command()
def today(location: str = typer.Argument(None)):
    # Call API
    connect.get_today(location)

# Get weather forecast for user requested length
@app.command()
def forecast(location: str = typer.Argument(None), num_days: str = typer.Argument(None)):
    print("forecast requested")
    # Call API
    connect.get_forecast(location, num_days)

if __name__ == "__main__":
    app()