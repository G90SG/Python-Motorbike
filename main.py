#2. A motorbike costs £2000 and loses 10% of its value every year. Print the bike’s value every year until it falls below £1000.

print ("Motorbike Value")
value = 2000
print ("£",value)
while value>1001:
  value=value*0.9
  limited_float=round(value,2)
  print("£",limited_float)
else:
  print ("Value is less than £1000")

#how do i stop it before the £956.59#
