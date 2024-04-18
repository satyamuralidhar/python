"""
Creating a  dictionary using user input
"""

response = {}
while True: 
    country = input("Enter country Name: ")
    capital = input("Enter capital Name: ")
    response[country] = capital
    recurse = input("If would yiou like to add more counties and capitals enter yes or else no: ")
    if recurse == "no" : 
        break
for country , capital in response.items():
    print(f'Country = {country},Capital={capital}')