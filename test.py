from imdb import IMDb
# https://github.com/alberanid/imdbpy/blob/master/docs/usage/query.rst
# requires  [console] pip install imdbpy

# https://github.com/hardikvasa/google-images-download#examples
# requires [console] pip install google_images_download
from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload() 

moviename='I Robot 2004'
output="images/"+moviename
# print(output)
ia = IMDb()
data=ia.search_movie(moviename)
# data=ia.search_movie('The Matrix')
if data:
        movieId= data[0].movieID
        movie=ia.get_movie(movieId)
        if movie:
            cast=movie.get('cast')
            # for actor in cast:  
            #     arguments = {"keywords": actor['name'],"limit":100,"print_urls":True}
            #     paths = response.download(arguments)   
            #     print(paths)  
            limit=5
            for index, actor in zip(range(limit), cast):
                a=str(actor['name'])
                a=a.replace("å","a").replace("ú","u").replace("á","a")
                print(index, a)
                keys=''+a+' '+moviename
                #millora de busqueda
                print(keys)
                arguments = {"keywords": keys,"limit":10,"print_urls":True,"output_directory": output,"image_directory":a}
                paths = response.download(arguments)   
                print(paths)  
