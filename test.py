from imdb import IMDb
# https://github.com/alberanid/imdbpy/blob/master/docs/usage/query.rst
# requires  [console] pip install imdbpy

ia = IMDb()
data=ia.search_movie('The Matrix')
if data:
        movieId= data[0].movieID
        movie=ia.get_movie(movieId)
        if movie:
            cast=movie.get('cast')
            for actor in cast:  
                print (actor['name'])