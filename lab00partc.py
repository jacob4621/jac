def main():
    count = 0
    file = open("lab00partb.py",'r')
    for line in file.readlines():
        print(count,line)
        count = count + 1
main()
