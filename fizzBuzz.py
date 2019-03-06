def isFizz(checkNum):
  if((checkNum % 15) == 0):
      return "FizzBuzz"
  elif(checkNum % 3 == 0):
       return "Fizz"
  elif((checkNum % 5) == 0):
       return "Buzz"
  else:
       return checkNum


# count = 1
# while count<101:
#     isFizz(count)
#     count += 1
