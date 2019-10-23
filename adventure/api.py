from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)


@csrf_exempt
@api_view(["GET"])
def rooms(request):
    rooms = Room.objects.all()
    roomsArray = []
    for i in range(len(rooms)):
        roomsArray.append({
            'id': rooms[i].id, 
            'title': rooms[i].title, 
            'description': rooms[i].description,
            'n_to': rooms[i].n_to, 
            's_to': rooms[i].s_to, 
            'e_to': rooms[i].e_to, 
            'w_to': rooms[i].w_to
        })
    return JsonResponse({
        'rooms': roomsArray
    }, safe=True)





#     # create Forest
# grid = []
# rows = 10
# cols = 15

# def createForest():
#   for i in range(rows):
#     currentRow = []
#     for j in range(cols):
#       currentRow.append(createForestRoom(i, j))
#     grid.append(currentRow)

#   for row in range(rows):
#     for col in range(cols):
#       addNeighbors(row, col)
  
#   return grid

  

# def createForestRoom(i, j):
#   return {
#     i: i,
#     j: j,
#     "start": i == 0 and j == 0,
#     "neighbors": [],
#     "treeOne":
#       i == 0 and j == 2 or
#       i == 0 and j == 3 or
#       i == 0 and j == 4 or
#       i == 1 and j == 2 or
#       i == 2 and j == 2 or
#       i == 1 and j == 4 or
#       i == 2 and j == 4 or
#       i == 0 and j == 5 or
#       i == 0 and j == 6 or
#       i == 2 and j == 5,
#     "treeTwo":
#       i == 5 and j == 10 or i == 5 and j == 11 or i == 5 and j == 12,
#     "treeThree":
#       i == 8 and j == 0 or
#       i == 9 and j == 0 or
#       i == 9 and j == 1 or
#       i == 9 and j == 2 or
#       i == 9 and j == 4 or
#       i == 9 and j == 5 or
#       i == 9 and j == 6 or
#       i == 9 and j == 7 or
#       i == 9 and j == 8 or
#       i == 9 and j == 9 or
#       i == 9 and j == 10 or
#       i == 9 and j == 11 or
#       i == 9 and j == 12 or
#       i == 9 and j == 13 or
#       i == 9 and j == 14,
#     "grave": i == 0 and j == 8,
#     "goldOne": i == 0 and j == 9,
#     "toStreet": i == 0 and j == 14,
#     "toHouse": i == 9 and j == 3
#   }

# def addNeighbors(i, j):
#   if i < rows - 1:
#     grid[i][j]["neighbors"].append(grid[i + 1][j])
#   if i > 0:
#     grid[i][j]["neighbors"].append(grid[i - 1][j])
#   if j < cols - 1:
#     grid[i][j]["neighbors"].append(grid[i][j + 1])
#   if j > 0:
#     grid[i][j]["neighbors"].append(grid[i][j - 1])
#   return

# print(createForest())