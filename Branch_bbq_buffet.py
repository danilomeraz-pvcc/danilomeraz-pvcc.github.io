# Name: Danilo_Meraz and Arash_Tajalli
# Prog Purpose: This program finds the cost of adults and children eating at Branch Barbecue Buffet
#   Price for adults: $19.95
#   Price for children: $11.95
#   Sales tax rate: 6.2%
#   Service Fee: 10%

import datetime

############# define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .062
SERVICE_FEE_RATE = .1
PR_ADULTS = 19.95
PR_CHILDREN = 11.95

# define global variables
num_adults = 0
num_children = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

############# define program functions ############
def main():

    more_people = True

    while more_people:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nAnybody else (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_people = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adults
    num_adults = int(input("Number of adults: "))
    global num_children
    num_children = int(input("Number of children: ")) 

def perform_calculations():
    global subtotal, sales_tax, service_fee, total
    subtotal = (num_adults * PR_ADULTS) + (num_children * PR_CHILDREN)
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE_RATE
    total = subtotal + sales_tax + service_fee

def display_results():
    moneyformat = '8,.2f'
    print('------------------------------')
    print('**** Branch Barbecue Buffet ****')
    print('Your neighborhood restuarant')
    print('------------------------------')
    print('Adult Meal   $ ' + format((num_adults * PR_ADULTS), '8,.2f'))
    print('Child Meal   $ ' + format((num_children * PR_CHILDREN), '8,.2f'))
    print('Subtotal     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax, '8,.2f'))
    print('Service Fee  $ ' + format(service_fee, '8,.2f'))
    print('Total        $ '+ format(total, '8,.2f'))
    print('-------------------------------')
    print(str(datetime.datetime.now()))

##########   call on main program to execute ###########
main()
