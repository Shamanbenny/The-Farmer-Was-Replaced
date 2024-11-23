def get_resource(idx, minReq):
	moveTo(0, WSIZE-1)
	quick_print("Harvesting: ", ITEMS[idx], " till ", minReq)
	while True:
		if idx == 0:
			hWheat()
			mLogic()
		elif idx == 1:
			hWood()
			mLogic()
		elif idx == 2:
			hCarrot()
			mLogic()
		elif idx == 3:
			hPumpkin()
		elif idx == 4:
			hGold()
		if get_pos_x() == 0 and get_pos_y() == WSIZE-1:
			# After each run of the entire farm, check if the minimum requirement is met
			if num_items(ITEMS[idx]) > minReq:
				break