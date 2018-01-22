jas = input("enter file you want to open and fix: ")
rjas = open(jas,"r")
wjas = open("New file.txt","w")
code = 0
for line in rjas:
    code = code + 1
    life = str(code) + " " + line
    wjas.write(str(life))
rjas.close()
wjas.close()
