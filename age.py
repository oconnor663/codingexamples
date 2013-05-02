my_age = 30
their_age = 47

minimum = my_age // 2 + 7

maximum = (my_age - 7) * 2

if their_age < minimum:
  print(their_age, "is too young!")
elif their_age > maximum:
  print(their_age, "is too old!")
else:
  print(their_age, "is fine.")
