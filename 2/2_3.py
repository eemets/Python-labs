n = int(input("n = "))

if ((n//100) == 2) or (((n%100)//10) == 2) or(((n%100)%10) == 2) :
    print("a) n есть цифра 2")

if (((n//100)%2) == 0) and ((((n%100)//10)%2) == 0) and ((((n%100)%10)%2) == 0) :
    print("b) n парное ")

if ((n//100))+ ((n%100)//10) + ((n%100)%10) == 18 :
    print("c) сумма цифр 18 ")
