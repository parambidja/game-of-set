class Node:
    def __init__(self,d,p = None,n = None):
        self.data = d
        self.next = n
        self.prev = p

    def get_prev(self):
        return self.prev

    def set_prev(self, p):
        self.prev = p

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class DeckOfCards():
    def __init__(self, L = None):
        self.length = 0
        self.head = None
        self.tail = None

        if type(L) == str:
            temp = L.split()
            for i in temp:
                self.addBottom(i)
        if type(L) == list:
            for i in L:
                self.addBottom(i)


    def dealTop(self):
        if self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return old_head.get_data()
        else:
            old_head = self.head
            new_head = old_head.get_next()
            new_head.set_prev(None)
            self.head = new_head
            self.length = self.length - 1
            return old_head.get_data()


    def dealBottom(self):
        if self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return old_head.get_data()
        else:
            old_tail = self.tail
            new_tail = old_tail.get_prev()
            new_tail.set_next(None)
            self.tail = new_tail
            self.length = self.length - 1
            return old_tail.get_data()
        

    def addTop(self,card):
        new = Node(card)

        if self.head is None:
            self.head = new
            self.tail = new
            self.length = self.length + 1

        else:
            old_head = self.head
            new_head = new
            new_head.set_next(old_head)
            old_head.set_prev(new_head)
            self.head = new_head
            self.length = self.length + 1

    

    def addBottom(self,card):
        new = Node(card)

        if self.head is None or self.tail is None:
            self.head = new
            self.tail = new
            self.length = self.length + 1
            
        else:
            self.tail.set_next(new)
            new.set_prev(self.tail)
            self.tail = new
            self.length = self.length + 1


    def addPileTop(self, pile):
        old_head = self.head

        if old_head is None:
            self.head = pile.head
            self.tail = pile.tail
            self.length = pile.length
        else:
            new_head = pile.head
            pile.tail.set_next(old_head)
            self.head = new_head
            self.length = self.length + pile.length

        pile.length = 0
        pile.head = None
        pile.tail = None

    def addPileBottom(self, pile):
        old_tail = self.tail
        
        if old_tail is None:
           self.head = pile.head
           self.tail = pile.tail
           self.length = pile.length
        else:
            new_tail = pile.tail
            pile.head.set_prev(old_tail)
            old_tail.set_next(pile.head)
            self.tail = new_tail
            self.length = self.length + pile.length

        pile.length = 0
        pile.head = None
        pile.tail = None

    def get_tail(self):
        return self.tail.get_data()
        

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def deal(self, nplayers, ncards = None):
        hands = []
        for i in range(nplayers):
            hands.append(DeckOfCards())
        
        if ncards == None:
            for i in range(self.length):
                hands[i % nplayers].addTop(self.dealTop())
        else:
            for i in range(ncards):
                hands[i % nplayers].addTop(self.dealTop())

        return hands

    

class SetDeck(DeckOfCards):
    def __init__(self,L=[]):
        DeckOfCards.__init__(self, L)

    def linked_list_to_string(self):
        card_string = ""
        temp_list = self
        current = self.head
        index = 0

        while index < self.length:
            card_string = card_string + " " + current.get_data()
            current = current.get_next()
            index = index + 1
            
        return card_string
    
    def generate_last_card(self,n1,n2):  #takes two strings (which are #s)
                                         #returns the number (as a string) to fulfill that set
        third_card = ""
        
        for i in range(len(n1)):
            temp1 = int(n1[i])      
            temp2 = int(n2[i])
            num = str((-temp1 - temp2) % 3)     #the sum of any three digit combinations is always perfectly divisible by 3
            third_card = third_card + num
        return third_card

    def check_set(self):
        list_of_cards = self.linked_list_to_string().split()

        my_dictionary = {}  #chose dictionary for its ability to add and search for a key in constant time
        
        for i in range(len(list_of_cards)):
            for j in my_dictionary:
                if self.generate_last_card(list_of_cards[i],j) in my_dictionary:
                    return True
            my_dictionary[list_of_cards[i]] = i+1
        return False
                






        
        


