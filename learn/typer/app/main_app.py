import typer
from typing import Optional

def main(extension: str, 
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés.")):
    
    """Affiche les fichiers trouvés avec l'extension donnée.
    """

    print(extension, directory, delete)

if __name__ == "__main__":
    typer.run(main)