_author_ = "amber buckley"

# write a program which gathers ticket sales for a concert fundraiser to raise money for the
#  North Fork of the Smith River put on by March Forth Marching Band, a local Portland Band
# at a venue which holds 625 people with general admission price and outputs the money raised

# moduleMain()
#   declare river money
#   riverMoney = call getMoneyRaised
#   display "You raised a lot of money for the Smith River!"
#   if money raised > 5000 then
#       display "great work"
#   else:
#       display "we will need another fundraiser"
# end module
#
# venue occupancy = 625
#
# function boolean is_valid_integer(string input_string)
#   isValid = is input_string a valid integer?
#   return is valid
# end function

# function integer getTicketsSold()
#   display "How many tickets did you sell?"
#   input string input_string
#   set isValid = isValid_integer(input_string)
#       while Not isValid:
#          display prompt
#          input input_string
#          If input_string is valid Real number then
#               return toReal(input_string)
#           End if
#           Display "Please enter a valid number"
#       end while
# end function
#
# function get money raised(integer n)
#   declare general admission = 25.00
#   call get tickets sold
#   set money raised = general admission * total tickets sold
# end function


def isValidReal(input_string):

    try:
        val = float(input_string)
        isValid = True

    except ValueError:
        isValid = False
    return isValid

def getTicketsSold():
    input_string = input("How many tickets were sold for the fundraiser?")
    isValid = isValidReal(input_string)
    while not isValid:
        input_string = input("Please enter a whole number")
        isValid = isValidReal(input_string)
    input_integer = int(input_string)
    return input_integer

# get money raised
def getMoneyRaised(n):
    generalSales = 25.00
    sales = 0
    sales = getTicketsSold()
    moneyRaised = sales * generalSales
    return moneyRaised

def calculateMoneyRaised():
    riverMoney = 0
    n = 0
    riverMoney = getMoneyRaised(n)
    print("You raised", riverMoney, " dollas for the Smith River!" + " And it was such a great show!")
    if riverMoney >= 5000:
        print("We are on the right path! Nice Job Team!")

calculateMoneyRaised()















