

import csv




def new_orders():
    
    clerk=input("Your Name: ")
    name=(input("Customer's name: "))
    address=input("Customer's address: ")
    desc=input("Description: ")
    cost=(input("Customer's cost: "))
    date=(input("Date (DD/MM/YY): "))
    file=open("orders.csv", newline='')
    reader=csv.DictReader(file)
    orders_list=list(reader)
    id=len(orders_list)+1
    file.close()
    file = open("orders.csv",'a', newline='\n')
    file.write(str(id)+','+name+','+address+','+desc+','+date+','+cost+','+'0'','+clerk+'\n')
    print("The addition of a new order has been successfully finalized.")
    file.close()    
    







def undelivered_orders():
    print("---UNDELIVERED ORDERS---")
    file=open("orders.csv")
    reader=csv.DictReader(file)
    counter=0
    for row in reader:
        if row['delivered'] == '0':
            counter +=1
    file.close()
    
    print(f"At present, there exist {counter} undelivered orders.")
    answer=str.lower(input("Would you prefer to review them? Please indicate your choice by selecting Y for yes or N for no.  "))

    undelivered_orders=[]
    if answer == 'y':
        with open("orders.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['delivered'] == '0':
                    undelivered_orders.append(row)
    elif answer == 'n':
        print("Concluding program execution...")
    file.close()
    
    
    for order in undelivered_orders:
        print("Order ID:", order['id'])
        print("Customer:", order['name'])
        print("Address:", order['address'])
        print("Items:", order['descr'])
        print("Cost:", order['cost'])
        print(f"Delivered: {'No' if order['delivered'] == '0' else None}")
        print("---------------------------")

    




 


    
            







