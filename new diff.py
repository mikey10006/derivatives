##this program calculates the derivative of inputs via the power rule, i need this for maths lol, the y input is for a later graphing tool im making##
while True:
    coef=[]
    powa=[]
    n= int(input("please enter the number of terms: "))
    y=float(input("please enter the x^0 term: "))
    for count in range(n-1):
        print("please enter coefficient",count+1)
        coefficient=float(input("enter here: "))
        print("please enter power",count+1)
        power=float(input("enter here: "))
        newCoef=coefficient*power
        newPower=power-1
        coef.append(newCoef)
        powa.append(newPower)
        print("your derivative of",count+1,"term is", coef[count],"x^",powa[count])
    
    
