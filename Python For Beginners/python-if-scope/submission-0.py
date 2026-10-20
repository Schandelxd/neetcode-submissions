def pay_bill(balance: int, bill: int) -> int:
    if balance >= bill:
        new_balance = balance - bill
        print(new_balance)
    else:
        print(balance)



# do not modify below this line
pay_bill(100, 50)
pay_bill(100, 100)
pay_bill(100, 150)
