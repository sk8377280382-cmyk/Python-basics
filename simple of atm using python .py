# Wap bank ATM(Automated )
menu = input("""
Hi , how can help you!! 
1) Enter 1  check balance.
2) Enter 2  change pin.
3) Enter 3 to withdrawl amount.
4) Enter 4 to deposit amount in your account balance.
5) Enter 5 to exit .
""")

# Given condition 
if menu == '1':
    print('To check balance ')
elif menu == '2':
    print('Change pin')
elif menu == '3':
    print('Withdrawl amount ')
elif menu == '4':
    print('Deposit amount to your balance ')
else:
    print('Exit to the card ')
