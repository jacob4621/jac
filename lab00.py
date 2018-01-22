def main():
    maxAmount = 100
    theAmount = [14,6,9,7,8,10,3,9]
    x = 0
    y = 0
    for J in range(len(theAmount)):
        apples = 100/theAmount[J]
        if(J<7):
            cash = (apples)*(theAmount[J+1])
            x = cash
            if x > y:
                y = x
                S = theAmount[J]
                A = theAmount[J+1]
            print(cash)
    print("the better profit major is :" , y,", by purchasing at ",S,"and selling at ",A,".")
main()       
