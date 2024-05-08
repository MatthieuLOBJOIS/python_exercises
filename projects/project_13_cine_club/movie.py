import os
import json

CUR_DIR = os.path.dirname(__file__)
DATA_File = os.path.join(CUR_DIR, "data", "movies.json")
class Movie():
    def __init__(self, title = str):
        self.title = title.title

    def __str__(self):
        return self.title()
    
    def _get_movies(self):
        with open(DATA_File, "r") as file:
         return json.load(file)

    def _write_movies(self, movies):
       with open(DATA_File, "w") as file:
         json.dump(movies, file, indent=4)

if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)
    m._write_movies([
    "le seigneur des anneaux",
    "harry potter",
    "transformers",
    "jurassic park 2"])
    print(m._get_movies())
 
