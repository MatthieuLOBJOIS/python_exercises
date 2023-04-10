from pathlib import Path

path = Path.cwd()
valid_file = path / "readme.txt"
invalid_file = path / "fichier_invalide.abc"

print(50 * "-")
print(f"Chemin du fichier valide : {valid_file}")
print(f"Chemin du fichier invalide : {invalid_file}")
print(50 * "-")

file_path = Path(input("Entrez un fichier à ouvrir : "))

try : 
    file = open(file_path, "r")
    print(file.read())
except FileNotFoundError : 
    print("Le fichier n'a pas était trouvé.")
except UnicodeDecodeError : 
    print("Impossible d'ouvrir le fichier.")
else :
    file.close()