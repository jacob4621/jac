def main():
    for J in range(2,50):
        prime = True
        for S in range(2,J):
            if J % S == 0:
                prime = False
                break
            if prime:
                print(J)
main()
