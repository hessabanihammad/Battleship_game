import random, os #imports 

#specifying the parameters 
dim=10
board=[]
numXs=3 
win=False 
trials=0

#creating the board 
for row in range(dim):
	tmpList=[]
	for col in range(dim):
		tmpList.append(".")
	board.append(tmpList)

#I will generate a random number that helps me decide whether the ship position is going to be vertical or horizontal 
random_number=random.randint(1,2)


#if the random number being generated is 1 it will print the ship horizontally 
if random_number== 1:
		RandomRow=random.randint(0,dim-1)
		RandomCol=random.randint(0,dim-3) 

		for i in range(numXs-1): #range function doesn't include the last index 
			board[RandomRow][RandomCol]='X'
			RandomCol+=1

		while board[RandomRow][RandomCol]=='X':
			RandomRow=random.randint(0,dim-1)
			RandomCol=random.randint(0,dim-3)
		board[RandomRow][RandomCol]='X'
		
elif random_number==2:
		RandomRow=random.randint(0,dim-3)
		RandomCol=random.randint(0,dim-1)

		for i in range(numXs-1):
			board[RandomRow][RandomCol]='X' 
			RandomRow+=1

		while board[RandomRow][RandomCol]=='X':
			RandomRow=random.randint(0,dim-3)
			RandomCol=random.randint(0,dim-1)
		board[RandomRow][RandomCol]='X'

trials+=0

#printing the board that has the answer 
for row in range(dim):
	for col in range(dim):
		print(board[row][col],end=" ")
	print()

os.system("clear")

#board that is empty and the user sees 
for r in range(dim):
	for c in range(dim):
		print(board[row][col], end=" ")
	print()

#game instructions 
print("Welcome to Battleship!")
print("To Win the game, you need to sink the battleship in the least number of trials, good luck!")
print("Your trials are being tracked by your score, the less number of trials, the better")


#outer while loop that controls the flow of the game 
while not win:
	#flag for error checking on the row
	#while the input is invalid, it will ask the user for a proper row value
	flag=False
	while flag==False:

		guess_row=input("Please guess the row by choosing a valid value from 0-9: ")

		if guess_row.isdigit():
			if len(guess_row)>1:
				print("Invalid range")
				continue
			flag=True 		
		else: 
			print("Invalid Input!")

	#flag for error checking on the coloumn
	#while the input is invalid, it will ask the user again for a coloumn value
	flag2=False 
	while flag2==False:

		guess_coloumn=input("Please guess the coloumn by choosing a valid value from 0-9: ")

		if guess_coloumn.isdigit():
			if len(guess_coloumn)> 1:
				print("Invalid range")
				continue
			flag2=True
		else:
			print("Invalid Input!")

	#casting the user's entries to integer values. 
	guess_row=int(guess_row)
	guess_coloumn=int(guess_coloumn)

	#checks for the user's input 
	if board[guess_row][guess_coloumn]=="X":
		board[guess_row][guess_coloumn]="."
		numXs=numXs-1 #subtracts from the number of ships to sink if user guesses the right location
		trials=trials+1 #increases the number of trials 
		
		if numXs !=0: 
			print("Well done! you have", numXs, "blocks to sink")
		else:
			print("Congratulations! you sank the battleship! It took you", trials,"trials to sink the battleship")
			win=True 
	#if the user gusses the wrong position, then the number of trials increase 
	elif board[guess_row][guess_coloumn]==".":
		print("Wrong guess! try again")
		trials=trials+1








	






		







