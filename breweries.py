import requests

# Define the list of states
states = ["Maine", "Alaska", "New York"]  # Add more states as needed


#Dict to store  breweries count for each state
brewery_counts = {}

brewery_typeCount={}

# Dictionary to store the counts and list of breweries with websites for each state
breweries_with_websites = {}

# Iterate through each state
for state in states:
    # Define the API endpoint URL for the current state
    url = f"https://api.openbrewerydb.org/v1/breweries?by_state={state}"
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Get the count of breweries for the current state
        brewery_count = len(data)
        
        # Store the count in the dictionary
        brewery_counts[state] = brewery_count
        #Store breweries by group of city
        breweries_byCity={}
        #Store count of website in each breweries
        breweries_with_website_count=0
        breweries_with_website_list=[]
        # Count the number of breweries with websites
        for brewery in data:
            print("Name:", brewery['name'])
            print("City:", brewery['city'])
            print("State:", brewery['state'])
            print("Type:", brewery['brewery_type'])
            print("Website:",brewery['website_url'])
            print("-------")
            city=brewery['city']
            brewery_type = brewery['brewery_type']
            if city in breweries_byCity:
                breweries_byCity[city].add(brewery_type)
                
            else:
                breweries_byCity[city]={brewery_type}

        for city,types in breweries_byCity.items():
            cities_state=f"{city},{state}"
            brewery_typeCount[cities_state]=len(types)    
        # Store the count and list of breweries with websites in the dictionary
        for brewery in data:
            if brewery['website_url']:
                breweries_with_website_count+=1
                breweries_with_website_list.append(brewery['name'])
        breweries_with_websites[state] = {
            'count': breweries_with_website_count,
            'list': breweries_with_website_list
        }
    else:
        print(f"Failed to retrieve data for {state}. Status code:", response.status_code)
#Print the counts of breweries for each state
# for state, count in brewery_counts.items():
#     print(f"{state}: {count} breweries")
# print("-----------------------------------------------------------")
#     #Print the counts of types of breweries of each cities with state
# for cities_state,count in brewery_typeCount.items():
#     print(f"{cities_state}:{count} types of breweries")
# #Print the counts and list of breweries with websites for each state
for state, data in breweries_with_websites.items():
    print(f"{state}:")
    print(f"Count of breweries with websites: {data['count']}")  
    print("List of breweries with websites:")
    for brewery_name in data['list']:
        print("-", brewery_name)
    print()
