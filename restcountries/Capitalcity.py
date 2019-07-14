import requests

BASE_URI='https://restcountries.eu/rest/v2'

def capitalcity_countryname(resource, name):
    countryname=name.lower()
    response = requests.get(BASE_URI+resource+countryname)
    if response.status_code == 400:
        return "Invalid country name, please re-enter\n"
    elif response.status_code == 404:
        return "Country name does not exist, please re-enter\n"
    elif response.status_code == 500:
        return "Server error, please retry later\n"
    elif response.status_code == 200:  
        countryinfo=response.json() 
        countries=[]
        for country in countryinfo:
            if countryname in country['name'].lower():
                capital=country['capital']
                cname= country['name']
                countries.append("Capital City of {} is {}\n".format(cname, capital))
        countries = "\n".join(countries)
        return countries

def capitalcity_countrycode(resource, code):
    code=code.upper()
    response = requests.get(BASE_URI+resource+code)
    if response.status_code == 400:
        return "Invalid country code, please re-enter\n"
    elif response.status_code == 404:
        return "Country code not found, please re-enter\n"
    elif response.status_code == 500:
        return "Server error, please retry later\n"
    elif response.status_code == 200:
        countryinfo=response.json()
        if countryinfo['alpha2Code'] == code or countryinfo['alpha3Code'] == code:
            capital=countryinfo['capital']
            countryname=countryinfo['name']
            return "Capital city of {} ({}) is {}\n".format(code, countryname, capital)

while True:
    print("select an option from the following: ")
    print("1. Find capital city by country name")
    print("2. Find capital city by country code")
    print("3. Exit the program")
    print("Enter your choice (1/2/3): ")
    choice=input() 
    if choice not in ("1", "2", "3"):
        print("Invalid choice\n")
        continue
    elif choice == "1":
        print("Enter the Country name: ")
        country=input()
        resource="/name/"
        capitalname=capitalcity_countryname(resource, country)
    elif choice == "2":
        while True:
            print("Enter 2 or 3 char country code: ")
            ccode=input()
            if len(ccode) == 2 or len(ccode) == 3:
                break
            else:
                print("Country code should be 2 or 3 characters")
                continue   
        resource="/alpha/"
        capitalname=capitalcity_countrycode(resource, ccode)
    elif choice == "3":
        print("Good Bye")
        break
    print(capitalname)
