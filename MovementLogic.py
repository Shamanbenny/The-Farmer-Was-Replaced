def moveTo(x, y):
	# Move to the specified position
	while get_pos_x() != x:
		move(East)
	while get_pos_y() != y:
		move(South)

def mLogic():
	# Sweeping movement logic w/ watering
	if get_water() == 0:
		use_item(Items.Water_Tank)
	if get_pos_y() == 0:
		move(South)
		move(East)
	else:
		move(South)