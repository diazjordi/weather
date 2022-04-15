import typer
import connect

app = typer.Typer()


@app.command()
def hello():
    print("There is weather")


if __name__ == "__main__":
    app()
