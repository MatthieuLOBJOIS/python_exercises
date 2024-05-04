import typer

def main(extension: str = typer.Argument(..., help="Extension à chercher")):
    """
    Affiche les fichiers trouvés avec l'extension données.
    """

    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")

if __name__ == "__main__":
    typer.run(main)