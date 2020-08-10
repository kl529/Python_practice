# ComputerHand, PlayerHand give() card() 중복사용 고칠것 
import random
class ECardController:
	def __init__(self):
		print("Ready")
	def play(self):
		Score.Computer=0
		Score.Player=0
		print("\n\nWelcome to Death E-Card Match!")
		print("You have to make a card each phase.")
		print("Emperor beats civil, civil beats slave and slave beats Emperor.")
		print("Each time you lose, a drill will penetrate into your ear.")
		print("If you lose, the drill will dig up your brain.")
		print("Then, Good Luck! \n\n")
		print("=============================================\n")
		self.__card=input("How many cards? (at least 3) : ")
		while not self.__card.isdigit() or int(self.__card)<3:
			self.__card=input("How many cards? (at least 3) : ")
		self.__slave=input("How many slave cards? (at most total cards-2) : ")
		while not self.__slave.isdigit() or int(self.__card)-2<int(self.__slave):
			self.__slave=input("How many slave cards? (at most total cards-2) : ")
		self.__games=input("How many matches?(at least 3) : ")
		while not self.__games.isdigit() or int(self.__games)<3:
			self.__games=input("How many matches? (at least 3) : ")			
		num=1
		while True:
			mat=Match(num, int(self.__card), int(self.__slave))
			mat.begin()
			num+=1
			if int(self.__games)%2==0:
				if Score.Player>=int(self.__games)/2+1:
					print("You win!")
					break
				if Score.Computer>=int(self.__games)/2+1:
					print("The drill pierces your brain")
					print("You Died")
					break
				if Score.Player==Score.Computer and Score.Player==int(self.__games)/2:
					print("Draw. Maybe lucky")
					break
			else:
				if Score.Player>=int(self.__games)//2+1:
					print("You win!")
					break
				if Score.Computer>=int(self.__games)//2+1:
					print("The drill pierces your brain")
					print("You Died")
					break

		print("\n\n=========  End  =========")

class ECard:
	@staticmethod
	def compare(card1,card2):
		if card1=="Emperor" and card2=="Civil" or card1=="Slave" and card2=="Emperor" or card1=="Civil" and card2=="Slave":
			return 1 # Computer wins
		elif card1=="Emperor" and card2=="Slave" or card1=="Civil" and card2=="Emperor" or card1=="Slave" and card2=="Civil":
			return 2 # Player wins 
		else:
			return 0 # Draw

class Score:
	Computer=0
	Player=0

class Match:
	def __init__(self, match, card, slave):
		self.__card=card
		self.__slave=slave
		self.__match=match
		print("=============== Stage "+str(self.__match)+" Starts ===============")
	def begin(self):
		com=ComputerHand(self.__match, self.__card, self.__slave)
		pla=PlayerHand(self.__match, self.__card, self.__slave)
		num=1
		while True:
			Ph=Phase(num, com.current(), pla.current())
			Ph.initiate()
			check=ECard.compare(com.give(), pla.give(Ph.input()))
			print("Computer makes "+"["+com.output()+"]")
			print("You make "+"["+pla.output()+"]")
			if check==1:
				print("You lose.")
				print("The drill approaches.\n")
				Score.Computer+=1
				break
			if check==2:
				print("You win.")
				print("Goddes saves you.\n")
				Score.Player+=1
				break
			else:
				print("Draw.\n")
			num+=1
			com.card()
			pla.card()

class Phase:
	def __init__(self, phase, com, pla):
		self.__phase=phase
		self.__com=com
		self.__pla=pla
		print("            ====== Phase "+str(self.__phase)+" ======")
	def initiate(self):
		print(self.__pla)
		self.__num=input("Choose the card number you want to make : ")
		while not self.__num.isdigit() or int(self.__num)<0 or len(self.__pla)<int(self.__num):
			self.__num=input("Choose the card number you want to make : ")	
	def input(self):
		return self.__num


class ComputerHand:
	def __init__(self, match, card, slave):
		if match%2==1:
			self.__Hand=["Emperor"]
			for _ in range(card-1):
				self.__Hand.append("Civil")
		else:
			self.__Hand=[]
			for _ in range(slave):
				self.__Hand.append("Slave")
			for _ in range(card-slave):
				self.__Hand.append("Civil")
	def give(self):
		self.__num=random.randrange(len(self.__Hand))
		self.__output=self.__Hand[self.__num]
		return self.__output
	def card(self):
		self.__Hand=self.__Hand[:self.__num]+self.__Hand[self.__num+1:]
	def output(self):
		return self.__output
	def current(self):
		return self.__Hand


class PlayerHand:
	def __init__(self, match, card, slave):
		if match%2==1:
			self.__Hand=[]
			for _ in range(slave):
				self.__Hand.append("Slave")
			for _ in range(card-slave):
				self.__Hand.append("Civil")
		else:
			self.__Hand=["Emperor"]
			for _ in range(card-1):
				self.__Hand.append("Civil")
	def give(self, num):
		self.__num=int(num)
		self.__output=self.__Hand[self.__num-1]
		return self.__output
	def card(self):
		self.__Hand=self.__Hand[:self.__num-1]+self.__Hand[self.__num:]		
	def output(self):
		return self.__output
	def current(self):
		return self.__Hand

