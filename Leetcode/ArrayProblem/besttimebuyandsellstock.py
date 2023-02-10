# Best Time to Buy and Sell Stock
# Given an array of integers where the ith integer represents the price of the stock on day i, return the largest possible profit from completing one transaction (i.e. buying 1 share and selling 1 share).
# Examples: Given the following prices...

# // Buy on day 1 and sell on day 5 for a profit of 5 - 1 = 4. 
# prices = [1, 2, 3, 4, 5], return 4. 
# // Buy on day 4 and sell on day 9 for a profit of 11 - 1 = 10. 
# prices = [4, 5, 2, 1, 6, 10, 4, 9, 11], return 10. 
# // Buying and selling the stock at any point would yield a negative profit. 
# prices = [33, 18, 8, 2], return 0 




# This implementation uses the peak valley approach to
# find the maximum profit possible from one transaction.
#  It loops through the prices array, keeping track of the
# minimum price seen so far and the maximum profit that
# can be made by selling at the current price.
# It returns the maximum profit after the loop is 
# finished. This should work for any input array of prices.

# PEAK-VALLEY APPROACH
# involves identifying the peaks and valleys of stock prices, and buying stocks when they 
# are at a low (valley)  and selling them when they reach a high (peak).

# The peak valley approach is a simple algorithm for finding the maximum profit.
# It is used to find the maximum difference between two numbers in a given array.
# The algorithm loops through the array and keeps track of the minimum price seen so far.
# It also keeps track of the maximum profit that can be made by selling at the current price.
# The algorithm returns the maximum profit after the loop is finished.
def buy_sell_stock(prices):
    
    min_price = float('inf')
    max_profit = 0
   
   
    for Current_Price in prices:
        min_price = min(min_price , Current_Price) 
    # print("min_price", min_price)
       
        max_profit = max(max_profit , Current_Price - min_price)
        # how is it able to keep track of the index of the min_price and the max_profit?
        # it is because the min_price and max_profit are not the actual values of the prices
        # but the difference between the current price and the min_price



    return  print(max_profit)


if __name__ == "__main__":
    buy_sell_stock([1, 2, 3, 4, 5])
    buy_sell_stock([4, 5, 2, 1, 6, 10, 4, 9, 11])
    buy_sell_stock([33, 18, 8, 2])