import math
from Utils import Timer

class NumberUtils:

    # ----------- FACTOR FUNCTION --------------
    def factor(self, n):
        factorList = []
        for i in range(1, n + 1):
            if n % i == 0:
                factorList.append(i)
        return factorList

    # ----------- PRIME CHECK BASIC -------------
    def prime(self, n):
        return len(self.factor(n)) == 2

    # ----------- GENERATE PRIME LIST ------------
    def prime_list(self, start, end):
        primeList = []
        for i in range(start, end + 1):
            if self.prime(i):
                primeList.append(i)
        return primeList

    # ----------- OPTIMIZED PRIME CHECK (Version 1) -------------
    def prime1(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # ----------- OPTIMIZED PRIME CHECK (Break on first factor) ------------
    def prime2(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # ----------- HIGHLY OPTIMIZED PRIME CHECK (Use sqrt) --------
    def prime3(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # ----------- NORMAL GCD ----------------
    def gcd_basic(self, m, n):
        common = []
        for i in range(1, min(m, n) + 1):
            if m % i == 0 and n % i == 0:
                common.append(i)
        return common[-1]

    # ----------- RECURSIVE GCD VERSION --------
    def gcd1(self, m, n):
        a, b = max(m, n), min(m, n)
        if a % b == 0:
            return b
        else:
            return self.gcd1(b, a - b)

    # ----------- EUCLID'S GCD (BEST METHOD) -----------
    def gcd_euclid(self, m, n):
        a, b = max(m, n), min(m, n)
        if b == 0:
            return a
        return self.gcd_euclid(b, a % b)

    # --------------------------------------------------
    #          TIMER FUNCTION (INSIDE SAME CLASS)
    # --------------------------------------------------


    # ----------- TEST TIMER -------------------
    def test_timer(self):
        t =  Timer.Timer()
        n = 0
        dist = {}
        for j in range(4, 9):
            t.start()
            for i in range(10 ** j):
                n = n + i
            t.end()
            dist[j] = t.show_elapsed_time()
        return (dist)

