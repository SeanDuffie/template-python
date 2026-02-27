import typer
from project.logic import calculate_data

app = typer.Typer()

@app.command()
def compute(value: int):
    """CLI command to run a calculation."""
    result = calculate_data(value)
    print(f"The result is: {result}")
