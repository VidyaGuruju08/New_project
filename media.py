import webbrowser

class Movie():
    
    def __init__(self,title,storyline,poster,trailer):
        self.title=title
        self.story_line=storyline
        self.poster_image=poster
        self.trailer_youtube_url=trailer
        
    def show_movie_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


