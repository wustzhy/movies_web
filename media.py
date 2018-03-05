import webbrowser


class Movie:
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_url, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        """open movie on web browser"""
        webbrowser.open(self.trailer_youtube_url)
