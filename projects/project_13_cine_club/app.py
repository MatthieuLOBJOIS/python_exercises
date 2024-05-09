from PySide2 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.resize(500, 800) 
        self.setup_connection()
        self.populate_movies()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_removeMovies)

    def setup_connection(self):
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        
        m = Movie(title=movie_title)
        result = m.add_to_movies()

        if result:
            lw_item = QtWidgets.QListWidgetItem(m.title)
            lw_item.setData(QtCore.Qt.UserRole, m)
            self.lw_movies.addItem(lw_item)
            
        self.le_movieTitle.setText("")

    def remove_movie(self):
        print("On supprime un film")


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
