card=input("enter the card number")
n=len(card)
sum=0
for i in range(n-2,-1,-2):
    product=int(card[i])*2
    if product<10:
        sum=sum+product
    else:
        product=str(product)
        sum=sum+ int(product[0]) + int(product[1])
for j in range(n-1,-1,-2):
    sum=sum+int(card[j]) 


sum=str(sum)
m=len(sum)

if (sum[m-1]=="0"):
    
    if((card[0:2] in ["34","37"]) and n==15):
        print("American express")
    elif((card[0]=="4") and (n==13 or n==16)):
        print("visa")  
    elif((card[0:2] in ["51","52","53","54","55"]) and n==16): 
        print("master card")   
    else:
        print("invalid card number")  


else:
    print("invalid card number")    

  

