#
#Counting change example translated from Scheme to Python 2
#From Structure and Interpretation of Computer Programs
#Chapter 1.2.2: Tree Recursion
#
#Problem Statement:
#How many different ways can we make change of $1.00, given half-dollars, 
#quarters, dimes, nickels, and pennies? More generally, can we write a procedure
#to compute the number of ways to change any given amount of money?
#
#Online:
#http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.2
#

def count_change(amount):
    return cc(amount, 5)

def cc(amount, kindsOfCoins):
    if amount == 0:
        return 1
    if amount < 0 or kindsOfCoins == 0:
        return 0
    
    return cc(amount, kindsOfCoins - 1) + \
            cc((amount - first_denomination(kindsOfCoins)), kindsOfCoins)

def first_denomination(kindsOfCoins):
    if kindsOfCoins == 1: return 1
    if kindsOfCoins == 2: return 5
    if kindsOfCoins == 3: return 10
    if kindsOfCoins == 4: return 25
    if kindsOfCoins == 5: return 50
    
print count_change(100)



#cc with memoization

def cc_with_memo(amount, kindsOfCoins, memo = {}):
    
    if (amount, kindsOfCoins) in memo:
        return memo[(amount, kindsOfCoins)]
    
    if amount == 0:
        return 1
    if amount < 0 or kindsOfCoins == 0:
        return 0
    
    memo[(amount, kindsOfCoins)] = cc_with_memo(amount, kindsOfCoins - 1) + \
         cc_with_memo((amount - first_denomination(kindsOfCoins)), kindsOfCoins)

    return cc_with_memo(amount, kindsOfCoins, memo)

