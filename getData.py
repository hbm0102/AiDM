def getMovies():
  movies = []
  with open("data/movies.dat") as f:
    for line in f:
      content = line.split("::")
      movie = {"id": int(content[0]), "name": content[1], "category": content[2]}
      movies.append(movie)
  return movies

def getRatings():
  ratings = []
  with open("data/ratings.dat") as f:
    for line in f:
      content = line.split("::")
      rating = {"userId": int(content[0]), "movieId": int(content[1]), "rating": int(content[2]), "timestamp": content[3]}
      ratings.append(rating)
  return ratings

def getRatingsForMovie(movieId):
  ratings = []
  with open("data/ratings.dat") as f:
    for line in f:
      content = line.split("::")
      if (int(content[1]) == movieId):
        rating = {"userId": int(content[0]), "movieId": int(content[1]), "rating": int(content[2]), "timestamp": content[3]}
        ratings.append(rating)
  return ratings

def getRatingsForUser(userId):
  ratings = []
  with open("data/ratings.dat") as f:
    for line in f:
      content = line.split("::")
      if (int(content[0]) == userId):
        rating = {"userId": int(content[0]), "movieId": int(content[1]), "rating": int(content[2]), "timestamp": content[3]}
        ratings.append(rating)
  return ratings

def allNumericRatings():
  ratings = []
  with open("data/ratings.dat") as f:
    for line in f:
      content = line.split("::")
      ratings.append(int(content[2]))
  return ratings

def getUsers():
  users = []
  with open("data/users.dat") as f:
    for line in f:
      content = line.split("::")
      # UserID::Gender::Age::Occupation::Zip-code
      user = {"userId": int(content[0]), "gender": content[1], "age": int(content[2]), "occupation": content[3], "zip": content[4]}
      users.append(user)
  return users
