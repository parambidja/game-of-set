import unittest
from DeckOfCards import DeckOfCards
from PlaySetWar import *


class TestSetWar(unittest.TestCase):
    def test_1(self):

        # basic functionality tests
        d = DeckOfCards([0,1,2,3,4,5,6,7,8])
        p = d.deal(3)
        assert(d.isEmpty())
        assert([p[0].dealTop() for i in range(3)] == [6,3,0])
        assert([p[1].dealTop() for i in range(3)] == [7,4,1])
        assert([p[2].dealTop() for i in range(3)] == [8,5,2])
        assert(p[0].isEmpty())
        assert(p[1].isEmpty())
        assert(p[2].isEmpty())

        d = DeckOfCards("1 2 3 4 12 31 0 12")
        assert(d.dealTop() == '1') 
        assert(d.dealTop() == '2') 
        assert(d.dealTop() == '3') 
        assert(d.dealBottom() == '12') 
        assert(d.size() == 4) 
        d.addBottom('314')
        assert(d.size() == 5) 
        d.addTop('900')
        assert(d.size() == 6)
        assert(d.dealTop() == '900') 
        assert(d.dealBottom() == '314')

        p = DeckOfCards("100 200 300 400 500")
        d.addPileBottom(p)
        assert(d.size() == 9)
        assert(p.isEmpty())
        assert(d.dealTop() == "4") 
        assert(d.dealBottom() == "500") 
        assert(d.dealTop() == "12") 
        assert(d.dealBottom() == "400") 
        assert(d.dealBottom() == "300")
        assert(p.size() == 0)

        ##Intialize an empty deck
        d = DeckOfCards()
        assert(d.isEmpty())

        ##dealTop and dealBottom tests
        k = DeckOfCards("100 200")
        assert(k.dealTop() == '100')
        assert(k.dealTop() == '200')
        
        s = "111 222 333 444 555 666 777 888 999"
        d = DeckOfCards(s.split())
        assert(not d.isEmpty())
        assert(d.dealTop() == '111')
        assert(d.dealBottom() == '999')
        assert(d.dealTop() == '222')
        assert(d.dealBottom() == '888')
        assert(d.dealTop() == '333')
        assert(d.dealBottom() == '777')
        assert(d.dealBottom() == '666')
        assert(d.dealBottom() == '555')
        assert(d.dealTop() == '444')
        assert(d.isEmpty())

        ##addTop tests
        d = DeckOfCards([3, 4, 5, 6, 7, 8])
        d.addTop(2)
        d.addTop(1)
        assert(d.dealTop() == 1)
        assert(d.dealTop() == 2)
        assert(d.dealTop() == 3)

        ##addBottom tests
        d = DeckOfCards([1,2,3])
        d.addBottom(4)
        d.addBottom(5)
        assert(d.dealBottom() == 5)
        assert(d.dealBottom() == 4)
        assert(d.dealBottom() == 3)

        ##addPileTop tests
        p = DeckOfCards([1,2])
        d = DeckOfCards([3,4])
        d.addPileTop(p)
        assert(p.isEmpty())
        assert(d.dealTop() == 1)
        assert(d.dealTop() == 2)
        assert(d.dealTop() == 3)
        assert(d.dealTop() == 4)
        assert(d.isEmpty())

        ##addPileBottom tests
        p = DeckOfCards([3,4])
        d = DeckOfCards([1,2])
        d.addPileBottom(p)
        assert(p.isEmpty())
        assert(d.dealTop() == 1)
        assert(d.dealTop() == 2)
        assert(d.dealTop() == 3)
        assert(d.dealTop() == 4)
        assert(d.isEmpty())

        ## isEmpty tests
        d = DeckOfCards([1,2])
        assert(not d.isEmpty())
        d = DeckOfCards()
        assert(d.isEmpty())
        d = DeckOfCards([])
        assert(d.isEmpty())

        ## deal tests
        d = DeckOfCards([0,1,2,3,4,5,6,7])
        p = d.deal(2)
        assert(d.isEmpty())
        assert([p[0].dealTop() for i in range(4)] == [6,4,2,0])
        assert([p[1].dealTop() for i in range(4)] == [7,5,3,1])
        assert(p[0].isEmpty())
        assert(p[1].isEmpty())

        d = DeckOfCards([0,1,2,3,4,5,6,7,8])
        p = d.deal(3)
        assert(d.isEmpty())
        assert([p[0].dealTop() for i in range(3)] == [6,3,0])
        assert([p[1].dealTop() for i in range(3)] == [7,4,1])
        assert([p[2].dealTop() for i in range(3)] == [8,5,2])
        assert(p[0].isEmpty())
        assert(p[1].isEmpty())
        assert(p[2].isEmpty())

        s = "a b c d"
        d = DeckOfCards(s.split())
        assert(not d.isEmpty())
        assert(d.dealTop() == 'a')
        assert(d.dealTop() == 'b')
        assert(d.dealTop() == 'c')
        assert(d.dealTop() == 'd')
        assert(d.isEmpty())

        d = DeckOfCards([0,1,2,3,4,5,6])
        p = d.deal(2)
        assert(d.isEmpty())
        assert([p[0].dealTop() for i in range(4)] == [6,4,2,0])
        assert([p[1].dealTop() for i in range(3)] == [5,3,1])
        assert(p[0].isEmpty())
        assert(p[1].isEmpty())

        # game tests
        assert(play(2,"0000 1111 1000 2222 1112 0001 0120 2220") == "Player 0 won in 4 rounds.")
        assert(play(2,"0020 2220 1222 0211 2112 1012 1020 1000 1121 1110 1111 0200 0201 0220 0021 0001 2022 0000 1210 2120 2021 1100 2122 2102 1212 0222 0110 1022 0202 2201 2210 0122 2101 1202 2020 0101 0011 0112 0012 1220 2221 1002 1201 1101 2011 1021 0102 0210 2010 2222 0121 2212 0002 2000 1221 0221 1211 1120 1200 1010 0010 1011 2211 2111 2202 2012 1112 2121 0022 1122 1102 2110 0111 2100 2002 2200 0120 1001 0212 0100 2001") == "Player 1 won in 22 rounds.")
        assert(play(2,"2001 0100 0212 1001 0120 2200 2002 2100 0111 2110 1102") == "Player 0 won in 1 round.")
        self.assertRaises(TypeError, play, 'abc', "0000 0000")
        q = "2000 1221 0221 1211 1120 1200 1010 0010 1011 2211 2111 2202 2012 1112 2121 0022 1122 1102 2110 0111 2100 2002 2200 0120 1001 0212 0100 2001 0020 2220 1222 0211 2112 1012 1020 1000 1121 1110 1111 0200 0201 0220 0021 0001 2022 0000 1210 2120 2021 1100 2122 2102 1212 0222 0110 1022 0202 2201 2210 0122 2101 1202 2020 0101 0011 0112 0012 1220 2221 1002 1201 1101 2011 1021 0102 0210 2010 2222 0121 2212 0002"
        assert(play(4,q) == "Player 0 won in 210 rounds.")
        



unittest.main()
            
