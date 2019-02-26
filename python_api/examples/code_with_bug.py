turned_left_last = False
while True:
	distance = input("Enter the distance in cm : ")
	if distance > 15:
		print("Go straight")
	else:
		# No elif needed, either above or below 15 cm
		if turned_left_last:
			print("Turn Right")
			turned_left_last = False
		else:
			print("Turn Left")
			turned_left_last = True
