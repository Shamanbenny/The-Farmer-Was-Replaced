def hGold():
	mazeSetup()

	# RESET adjList and visited
	DICTS[0] = []
	for _2 in range(WSIZE * WSIZE):
		DICTS[0].append([])
	DICTS[1] = []
	for _3 in range(WSIZE * WSIZE):
		DICTS[1].append(False)
	
	mazeSolve()
	
def mazeSolve():
	# Solves the maze repeatedly until the count is 0
	startX, startY = get_pos_x(), get_pos_y()
	setupAdjList(startX, startY)
	count = 298		# Adjustable [Handle with care]
	while count > 0:
		treasureIdx = pos_to_index(TREASURE[0], TREASURE[1])
		currIdx = pos_to_index(get_pos_x(), get_pos_y())
		path = findPath(currIdx, treasureIdx)
		#quick_print(path)
		for nextIdx in path[1::]:
			toMove = nextIdx - pos_to_index(get_pos_x(), get_pos_y())
			move(PATH_TO_DIR[toMove])
		next_x, next_y = measure()
		TREASURE[0] = next_x
		TREASURE[1] = next_y
		if count == 1:
			count = count - 1
			continue
		if num_items(Items.Fertilizer) == 0:
			trade(Items.Fertilizer)
		while get_entity_type() == Entities.Treasure:
			use_item(Items.Fertilizer)
		count = count - 1
	harvest()
	
def setupAdjList(x, y):
	# Uses DFS to setup adjList
	# [IMPORTANT] MAY NOT BE THE SHORTEST PATH
	if get_entity_type() == Entities.Treasure:
		TREASURE[0], TREASURE[1] = x, y
	currIdx = pos_to_index(x, y)
	DICTS[1][currIdx] = True
	for direction in DIRECTIONS:
		(dx, dy) = DIRECTIONS[direction]
		nx, ny = x + dx, y + dy
		neighbor = pos_to_index(nx, ny)
		if 0 <= nx and nx < WSIZE and 0 <= ny and ny < WSIZE:
			if not DICTS[1][neighbor]:
				if move(direction):
					DICTS[0][currIdx].append(neighbor)
					DICTS[0][neighbor].append(currIdx)
					setupAdjList(nx, ny)
					move(BACK_DIR[direction])

def findPath(startIdx, treasureIdx):
	# Uses BFS to find the shortest path based on adjList
	_queue = [[startIdx]]
	_visited = []
	while _queue:
		path = _queue.pop(0)
		currVertex = path[-1]
		if currVertex == treasureIdx:
			return path
		if currVertex not in _visited:
			_visited.append(currVertex)
			for nIdx in DICTS[0][currVertex]:
				new_path = path + [nIdx]
				_queue.append(new_path)
	return []
	