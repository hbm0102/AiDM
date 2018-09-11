def getMovies():
  movies = []
  with open("data/movies.dat") as f:
    for line in f:
      content = line.split("::")
      movie = {"id": content[0], "name": content[1], "category": content[2]}
      movies.append(movie)
  return movies

def getRatings():
  ratings = []
  with open("data/ratings.dat") as f:
    for line in f:
      content = line.split("::")
      rating = {"userId": content[0], "movieId": content[1], "rating": content[2], "timestamp": content[3]}
      ratings.append(rating)
  return ratings

def getUsers():
  users = []
  with open("data/users.dat") as f:
    for line in f:
      content = line.split("::")
      # UserID::Gender::Age::Occupation::Zip-code
      user = {"userId": content[0], "gender": content[1], "age": content[2], "occupation": content[3], "zip": content[4]}
      users.append(user)
  return users
