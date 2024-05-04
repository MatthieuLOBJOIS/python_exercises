import typer

def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str = typer.Argument(..., help="Extension à chercher")):
    """
    Affiche les fichiers trouvés avec l'extension données.
    """
    print(delete)
    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")

    if delete:
        confirm = typer.confirm("Souaitez vous supprimer les fichiers", abort=True)
        # if not confirm:
        #     typer.echo("Opération annulée.")
        #     raise typer.Abort()
    
    print("Suppression des fichiers.")


if __name__ == "__main__":
    typer.run(main)