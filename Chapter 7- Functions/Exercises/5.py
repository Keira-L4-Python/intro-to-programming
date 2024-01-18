def describe_city(city, country='Mexico'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Seattle')
describe_city('Paris', 'France')
describe_city('Venice')
