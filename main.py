 # A motorbike costs £2000 and loses 10% of its value every year. Print the bike’s value every year until it falls below £1000.
print ("Motorbike Value")
# Create Value Variable to hold starting value of 2000
value = 2000
# Create a While loop to take reduce the original value by !0% stopping before it goes under 1000
while value > 1000:
# Using a round function, restrict the Value Variable (float) to 2 decimal places to reflect Money
  limited_float = round (value, 2)
# Print the value
  print ("£", limited_float)
# Multiply the value by 0.9 to remove 10%
  value = value * 0.9
# Else statement to print if the Value goes lower than 100  
else:
  print ("Value is less than £1000")
