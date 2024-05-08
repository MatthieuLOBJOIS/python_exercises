import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_File = os.path.join(CUR_DIR, "data", "movies.json")

class Movie():
    def __init__(self, title = str):
        self.title = title.title()

    def __str__(self):
        return self.title()
    
    def _get_movies(self):
        with open(DATA_File, "r") as file:
            return json.load(file)

    def _write_movies(self, movies):
       with open(DATA_File, "w") as file:
            json.dump(movies, file, indent=4)

    def add_to_movies(self) -> bool:
       list_movies = self._get_movies()
       if self.title not in list_movies:
           list_movies.append(self.title)
           self._write_movies(list_movies)
           return True
       else:
            logging.warning(f"Le film {self.title} est déjà dans la liste.")
            return False
          

if __name__ == "__main__":
    m = Movie("harry potter")
    m.add_to_movies()
 
 
