import numpy as np

def main():
	gm = GameManager()
	gm.start_Game()
	#b = Board()
	#b.getAvailableMoves(Board.BLACK)

class GameManager:
	
	def __init__(self):
		self.board = Board()
		self.turn = Board.BLACK
		
	def start_Game(self):
		
		passCount = 0
		while passCount < 2:
			self.board.print_board()
			self.printTurn()
			moves = self.board.getAvailableMoves(self.turn)
			if len(moves) == 0:
				passCount += 1
				print('pass')
				
			else:
				passCount = 0
				self.board.printAvailables(self.turn)
				print('Please select move')
				print('X : ...')
				x = input()
				print('Y : ...')
				y = input()
				if self.move(x, y, self.turn) > 0:
					self.changeTurn()
				else:
					print('Invalid move!!')
					
	def changeTurn(self):
		self.turn = 3 - self.turn
					
	def move(self, x, y, color):
		return self.board.move(int(x)-1, int(y)-1, color)
	
	def getTurn(self):
		return self.turn
		
	def printTurn(self):
		if self.turn == Board.BLACK:
			print('Turn : Black(O)')
		else:
			print('Turn : White(@)')

class Board:
	NO_DISK = 0
	BLACK = 1
	WHITE = 2
	AVAILABLE = 3
	
	def __init__(self):
		self.board = np.array([[0,0,0,0,0,0,0,0],\
											[0,0,0,0,0,0,0,0],\
											[0,0,0,0,0,0,0,0],\
											[0,0,0,1,2,0,0,0],\
											[0,0,0,2,1,0,0,0],\
											[0,0,0,0,0,0,0,0],\
											[0,0,0,0,0,0,0,0],\
											[0,0,0,0,0,0,0,0]])
	
	def getAvailableMoves(self, color):
		temp = self.board.copy()
		moves = []
		for x in range(8):
			for y in range(8):
				if self.board[y, x] == \
				Board.NO_DISK and \
				self.move(x, y, color) >0:
					moves.append([x, y])
				self.board = temp.copy()
		return moves
	
	def print_board(self):
		n = 1
		row = ''
		print('Black:O, White:@')
		print('    1  2  3  4  5  6  7  8 ')
		for disk in self.board.flatten():
			if n % 8 == 1:
				row += ' ' + str(int(n / 8) + 1) + ' '
			if disk == Board.NO_DISK:
				row += '[ ]'
			elif disk == Board.BLACK:
				row += '[O]'
			else:
				row +='[@]'
				
			if n % 8 == 0:
				print(row)
				row = ''
			
			n+=1
		print('\n')
		
	def printAvailables(self, color):
		board = self.board.copy()
		for move in self.getAvailableMoves(color):
			board[move[1], move[0]] = Board.AVAILABLE
			#print(move)
			
		n = 1
		row = ''
		print('Black:O, White:@')
		print('    1  2  3  4  5  6  7  8 ')
		for disk in board.flatten():
			if n % 8 == 1:
				row += ' ' + str(int(n / 8) + 1) + ' '
			if disk == Board.NO_DISK:
				row += '[ ]'
			elif disk == Board.BLACK:
				row += '[O]'
			elif disk == Board.AVAILABLE:
				row += '[*]'
			else:
				row +='[@]'
				
			if n % 8 == 0:
				print(row)
				row = ''
			
			n+=1
		print('\n')
		
	def move(self, x, y, color):
		xTemp = x
		yTemp = y
		opponent = self.flip(color)
		
		sum = 0
		flipList = []
		
		# right
		tempList = []
		while x < 7:
			x += 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
		
		# left
		x = xTemp
		y = yTemp
		tempList.clear()
		while x > 0:
			x -= 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
			
		# upper
		x = xTemp
		y = yTemp
		tempList.clear()
		while y > 0:
			y -= 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
		
		# lower
		x = xTemp
		y = yTemp
		tempList.clear()
		while y < 7:
			y += 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
		
		#upper left
		x = xTemp
		y = yTemp
		tempList.clear()
		while x > 0 and y > 0:
			x -= 1
			y -= 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
				
		# upper right
		x = xTemp
		y = yTemp
		tempList.clear()
		while x < 7 and y > 0:
			x += 1
			y -= 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
				
		# lower left
		x = xTemp
		y = yTemp
		tempList.clear()
		while x > 0 and y < 7:
			x -= 1
			y += 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
				
		# lower right
		x = xTemp
		y = yTemp
		tempList.clear()
		while x < 7 and y < 7:
			x += 1
			y += 1
			if self.board[y, x] == opponent:
				tempList.append([x, y])
			elif self.board[y, x] == Board.NO_DISK:
				break
			elif self.board[y, x] == color:
				if len(tempList) != 0:
					flipList += tempList
				break
		if len(flipList) > 0:
			self.board[yTemp, xTemp] = color
			for item in flipList:
				self.board[item[1], item[0]] = color
		
		return len(flipList)
	
	def flip(self, color):
		return 3 - color
		
if __name__ == '__main__':
	main()
