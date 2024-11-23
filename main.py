ITEMS = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Gold]
WSIZE = get_world_size()

# ===[GLOBAL VARIABLE] FOR MAZE RUNNER===
DIRECTIONS = {North:(0,1),South:(0,-1),East:(1,0),West:(-1,0)}
BACK_DIR = {North:South,South:North,East:West,West:East}
PATH_TO_DIR = {10:North,1:East,-10:South,-1:West}
DICTS = [{}, {}] # 0 == adjList, 1 == visited
TREASURE = [-1, -1]
# ===[GLOBAL VARIABLE] FOR MAZE RUNNER===

while True:
	# DETERMINES THE MINIMUM AND 2ND MINIMUM ITEMS
	# AND GETS THE MINIMUM ITEM UP TO THE 2ND MINIMUM ITEM AMOUNT + DIFFERENCES
	_MIN = [0, num_items(ITEMS[0])]
	for _1 in range(len(ITEMS[1::])):
		if _MIN[1] > num_items(ITEMS[_1 + 1]):
			_MIN[0] = _1 + 1
			_MIN[1] = num_items(ITEMS[_1 + 1])
	_2ND_MIN = [None, None]
	for _1 in range(len(ITEMS)):
		if _1 != _MIN[0]:
			if not _2ND_MIN[0]:
				_2ND_MIN[0] = _1
				_2ND_MIN[1] = num_items(ITEMS[_1])
			else:
				if _2ND_MIN[1] > num_items(ITEMS[_1]):
					_2ND_MIN[0] = _1
					_2ND_MIN[1] = num_items(ITEMS[_1])
	#quick_print("MIN: ",_MIN[1],"| 2ND MIN:",_2ND_MIN[1])
	get_resource(_MIN[0], _2ND_MIN[1]+_2ND_MIN[1]-_MIN[1])