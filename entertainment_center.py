
import media
import fresh_tomatoes

#different movie trailers
orange=media.Movie("Orange",
                   "A boy who doesn’t believe in everlasting love",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Orange_poster.jpg/220px-Orange_poster.jpg",
                   "https://www.youtube.com/watch?v=sW4bXzRAj9I")

#print(orange.story_line)
coco=media.Movie("Coco",
                 "A boy who fell for music",
                 "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                 "https://www.youtube.com/watch?v=zNCz4mQzfEI")
#print(coco.story_line)
#coco.show_movie_trailer()
spykids=media.Movie("Spy-Kids",
                    "people mysteriously disappear and they were rescued by their own kids",
                    "http://www.impawards.com/2001/posters/spy_kids_ver5.jpg",
                    "https://www.youtube.com/watch?v=GE5aHKJp6HI")
#print(spykids.story_line)
mukundha=media.Movie("Mukundha",
                    "A person makes it a part of his daily routine to fight for his friend and for truth",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Mukunda_poster.jpg/220px-Mukunda_poster.jpg",
                    "https://www.youtube.com/watch?v=9rcxSklwL0g")
#print(mukundha.story_line)
insidious=media.Movie("Insidious",
                    "A supernatural horror film of a boy",
                    "https://vignette.wikia.nocookie.net/insidiousmovie/images/2/2d/INS.jpg/revision/latest?cb=20180114194522",
                    "https://www.youtube.com/watch?v=zuZnRUcoWos")
#print(insidious.story_line)
tangled=media.Movie("Tangled",
                    "young girl locked up by her overly protective mother. Her wish to escape into the world outside and finally comes true when she meets the good-hearted thief",
                    "https://vignette.wikia.nocookie.net/disney/images/c/ca/Tangled_rapunzel_poster_20.jpg/revision/latest?cb=20110929034113",
                    "https://www.youtube.com/watch?v=ip_0CFKTO9E")
#print(tangled.story_line)
my_movies=[orange,coco,spykids,mukundha,insidious,tangled]
fresh_tomatoes.open_movies_page(my_movies)
