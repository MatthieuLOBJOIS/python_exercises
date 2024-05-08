class Movie():
    def __init__(self, movie_name = str):
        #self.set_movie_name(movie_name)
        self.title = movie_name.title()

    def __str__(self):
        return self.title
    
    # def set_movie_name(self, movie_name = str) -> str:
    #     """_summary_

    #     Args:
    #         movie_name (str)

    #     Returns:
    #         str: returns the name of the film with the first character of each word capitalized
    #     """
    #     word_list_upper_first_character = [word.replace(word[0], word[0].upper()) for word in movie_name.split(" ")]
    #     movie_name_modified = " ".join(word_list_upper_first_character)
    #     print(movie_name_modified)

if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)