from getData import getRatings, allNumericRatings, getRatingsForMovie, getRatingsForUser
import numpy as np

def getMeanGlobalRatingSlow():
  ratings = getRatings()
  total = 0.0
  amount = 0.0
  for rating in ratings:
    total += rating["rating"]
    amount += 1
  return total / amount

def getMeanGlobalRatingFast():
  ratings = np.array(allNumericRatings())
  return np.mean(ratings)

def getMeanRatingForItem(movieId):
  movieRatings = getRatingsForMovie(movieId)
  total = 0.0
  amount = 0.0
  for rating in movieRatings:
    total += rating["rating"]
    amount += 1
  return total / amount

def getMeanRatingForUser(userId):
  movieRatings = getRatingsForUser(userId)
  total = 0.0
  amount = 0.0
  for rating in movieRatings:
    total += rating["rating"]
    amount += 1
  return total / amount


print("mean is", getMeanRatingForUser(10))