print('Welocome To Tip Calculationn')

bill = input("What was the Total Bill ?")
print(type(bill))

Amount_bill = float(bill)
print(type(Amount_bill))  

tip = int(input("How Much Tip You Give Precent Of Bill 10,12,or 15 ?"))
people = int(input("No. of People"))

tip_precent = tip/100
Amount_per_person = (Amount_bill + Amount_bill * tip_precent)/people

final_amount = round(Amount_per_person , 2)


print(final_amount) 
