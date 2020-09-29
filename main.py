#2. A motorbike costs £2000 and loses 10% of its value every year. Print the bike’s value every year until it falls below £1000.

print ("Motorbike Value")
value = 2000


while value>1000:
  limited_float=round(value,2)
  print("£",limited_float)
  value=value*0.9
  
  
else:
  print ("Value is less than £1000")


