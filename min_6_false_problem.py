def min_false_coin_problem():
    """Function to weigh the coins and find the false coin"""
    #initailize the coins
    coins = [True, True, True, False,True, True]

    #function to simulate the weighing process
    def weigh(group1, group2):
        sum_group1= sum ([ 1 if coins[i] == False else 0 for i in group1])
        sum_group2 = sum([1 if coins[i] == False else 0 for i in group2])

        if sum_group1 == sum_group2:
            #coins in group1 and 2 are balanced
            return 0
        elif sum_group1 > sum_group2:
            return 1 #left side is heavier
        else:
            return -1 #right side is heavier
    #divide coins into groups
    group1 = [0, 1] #coins 1 and 2
    group2 = [2, 3] #coins 3, and 4
    group3 = [4, 5] # coins 5 and 6

    #perform the first weighing
    result = weigh(group1, group2)
    if result == 0:  #coins in group 1 and 2 are balanced then we weighn group3
        result= weigh([4], [5])
        if result == 0:
            print("Theres an error , finding the false coin")
        elif result == 1:
            print("C5 is the false coin")
        else:
            print ("C6 is the false coin")
    else:
        if result == 1: # weigh coin 1 and 3
            result = weigh([0],[2])
            if result == 0:
                print("coin 2 is false coin")
            elif result == 1:
                print("coin is false coin")
            else:
                print("coin 3 is false")
        else:
            result = weigh([1], [3])
            if result == 0:
                print("Coin 4 is false")
            elif result == 1:
                print("Coin2 is unbalanced and it is a false")
            else:
                print("Coin3 is the false coin")
min_false_coin_problem()
#N*N queen problem
#A Function to check if it is safe to place the queen at board[row][col]
def isSafe(mat, row, col):
    n = len(mat)
    #checking if no queens are on the same column or diagnolas
    for i in range(row):
        #check for the same col or if coins are placed on diagnos
        if mat[i] == col or abs(mat[i]- col) == abs(i -row):
            return False #not safe to place the coin
        #checkin for diagnos
    return False
