total=0
while True:
    try:
        n1=input("Digite um numero: ")
        total=total+float(n1)
        if float(n1)==0:
            break
    except:
        print("Não e um numero valido")
print(total)
