def q5(endnum):

  list = []
  sq_list = []
  
  for i in range (endnum + 1):
  """ Create a list with numbers from 1 to a 100
    list.append(i)
  """ Create a list with squares of earlier created numbers   
    sq_list.append(i**2)
    
""" Get the sum of the list with squared number
  sum_of_squares = sum(sq_list)
  
""" Get the square of the sum of the initial list
  square_of_sum = sum(list)**2
  
  result = square_of_sum - sum_of_squares
  
  print (result)
  return result
  
q5(100)
