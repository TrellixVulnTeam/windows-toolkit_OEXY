def submenuHeader(header):
	headerLength = len(header)
	headerLengthPlusTwo = headerLength + 2
	print("{}{}{}".format("==", "=" * headerLengthPlusTwo, "=="))
	print("{}{}{}{}{}".format("==", " ", header, " ", "=="))
	print("{}{}{}".format("==", "=" * headerLengthPlusTwo, "=="))
	print()

def submenuFooter():
	print()
	while True:
		userChoice = input("Choose your operation or [x] to get back to main menu: ")
		if userChoice.isdigit():
			# userChoice = int(userChoice)
			return userChoice
			break
		elif (userChoice == 'x') or (userChoice == 'X'):
			return 'x'
			break
		else:
			print("Invalid input! Please try again.")