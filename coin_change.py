class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cents_prime = amount
        num = 0
        coins.sort()
        coins_reverse = coins[::-1]
        
        if cents_prime == 0:
          return 0
        else:
          for coin in coins_reverse:
            if cents_prime == 0:
              break
            num = num + cents_prime/coin
            cents_prime = cents_prime - (cents_prime/coin)*coin
        if cents_prime != 0:
          return -1
        else:
          return num

