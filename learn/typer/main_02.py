import typer

def main():
    # prenom = typer.style("Patrick", fg=typer.colors.BLUE)
    # typer.echo(f"Bonjour {prenom}")

    typer.secho("Bonjour Patrick", bg=typer.colors.RED, bold=True)

if __name__ == "__main__":
    typer.run(main)