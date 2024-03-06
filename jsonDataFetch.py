import requests

class countrydata:
#constructor for taking input
    def __init__(self):
        self.url="https://restcountries.com/v3.1/all"
        self.data=self.fetch_data()


# create method to fetch data from the url
    def fetch_data(self):
        response=requests.get(self.url)
        if response.status_code==200:
            return response.json()
        else:
            print("Error: Not found")
            return None
       
    def disp_country_info(self):
        if self.data:
            for country in self.data:
                name = country['name']['common']
                currencies = country.get('currencies', {})  # Use get method to handle missing 'currencies' key
                print("Name of the country : ",name)
                print("-----currencies info------")
                for currency, details in currencies.items():
                    symbol = details.get('symbol')  # Use get method to handle missing 'symbol' key
                    print(f"{currency}:{symbol}")
                print()
            
    def disp_symbol_DOLLAR(self):
        if self.data:
            for country in self.data:
                name = country['name']['common']
                currencies = country.get('currencies', {})  # Use get method to handle missing 'currencies' key
                
                for currency, details in currencies.items():
                    symbol = details.get('symbol')  # Use get method to handle missing 'symbol' key
                    if symbol == '$':

                        print(f"{name}={currency}:{symbol}")
                #print()
    def disp_symbol_EURO(self):
        if self.data:
            for country in self.data:
                name = country['name']['common']
                currencies = country.get('currencies', {})  # Use get method to handle missing 'currencies' key
                
                for currency, details in currencies.items():
                    symbol = details.get('symbol')  # Use get method to handle missing 'symbol' key
                    if symbol == '€':
                        
                        print(f"{name}={currency}:{symbol}")
                #print()
country_data=countrydata()
print("------------------Fetching data from json -------------------")
print(country_data.fetch_data())
print("-------------Country Name, Currencies and its symbol----------")
country_data.disp_country_info()
print("-------------Countries which has DOLLAR symbol Currencies-------")
country_data.disp_symbol_DOLLAR()
print("-----------Countries which has EURO symbol Currencies------------")
country_data.disp_symbol_EURO()