def myFunction(list): 
  return [
    list[i:i+3]
    for i in range(len(list) - 2)
  ]

