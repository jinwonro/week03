from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
print(target_movie['star'])

movies = list(db.movies.find({'star': target_movie['star']}))

for movie in movies:
    print(movie['title'])

db.movies.update_many({'star': target_movie['star']}, {'$set': {'star': '0'}})

