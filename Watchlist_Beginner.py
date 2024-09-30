class Movies:
    def __init__(self, name, duration, director):
        self.name = name
        self.duration = duration
        self.director = director

    def __repr__(self):
        return self.name #returns the movies name CORRECTLY not as numbers or whatever
        return self.duration

class Watchlist:
    def __init__(self):
        self.movies_to_watch = []
        self.watched_movies = []

    def add_movies(self, movie_list):
        self.movies_to_watch.extend(movie_list)

    def watch_movies(self, movie_name):
        for movie in self.movies_to_watch:
            if movie.name == movie_name:
                self.movies_to_watch.remove(movie)
                self.watched_movies.append(movie)
                print(f"'{movie.name}' has been added to the 'watched' list.")
                return
        print("Movie not found.")

    def total_time_watched(self):
        total_time = sum(movie.duration for movie in self.watched_movies)
        return total_time

    def total_time_to_watch(self):
        total_time = sum(movie.duration for movie in self.movies_to_watch)
        return total_time


    def print_status(self):
        print(f"Still to watch: {watchlist.movies_to_watch},\n Already watched: {watchlist.watched_movies}")
        print(f"Total duration of movies still to watch: {watchlist.total_time_to_watch()}, \n Total duration of all watched movies: {watchlist.total_time_watched()}")
        #used watchlist.total_time_to_watch() and the other with () bc they return VALUES

watchlist = Watchlist()
watchlist.add_movies([Movies("Pulp Fiction", 154, "Quentin Tarantino"),
        Movies("Barry Lyndon", 185, "Stanley Kubrick"),
        Movies("Luca", 95, "Enrico Casarosa"),
        Movies("Gone with the Wind", 238, "Victor Fleming")])

watchlist.add_movies([Movies("Volver", 121, "Pedro Almodóvar"),
        Movies("The Shining", 115, "Stanley Kubrick")])
watchlist.print_status()


watchlist.watch_movies("Volver")
watchlist.watch_movies("Luca")
watchlist.print_status()