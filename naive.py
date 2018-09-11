from getData import getRatings, allNumericRatings
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
    


print("mean is", getMeanGlobalRatingFast())
print("mean is", getMeanGlobalRatingSlow())