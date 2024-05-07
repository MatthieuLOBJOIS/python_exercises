from pathlib import Path

chemin = Path.cwd()

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for key in d : 
    for f in d[key] : 
        (chemin / key).mkdir(exist_ok=True)
        if key == "Films" : 
         (chemin / key / f).mkdir(exist_ok=True)
        elif key == "Employes" : 
         (chemin / key / f).mkdir(exist_ok=True)
        elif key == "Exercices" : 
         (chemin / key / f).mkdir(exist_ok=True)