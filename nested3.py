for left in range(5):
  for right in range(left, 6):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()


  #fight club weekly schedule...
print("Weekly Fights:")
fighters = [ 'Elii', 'Rob', 'NS', 'Donald','Julia']
countries=['France','Italy','Spain','Germany']
for home_team in fighters:
  for away_team in fighters:
    for country in countries:
         if home_team != away_team:
             print(home_team + " vs " + away_team + " at: " +country)



for left in range(5):
  for right in range(left, 6):
    print("[" +str('b') + "|" + str('m') + "]", end=" ")
  print()

for left in range(5):
  for right in range(left, 6):
    print("[" +"*" + "|" + "#" + "]", end=" ")
  print()

for left in range(0,10,1):
  for right in range(left, 20,3):
    print("[" +"@" + "|" + "£" + "]", end=" ")
  print()
