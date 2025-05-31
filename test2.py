import pandas as pd

# Example: Static dataset of hotels
data = [
    {"name": "Hotel California", "location": "Los Angeles"},
    {"name": "The Beverly Hills Hotel", "location": "Beverly Hills"},
    {"name": "Fairmont San Francisco", "location": "San Francisco"},
    {"name": "The Ritz-Carlton", "location": "Half Moon Bay"},
    {"name": "Palomar Hotel", "location": "San Diego"},
    {"name": "Hilton Anaheim", "location": "Anaheim"},
    {"name": "Hyatt Regency", "location": "San Francisco"},
    {"name": "InterContinental Los Angeles", "location": "Los Angeles"},
    {"name": "Loews Santa Monica Beach Hotel", "location": "Santa Monica"},
    {"name": "W Hollywood", "location": "Hollywood"}
]

def get_hotels_in_california():
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    hotels = get_hotels_in_california()
    print("Top Hotels in California:")
    print(hotels)