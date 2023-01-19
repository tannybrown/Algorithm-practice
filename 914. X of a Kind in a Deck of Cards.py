class Solution(object):
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        if len(deck) == 1 :
            return False
        deck.sort()
        cur = deck[0]
        count = 1
        arr = []
        for item in deck[1:] :
            if cur == item :
                count += 1
            else : 
                arr.append(count)
                cur = item
                count = 1
        if count > 1 :
            arr.append(count)
        cur = arr[0]
        for item in arr[1:] :
            if gcd(cur,item) == 1 :
                return False
            else :
                cur = gcd(cur,item)
        return True
