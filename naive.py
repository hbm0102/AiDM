from getData import getRatings

def getMeanGlobalRating():
  ratings = getRatings()
  total = 0
  amount = 0
  for rating in ratings:
    total += rating["rating"]
    amount += 1
  return total
    


print("mean is", getMeanGlobalRating())