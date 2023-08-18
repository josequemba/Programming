#Heart rate
#Author: josé Quemba
print ()
def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = float(input ('Enter the odometer starting value in miles: '))
    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input ('Enter the odometer ending value in miles: '))
    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input ('Enter the fuel amount in U.S. gallons: '))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon (start_miles, end_miles, amount_gallons)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print (f'The fuel efficiency of this vehicle is of {mpg:.1f} miles per gallon')
    print (f'Using liters per 100 kilometers, the fuel efficiency of this vehicle is of {lp100k:.2f} liters per 100 kilometers')

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    fuel_efficiency = (end_miles - start_miles) / amount_gallons
    return fuel_efficiency

def lp100k_from_mpg(mpg):
    fuel_efficiency = 235.215/mpg
    return fuel_efficiency
main()