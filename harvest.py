def hWheat():
	if get_ground_type() == Grounds.Soil:
		harvest()
		till()
	harvest()
def hWood():
	if get_ground_type() == Grounds.Soil:
		harvest()
		till()
	harvest()
	if get_pos_x()%2==0 and get_pos_y()%2==1:
		plant(Entities.Tree)
	elif get_pos_x()%2==1 and get_pos_y()%2==0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
def hCarrot():
	if get_ground_type() == Grounds.Turf:
		harvest()
		till()
	harvest()
	if num_items(Items.Carrot_Seed) == 0:
		trade(Items.Carrot_Seed)
	plant(Entities.Carrots)
def hPumpkin():
	count = 3
	while count > 0:
		if get_ground_type() == Grounds.Turf:
			harvest()
			till()
		if num_items(Items.Pumpkin_Seed) == 0:
			trade(Items.Pumpkin_Seed)
		plant(Entities.Pumpkin)
		mLogic()
		if get_pos_x()==0 and get_pos_y()==WSIZE-1:
			count = count - 1
	while True:
		while get_entity_type() == None or not can_harvest():
			if get_entity_type() == None:
				if num_items(Items.Pumpkin_Seed) == 0:
					trade(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)
			else:
				continue
		mLogic()
		if get_pos_x()==0 and get_pos_y()==WSIZE-1:
			break
	harvest()