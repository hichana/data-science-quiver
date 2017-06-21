# import beautiful soup
from bs4 import BeautifulSoup

# returns a list of all the option element, which are
# a list of all the airline carriers
def options(soup, id):
    # list to hold all of the carriers
    options_values = []
    # .find() method finds an element with specified id
    carrier_list = soup.find(id=id)
    # loops through all the 'option' elements in the list object
    for option in carrier_list.find_all('option'):
        # appeneds the options_values (carriers) with the value
        # from each 'option' tag
        option_values.append(option['value'])
    return option_values

def print_list(label, codes):
    print("\n%s:" % label)
    for c in codes:
        print(c)

def main():
    soup = BeautifulSoup(open("virgin_and_logan_airport.html"), "lxml")

    codes = options(soup, 'CarrierList')
    print_list("Carriers", codes)

    codes = options(soup, 'AirportList')
    print_list("Airports", codes)

main()
