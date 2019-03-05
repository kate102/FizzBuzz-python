def isFizz(checkNum):
  if((checkNum % 15) == 0):
      print "FizzBuzz"
  elif(checkNum % 3 == 0):
       print "Fizz"
  elif((checkNum % 5) == 0):
       print "Buzz"
  else:
       print checkNum



count = 1
while count<101:
    isFizz(count)
    count += 1
