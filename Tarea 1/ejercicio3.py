
while True:
    try:
        var = int(input("numero:"))
        #o
        #var = 600851475143
        maximo = 2;
        while var > maximo:
            if var % maximo == 0:
                var = var/maximo
                maximo = 2
            else:
                maximo+=1;
        print("maximo: %d" % (maximo))
        break 
    except ValueError: 
        print ("ingrese un numero")





