 #write a program to withdraw ksh25000 if account balance is btn ksh ksh 100000 to 200000
 #30%if acc bal btn 500000 and 1M
 #above ! deduct 15000
 
 acc_bal = input("What is your account balance?")
 if (int(acc_bal)) > 100000 and int(acc_bal) < 200000):
     acc_bal = acc_bal - ksh25000
     print("we have deducted ksh 25000 from your account")
     print(acc_bal)

elif(iny(acc_bal) > 500000 and int(acc_bal) < 1000000):
    acc_bal = float(acc_bal) -(0.3*float(acc_bal))
    print("we have deducted 30% from your account")
    print(acc_bal)
    
elif(int(acc_bal) > 1000000):
    acc_bal = acc_bal - 15000
    print("we have deducted 15000 from ur account")
    print(acc_bal)
 
 