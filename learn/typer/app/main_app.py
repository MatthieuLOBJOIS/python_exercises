import typer
from typing import Optional
from pathlib import Path

def main(extension: str, 
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés.")):
    
    """Affiche les fichiers trouvés avec l'extension donnée.
    """

    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()

    if not directory.exists():
        typer.secho(f"Le dossier {directory} n'existe pas.", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")
    if delete:
        typer.confirm("Voulez-vous vraiment supprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Fichier : {file} supprimé", fg=typer.colors.RED)
    else:
        for file in files:
            typer.secho(f"Fichier : {file} trouvé", fg=typer.colors.BLUE)
        
if __name__ == "__main__":
    typer.run(main)