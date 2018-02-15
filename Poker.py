#  File: Poker.py

#  Description: This program simulates a simple game of poker between a user defined number of players.

#  Student's Name: Mathew Perez

#  Student's UT EID: mjp3457

#  Partner's Name: Samuel Gutierrez

#  Partner's UT EID: sfg384

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 2/04/2018

#  Date Last Modified: 2/09/2018

import random

#This comment line is a test

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  #Convert card suit and number values to string
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)
  
  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):

    return (self.rank >= other.rank)
  
    

class Deck (object):
  def __init__ (self):
    #create empty deck list
    self.deck = []
    #populate the deck
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  #shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  #give out one card from top of deck
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    #create actual deck object
    self.deck = Deck()
    #shuffle actual deck object
    self.deck.shuffle()
    #create object to represent every player hand in the game
    self.players = []
    #create poker rule in the game
    numcards_in_hand = 5

    
    for i in range (num_players):
      #temporarily create everyone's individual hand
      hand = []
      #populate every individual hand
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      #append every hand to object representation for every hand in the game list
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      #convert every hand to string to print
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str(i + 1) + " : " + hand)

    # determine each type of hand and print
     # create list to store points for each hand 
    everyones_points = []
    hands = []
    print()
    
    #total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
    
    for i in range(len(self.players)):
      single_hand_points = []
      if (self.is_royal(self.players[i])):
        print ('Player ' + str(i+1) + " : Royal Flush")
        hands.append(10)
        #
        single_hand_points.append(10 * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank + 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank + 13 + self.players[i][4].rank)
        everyones_points.append(single_hand_points)
      elif (self.is_straight_flush(self.players[i])):
        print ('Player ' + str(i+1) + " : Straight Flush")
        hands.append(9)
        #
        single_hand_points.append(9 * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank + 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank + 13 + self.players[i][4].rank)
        everyones_points.append(single_hand_points)
      elif (self.is_four_kind(self.players[i])):
        print ('Player ' + str(i+1) + " : Four of a Kind")
        hands.append(8)
        #c1, c2, c3, and c4 are the ranks of the four of a kind cards and c5 is the side card. 
        single_hand_points = self.four_kind_points(self.players[i])
        everyones_points.append(single_hand_points)
      elif (self.is_full_house(self.players[i])):
        print ('Player ' + str(i+1) + " : Full House")
        hands.append(7)
        #c1, c2, and c3 are the ranks of the three cards having the same rank and c4 and c5 are the ranks of the two remaining cards having the same rank.
        single_hand_points = self.full_house_points(self.players[i])
        everyones_points.append(single_hand_points)
      elif (self.is_flush(self.players[i])):
        print ('Player ' + str(i+1) + " : Flush")
        hands.append(6)
        #
        single_hand_points = (6 * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank + 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank + 13 + self.players[i][4].rank)
        everyones_points.append(single_hand_points)
      elif (self.is_straight(self.players[i])):
        print ('Player ' + str(i+1) + " : Straight")
        hands.append(5)
        #
        single_hand_points = (5 * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank + 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank + 13 + self.players[i][4].rank)
        everyones_points.append(single_hand_points)
      elif (self.is_three_kind(self.players[i])):
        print ('Player ' + str(i+1) + " : Three of a Kind")
        hands.append(4)
        #
        single_hand_points = self.three_kind_points(self.players[i])
        everyones_points.append(single_hand_points)
      elif (self.is_two_pair(self.players[i])):
        print ('Player ' + str(i+1) + " : Two Pair")
        single_hand_points = self.two_pair_points(self.players[i])
        hands.append(3)
        everyones_points.append(single_hand_points)
      elif (self.is_one_pair(self.players[i])):
        print ('Player ' + str(i+1) + " : One Pair")
        hands.append(2)
        single_hand_points = self.one_pair_points(self.players[i])
        everyones_points.append(single_hand_points)
      elif (self.is_high_card(self.players[i])):
        print ('Player ' + str(i+1) + " : High Card")
        hands.append(1)
        single_hand_points = (1 * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank + 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank + 13 + self.players[i][4].rank)
        everyones_points.append(single_hand_points)


    tie_list = []
    max_var = max(everyones_points)
    index_var = everyones_points.index(max_var)
    x = 0
    print()
    #find max in tie hand list
    max2 = max(hands)
    #take this max value out to not re reference it
    index_var2 = hands.index(max2)
    hands[index_var2] = 0
    tie_list.append(index_var2 + 1)
    for x in hands:
      index_var3 = 0
      if x == max2:
        index_var3 = hands.index(x)
        tie_list.append(index_var3 + 1)
        hands[index_var3] = 0

    
    
    if len(tie_list) == 1:
      print("Player " + str(index_var + 1) + " wins.")
    #else:
    else:
      tie_points = []
      for x in tie_list:
        tie_points.append(everyones_points[x-1])
      tie_points = sorted (tie_points, reverse = True)
      for c in tie_points:
        tie_num = int(everyones_points.index(c)) + 1
        print("Player", tie_num, "ties")
          
    

  # determine if a hand is a royal flush 
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    return (same_suit and rank_order)

  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

    if (not same_suit):
      return False

    num_order = True
    #correct function to (hand[i].rank = (hand[i+1].rank + 1))
    for i in range(len(hand)-1):
      num_order = num_order and (hand[i].rank == (1 + hand[i+1].rank))

    return (same_suit and num_order)

  def is_four_kind (self, hand):
    for i in range(len(hand)-3):
      if (hand[i].rank == hand[i+1].rank) and (hand[i].rank == hand[i+2].rank) and (hand[i].rank == hand[i+3].rank):
        return True
    return False

  ##############
  def four_kind_points (self, hand):
    
    if (hand[i].rank == hand[i+1].rank) and (hand[i].rank == hand[i+2].rank) and (hand[i].rank == hand[i+3].rank):
      point = (8 * 13**5 + hand[0].rank * 13**4 + hand[1].rank + 13**3 + hand[2].rank * 13**2 + hand[3].rank + 13 + hand[4].rank)
      return point
    elif (hand[i + 1].rank == hand[i+2].rank) and (hand[i+1].rank == hand[i+3].rank) and (hand[i+1].rank == hand[i+4].rank):
      point = (8 * 13**5 + hand[1].rank * 13**4 + hand[2].rank + 13**3 + hand[3].rank * 13**2 + hand[4].rank + 13 + hand[0].rank)
      return point
    

  def is_full_house (self, hand):
    fh_seq1 = (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank == hand[4].rank)
    fh_seq2 = (hand[0].rank == hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)
    return fh_seq1 or fh_seq2

  ###########
  def full_house_points(self, hand):
    
    if (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank == hand[4].rank):
      point = (7 * 13**5 + hand[2].rank * 13**4 + hand[3].rank + 13**3 + hand[4].rank * 13**2 + hand[0].rank + 13 + hand[1].rank)
      return point
    elif (hand[0].rank == hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank):
      point = (7 * 13**5 + hand[0].rank * 13**4 + hand[1].rank + 13**3 + hand[2].rank * 13**2 + hand[3].rank + 13 + hand[4].rank)
      return point
    
  def is_flush (self, hand):
    same_suit = True
    for i in range(len(hand)-1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
    return same_suit

  def is_straight (self, hand):
    for i in range(len(hand)-1):
      if (hand[i].rank != (1 + hand[i+1].rank)):
        return False
    return True

  def is_three_kind (self, hand):
    for i in range(len(hand)-2):
      if (hand[i].rank == hand[i+1].rank == hand[i+2].rank):
        return True
    return False

  ########
  def three_kind_points(self, hand):
    
    if (hand[0].rank == hand[1].rank == hand[2].rank):
      point = (4 * 13**5 + hand[0].rank * 13**4 + hand[1].rank + 13**3 + hand[2].rank * 13**2 + hand[3].rank + 13 + hand[4].rank)
      return point
    elif(hand[1].rank == hand[2].rank == hand[3].rank):
      point = (4 * 13**5 + hand[1].rank * 13**4 + hand[2].rank + 13**3 + hand[3].rank * 13**2 + hand[0].rank + 13 + hand[4].rank)
      return point
    else:
      point = (4 * 13**5 + hand[2].rank * 13**4 + hand[3].rank + 13**3 + hand[4].rank * 13**2 + hand[0].rank + 13 + hand[1].rank)
      return point

  def is_two_pair (self, hand):
    tp_seq1 = (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank)
    tp_seq2 = (hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)
    tp_seq3 = (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank)
    return tp_seq1 or tp_seq2

  ########
  def two_pair_points(self, hand):
    
    tp_seq1 = (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank)
    tp_seq2 = (hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)
    tp_seq3 = (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank)
    if tp_seq1 == True:
      point = (3 * 13**5 + hand[0].rank * 13**4 + hand[1].rank + 13**3 + hand[2].rank * 13**2 + hand[3].rank + 13 + hand[4].rank)
      return point
    elif tp_seq2 == True:
      point = (3 * 13**5 + hand[1].rank * 13**4 + hand[2].rank + 13**3 + hand[3].rank * 13**2 + hand[4].rank + 13 + hand[0].rank)
      return point
    else:
      point = (3 * 13**5 + hand[0].rank * 13**4 + hand[1].rank + 13**3 + hand[3].rank * 13**2 + hand[4].rank + 13 + hand[2].rank)
      return point

  # determine if a hand is one pair
  def is_one_pair(self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i+1].rank):
        return True
    return False

  ######
  def one_pair_points(self, hand):
    
    
    if (hand[0].rank == hand[1].rank):
      point = (2 * 13**5 + hand[0].rank * 13**4 + hand[1].rank + 13**3 + hand[2].rank * 13**2 + hand[3].rank + 13 + hand[4].rank)
      return point
    elif(hand[1].rank == hand[2].rank):
      point = (2 * 13**5 + hand[1].rank * 13**4 + hand[2].rank + 13**3 + hand[0].rank * 13**2 + hand[3].rank + 13 + hand[4].rank)
      return point
    elif (hand[2].rank == hand[3].rank):
      point = (2 * 13**5 + hand[2].rank * 13**4 + hand[3].rank + 13**3 + hand[0].rank * 13**2 + hand[1].rank + 13 + hand[4].rank)
      return point
    else:
      point = (2 * 13**5 + hand[3].rank * 13**4 + hand[4].rank + 13**3 + hand[0].rank * 13**2 + hand[1].rank + 13 + hand[2].rank)
      return point
  

  def is_high_card (self, hand):
    return (not self.is_royal(hand)) and (not self.is_straight_flush(hand)) and (not self.is_four_kind(hand)) and (not self.is_full_house(hand)) and (not self.is_flush(hand)) and (not self.is_straight(hand)) and (not self.is_three_kind(hand)) and (not self.is_two_pair(hand)) and (not self.is_one_pair(hand))

def main ():
  # prompt user to enter number of players
  print()
  num_players = int(input("Enter number of players: "))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int(input("Enter number of players: "))
  print()

  # create the Poker object
  game = Poker (num_players)
  points = []
  # play the game (poker)
  game.play()
  

main()
