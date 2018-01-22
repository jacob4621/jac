def main():
    for J in range(1,101):
        jazz = ""
        if(J%3==0):
            jazz+= "fizz"
        if(J%5==0):
            jazz+= "buzz"
        if(jazz==""):
            jazz = J
        print(jazz)
main()
