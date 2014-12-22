#  File: Poker.py

#  Description: Simulates a game of 5-card Poker and determines winner

#  Student's Name: Evan Johnston

#  Student's UT EID: eaj628

#  Course Name: CS 313E 

#  Unique Number: 53580

#  Date Created: 2/4/14

#  Date Last Modified:2/14

import random

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

  def __str__ (self):
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

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
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)
      
class Poker (object):
  def __init__ (self, numHands):
    self.deck = Deck()
    self.deck.shuffle()
    self.hands = []
    numCards_in_Hand = 5

    for i in range (numHands):
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  def play (self):
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '       
      print ('Hand ' + str(i + 1) + ': ' + hand)
    print ('')

    pointList=[]
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '

      # this set of conditionals determines the values of c1-c5 used in the
      # given scoring formula, while determining the classification of the hand
        
      if self.is_royal(hand)>0:
        h=self.is_royal(hand)
        c1=sortedHand[0].rank
        c2=sortedHand[1].rank
        c3=sortedHand[2].rank
        c4=sortedHand[3].rank
        c5=sortedHand[4].rank
        print ('Hand '+str(i+1)+': Royal Flush')

      elif self.is_straight_flush(hand)>0:
        h=self.is_straight_flush(hand)
        c1=sortedHand[0].rank
        c2=sortedHand[1].rank
        c3=sortedHand[2].rank
        c4=sortedHand[3].rank
        c5=sortedHand[4].rank
        print ('Hand '+str(i+1)+': Straight Flush')

      elif self.is_four(hand)>0:
        h=self.is_four(hand)
        if sortedHand[0].rank>sortedHand[1].rank:
          c1=sortedHand[1].rank
          c2=sortedHand[2].rank
          c3=sortedHand[3].rank
          c4=sortedHand[4].rank
          c5=sortedHand[0].rank
        else:
          c1=sortedHand[0].rank
          c2=sortedHand[1].rank
          c3=sortedHand[2].rank
          c4=sortedHand[3].rank
          c5=sortedHand[4].rank
        print ('Hand '+str(i+1)+': Four of a Kind')

      elif self.is_full(hand)>0:
        h=self.is_full(hand)
        if sortedHand[0].rank>sortedHand[2].rank:
          c1=sortedHand[2].rank
          c2=sortedHand[3].rank
          c3=sortedHand[4].rank
          c4=sortedHand[0].rank
          c5=sortedHand[1].rank
        else:
          c1=sortedHand[0].rank
          c2=sortedHand[1].rank
          c3=sortedHand[2].rank
          c4=sortedHand[3].rank
          c5=sortedHand[4].rank
        print ('Hand '+str(i+1)+': Full House')

      elif self.is_flush(hand)>0:
        h=self.is_flush(hand)
        c1=sortedHand[0].rank
        c2=sortedHand[1].rank
        c3=sortedHand[2].rank
        c4=sortedHand[3].rank
        c5=sortedHand[4].rank
        print ('Hand '+str(i+1)+': Flush')

      elif self.is_straight(hand)>0:
        h=self.is_straight(hand)
        c1=sortedHand[0].rank
        c2=sortedHand[1].rank
        c3=sortedHand[2].rank
        c4=sortedHand[3].rank
        c5=sortedHand[4].rank
        print ('Hand '+str(i+1)+': Straight')

      elif self.is_three(hand)>0:
        h=self.is_three(hand)
        
        if sortedHand[0].rank==sortedHand[1].rank and sortedHand[2].rank!=sortedHand[3].rank:
          c1=sortedHand[0].rank
          c2=sortedHand[1].rank
          c3=sortedHand[2].rank
          c4=sortedHand[3].rank
          c5=sortedHand[4].rank                       
          
        elif sortedHand[1].rank==sortedHand[2].rank and sortedHand[0].rank!=sortedHand[1].rank:
          c1=sortedHand[1].rank
          c2=sortedHand[2].rank
          c3=sortedHand[3].rank
          c4=sortedHand[4].rank
          c5=sortedHand[0].rank

        elif sortedHand[2].rank==sortedHand[3].rank and sortedHand[1].rank!=sortedHand[2].rank:
          c1=sortedHand[2].rank
          c2=sortedHand[3].rank
          c3=sortedHand[4].rank
          c4=sortedHand[0].rank
          c5=sortedHand[1].rank
        
        print ('Hand '+str(i+1)+': Three of a Kind')

      elif self.is_two(hand)>0:
        h=self.is_two(hand)

        if sortedHand[0].rank==sortedHand[1].rank and sortedHand[2].rank==sortedHand[3].rank:
            c1=sortedHand[0].rank
            c2=sortedHand[1].rank
            c3=sortedHand[2].rank
            c4=sortedHand[3].rank
            c5=sortedHand[4].rank
          
        elif sortedHand[1].rank==sortedHand[2].rank and sortedHand[3].rank==sortedHand[4].rank:
            c1=sortedHand[1].rank
            c2=sortedHand[2].rank
            c3=sortedHand[3].rank
            c4=sortedHand[4].rank
            c5=sortedHand[0].rank
          
        elif sortedHand[0].rank==sortedHand[1].rank and sortedHand[3].rank==sortedHand[4].rank:
            c1=sortedHand[0].rank
            c2=sortedHand[1].rank
            c3=sortedHand[3].rank
            c4=sortedHand[4].rank
            c5=sortedHand[2].rank
        
        print ('Hand '+str(i+1)+': Two Pair')

      elif self.is_one(hand)>0:
        h=self.is_one(hand)
        
        if sortedHand[0].rank==sortedHand[1].rank:
          c1=sortedHand[0].rank
          c2=sortedHand[1].rank
          c3=sortedHand[2].rank
          c4=sortedHand[3].rank
          c5=sortedHand[4].rank
          
        elif sortedHand[1].rank==sortedHand[2].rank:
          c1=sortedHand[1].rank
          c2=sortedHand[2].rank
          c3=sortedHand[0].rank
          c4=sortedHand[3].rank
          c5=sortedHand[4].rank
          
        elif sortedHand[2].rank==sortedHand[3].rank:
          c1=sortedHand[2].rank
          c2=sortedHand[3].rank
          c3=sortedHand[0].rank
          c4=sortedHand[1].rank
          c5=sortedHand[4].rank
          
        elif sortedHand[3].rank==sortedHand[4].rank:
          c1=sortedHand[3].rank
          c2=sortedHand[4].rank
          c3=sortedHand[0].rank
          c4=sortedHand[1].rank
          c5=sortedHand[2].rank

        print ('Hand '+str(i+1)+': One Pair')

      else:
        h=self.is_high(hand)
        c1=sortedHand[0].rank
        c2=sortedHand[1].rank
        c3=sortedHand[2].rank
        c4=sortedHand[3].rank
        c5=sortedHand[4].rank        
        print ('Hand '+str(i+1)+': High Card')
      
      total_points = h * 13^5 + c1 * 13^4 + c2 * 13^3 + c3 * 13^2 + c4 * 13 + c5
      pointList.append(total_points)
      
    winner=max(pointList)
    handIdx=pointList.index(winner)
    print ('')
    print ('Hand '+str(handIdx+1)+' wins.')

    # from pointList, which is a list of all the total point values from each hand,
    # the index of the highest value is found and that indicates the highest scoring
    # hand


    # all functions below have a similar, taylored beginning section in which
    # the suit and/or rank (depending on what is relevant to the function) are
    # taken from the 'hand' input, which is a string created in play of all the
    # cards in the hand
             
  def is_royal (self, hand):
    hand=hand.split()
    royalRanks=['10','J','Q','K','A']
    royalCount=0
    royalSuits=[]
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
        suit=hand[i][2]
      else:
        rank=hand[i][0]
        suit=hand[i][1]
      if rank in royalRanks:
        royalCount+=1
      royalSuits.append(suit)
    if ((royalCount==5) and (royalSuits.count('S')==5 or royalSuits.count('H')==5 or\
       royalSuits.count('D')==5 or royalSuits.count('C')==5)):
      # if all cards have the same suit and are in the royalRanks list, it is royal
      
      return 10
    else:
      return 0

  def is_straight_flush (self, hand):
    handSt=hand
    hand=hand.split()
    straightFlusSuits=[]
    straightFlushRanks=[]
    rankOrder=False
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
        suit=hand[i][2]
      else:
        rank=hand[i][0]
        suit=hand[i][1]
      straightFlusSuits.append(suit)
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      straightFlushRanks.append(rank)
      straightFlushRanks.sort()
    if (straightFlushRanks[0]+1==straightFlushRanks[1]) and (straightFlushRanks[0]+2==straightFlushRanks[2]) and\
       (straightFlushRanks[0]+3==straightFlushRanks[3]) and (straightFlushRanks[0]+4==straightFlushRanks[4]):
      rankOrder=True
    if rankOrder and (straightFlusSuits.count('S')==5 or straightFlusSuits.count('H')==5 or\
       straightFlusSuits.count('D')==5 or straightFlusSuits.count('C')==5):
      # if the order of the cards in the hand is increasing by one and all are in
      # same suit, hand is straight flush
      return 9
    else:
      return 0

  def is_four (self, hand):
    hand=hand.split()
    fourRanks=[]
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
      else:
        rank=hand[i][0]
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      fourRanks.append(rank)
    if (fourRanks.count(fourRanks[0])==4 or fourRanks.count(fourRanks[1])==4 or\
           fourRanks.count(fourRanks[2])==4 or fourRanks.count(fourRanks[3])==4 or\
           fourRanks.count(fourRanks[4])==4):
      # must be a count of 4 of the same rank for 4-of-a-kind
      return 8
    else:
      return 0
  
  def is_full (self, hand):
    hand=hand.split()
    fullRanks=[]
    threeTest=False
    twoTest=False
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
      else:
        rank=hand[i][0]
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      fullRanks.append(rank)
    if fullRanks.count(fullRanks[0])==3 or fullRanks.count(fullRanks[1])==3 or\
       fullRanks.count(fullRanks[2])==3 or fullRanks.count(fullRanks[3])==3 or\
       fullRanks.count(fullRanks[4])==3:
      threeTest=True
    if fullRanks.count(fullRanks[0])==2 or fullRanks.count(fullRanks[1])==2 or\
       fullRanks.count(fullRanks[2])==2 or fullRanks.count(fullRanks[3])==2 or\
       fullRanks.count(fullRanks[4])==2:
      twoTest=True
    if threeTest and twoTest:
      # a version of 4 of a kind divided into 2 of a kind and 3 of a kind
      # both must be true to be a full house
      return 7
    else:
      return 0
  
  def is_flush (self, hand):
    handSt=hand
    hand=hand.split()
    flushSuits=[]
    for i in range (len(hand)):
      if len(hand[i])>2:
        suit=hand[i][2]
      else:
        suit=hand[i][1]
      flushSuits.append(suit)
    if (flushSuits.count('S')==5 or flushSuits.count('H')==5 or\
       flushSuits.count('D')==5 or flushSuits.count('C')==5):
      return 6
    # all same suits
    else:
      return 0

  def is_straight (self, hand):
    handSt=hand
    hand=hand.split()
    straightRanks=[]
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
      else:
        rank=hand[i][0]
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      straightRanks.append(rank)
      straightRanks.sort()
    if (straightRanks[0]+1==straightRanks[1]) and (straightRanks[0]+2==straightRanks[2]) and\
       (straightRanks[0]+3==straightRanks[3]) and (straightRanks[0]+4==straightRanks[4]):
      return 5
    # all increasing by 1
    else:
      return 0

  def is_three (self, hand):
    handSt=hand
    hand=hand.split()
    fullRanks=[]
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
      else:
        rank=hand[i][0]
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      fullRanks.append(rank)
    if (fullRanks.count(fullRanks[0])==3 or fullRanks.count(fullRanks[1])==3 or\
       fullRanks.count(fullRanks[2])==3 or fullRanks.count(fullRanks[3])==3 or\
       fullRanks.count(fullRanks[4])==3):
      return 4
    # the Three Test from the full house check
    else:
      return 0

  def is_two (self, hand):
    handSt=hand
    hand=hand.split()
    twoPairRanks=[]
    countedList=[]
    pairCount=0
    
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
      else:
        rank=hand[i][0]
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      twoPairRanks.append(rank)
      
    if twoPairRanks.count(twoPairRanks[0])==2:
      countedList.append(twoPairRanks[0])
      pairCount+=1
    if twoPairRanks.count(twoPairRanks[1])==2 and not(twoPairRanks[1] in countedList):
      countedList.append(twoPairRanks[1])
      pairCount+=1
    if twoPairRanks.count(twoPairRanks[2])==2 and not(twoPairRanks[2] in countedList):
      countedList.append(twoPairRanks[2])
      pairCount+=1
    if twoPairRanks.count(twoPairRanks[3])==2 and not(twoPairRanks[3] in countedList):
      countedList.append(twoPairRanks[3])
      pairCount+=1
    if twoPairRanks.count(twoPairRanks[4])==2 and not(twoPairRanks[4] in countedList):
      countedList.append(twoPairRanks[4])
      pairCount+=1
    if pairCount==2:
      # this is just the 2 of a kind check found in the full house function, but
      # in order to prevent a pair from counting twice, a second list (countedList)
      # is compared against ranks that have already been matched to prevent duplication
      return 3
    else:
      return 0
      
  def is_one (self, hand):
    handSt=hand
    hand=hand.split()
    onePairRanks=[]
    countedList=[]
    pairCount=0
    for i in range (len(hand)):
      if len(hand[i])>2:
        rank=hand[i][:2]
      else:
        rank=hand[i][0]
      if rank in ('J','Q','K','A'):
        if rank=='J':
          rank=11
        elif rank=='Q':
          rank=12
        elif rank=='K':
          rank=13
        elif rank=='A':
          rank=14
      else:
        rank=int(rank)
      onePairRanks.append(rank)
    if onePairRanks.count(onePairRanks[0])==2:
      countedList.append(onePairRanks[0])
      pairCount+=1
    if onePairRanks.count(onePairRanks[1])==2 and not(onePairRanks[1] in countedList):
      countedList.append(onePairRanks[1])
      pairCount+=1
    if onePairRanks.count(onePairRanks[2])==2 and not(onePairRanks[2] in countedList):
      countedList.append(onePairRanks[2])
      pairCount+=1
    if onePairRanks.count(onePairRanks[3])==2 and not(onePairRanks[3] in countedList):
      countedList.append(onePairRanks[3])
      pairCount+=1
    if onePairRanks.count(onePairRanks[4])==2 and not(onePairRanks[4] in countedList):
      countedList.append(onePairRanks[4])
      pairCount+=1
    if pairCount==1 :
      # the same process as in 2 pairs, but the needed pairCount is 1 rather than 2
      return 2
    else:
      return 0

  def is_high (self, hand):
      return 1
    # becuase this function is only called if all others fail, there is no need
    # for the function to do anything other than return 1

def main():
  numHands = int (input ('Enter number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    
    numHands = int (input ('Enter number of hands to play: '))
  print ('')
  
  game = Poker (numHands)
  game.play()
main()
