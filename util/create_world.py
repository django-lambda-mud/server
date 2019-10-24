from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

allRooms = {title: Room(title=title, description=title) for title in range(100)}

grid = []
tempArray = []
keepTrackOfIndex = 9
rows=10
cols=10

for key, value in allRooms.items():
  if keepTrackOfIndex == key:
    keepTrackOfIndex += rows
    tempArray.append(value)
    grid.append(tempArray)
    tempArray = []
  else:
    tempArray.append(value)
 
for i in range(rows):
  for j in range(cols):
    grid[i][j].save()

for i in range(rows):
  for j in range(cols):
    if i < rows - 1:
      grid[i][j].connectRooms(grid[i + 1][j], "s")
    if i > 0:
      grid[i][j].connectRooms(grid[i - 1][j], "n")  
    if j < cols - 1:
      grid[i][j].connectRooms(grid[i][j + 1], "e")  
    if j > 0:
      grid[i][j].connectRooms(grid[i][j - 1], "w")

players=Player.objects.all()
for p in players:
  p.currentRoom=grid[0][0].id
  p.save()