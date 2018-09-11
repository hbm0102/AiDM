def getMovies():
  with open("data/movies.dat") as f:
    for line in f:
      content = line.split("::")
      movie = {"id": content[0], "name": content[1], "category": content[2]}
