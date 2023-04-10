"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""

from pathlib import Path

path = Path.cwd()
file =  path / "prenoms.txt"
text = file.read_text()

new_file = (path / "prenoms_clean.txt")
new_file.touch()

first_name_list = text.split()
first_name_clean_list = [f.strip(",. ") for f in first_name_list]
new_first_name_list = [f"| {f}" for f in first_name_clean_list]
 
new_file.write_text("\n".join(new_first_name_list))