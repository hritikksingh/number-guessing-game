n=7
num=int(input(" enter any number between 0 to 100  \n"))
i=1
if num!=n:
    for j in range(100000):
        if num>n:
            print("\ntoo large \n")
        elif num<n:
            print("\n too small \n")
        elif num==n:
            break
        i+=1
        num=int(input("enter number again \n"))
print(f"\n you got it right in {i} tries")




    

