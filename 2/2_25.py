k = int(input("COUNT : "))
c = k % 10
if c == 1:
    print("ГРИБ: ", k)

elif c == 2 or c == 3 or c == 4:
    print("ГРИБА: ", k)
else:
    print("ГРИБОВ", k)
