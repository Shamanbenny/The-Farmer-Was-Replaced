def mazeSetup():
	# Sets up the maze by Fertilizing the bushes
	if get_entity_type() == Entities.Hedge:
		return
	if get_entity_type() == Entities.Treasure:
		return
	moveTo(0,WSIZE-1)
	if get_entity_type() != Entities.Bush:
		harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Bush)
	while get_entity_type() != Entities.Hedge:
		if num_items(Items.Fertilizer) == 0:
			trade(Items.Fertilizer)
		use_item(Items.Fertilizer)

def pos_to_index(x, y):
	# Converts the x and y position to an index
	return y * WSIZE + x

def index_to_pos(idx):
	# Converts the index to an x and y position
	tmpX = idx % WSIZE
	tmpY = (idx - tmpX) / WSIZE
	return (tmpX, tmpY)