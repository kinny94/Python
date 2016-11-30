import random
playing = False
chip_pool = 100
bet = 1
restart_phrase ="Press 'd' to deal the cards agaib, or press 'q' to quit"
suits = ('H', 'D', 'C', 'S')
ranking = ('A', '2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}


class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + self.rank

	def grab_suit(self):
		return self.suit

	def grab_rank(self):
		return self.rank

	def draw(self):
		print "%s %s"%(self.suit, self.rank)

class Hand:
	
	def __init__(self):
		self.cards = []
		self.calue = 0
		self.ace = False #aces can be 1 or 11 so needto define it

	def __str__(self):
		hand_comp = ""

		for card in self.cards:
			card_name = card.__str__()
			hand_comp += " " + card_name

		return 'The hand has %s' %hand_comp

	def card_add(self, card):
		#Add  another card to the hand 
		self.cards.append(card)
		#check for aces
		if card.rank == 'A':
			self.ace = True
		self.value += card_val[card.rank]

	def calc_self(self):
		if(self.ace == True and self.value < 12):
			return self.value + 10
		else:
			return self.value
	
	def draw(self.hidden):
		if hidden == True and playing == True:
			#Don show first hidden card
			starting_card = 1
		else:
			starting_card = 0
			for x in range(starting_card, len(self.cards)):
				self.cards[x].draw()

class Deck:
	def __init__(self):
		#create a dec in order
		self.deck = []
		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit, rank))

	def shuffle(self):
		#sheffle the deck
		random.shuffle(self.deck)

	def deal(self):
		#Grab the first item in the deck
		single_card = self.deck.pop()
		return single_card

	def __str__(self):
		deck_comp = ""
		for card   in self.cards:
			deck_comp += " " + deck_comp.__str__()
		return "The deck has %s"%(deck_comp)