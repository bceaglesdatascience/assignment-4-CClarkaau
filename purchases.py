#decsription: purchases.py
#author: Clark.Colin
#date: 9.18.23

#b. add tax function
def add_tax (lst,sls_tx):
    updated_list = lst.copy()
    i = 0
    while i < len(updated_list):
        updated_list[i] += (sls_tx * updated_list[i])
        i += 1
    return updated_list
'''
MAIN
'''
#a. Get input and create lists
number_of_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))
#Initialize lists
customer_names = []
item_costs = []
#initialize the dictionary
reciept_dict = {}
while(number_of_purchases) > 0:
    customer_names.append(input("Customer: "))
    item_costs.append(float(input("Cost: ")))
    number_of_purchases -= 1
#c. use add_tax to apply sales tax to the costs in cost list
updated_list = add_tax(item_costs, sales_tax)
#d. define an empty dictionary with customer : cost
for i in range(len(customer_names)):
    name = customer_names[i]
    price = updated_list[i]
    if name in reciept_dict:
        reciept_dict[name] += price
    else:
        reciept_dict[name] = price
#Outputs
print(reciept_dict)

