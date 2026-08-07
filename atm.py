pin = int(input ("enter PIN"))
if pin==1234:
    balance = int (input ("enter your balance"))
    withdraw = int (input ("how much would you like to withdraw"))
    if withdraw<=0:
        print ("invalid amount")
    elif withdraw>balance:
        print ("insufficient balance")
    else:
        balance = balance-withdraw
        print ("withdrawal successful")
        print (f"remaining balance: {balance}")
else:
    print("wrong pin")