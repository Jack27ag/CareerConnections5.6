def calculate_square_footage(farms):
    for farm in farms:
        width = farm.get('width', 0)
        length = farm.get('length', 0)
        square_footage = width * length
        farm['square_footage'] = square_footage
    return farms


# Example usage:
farm_data = [
    {'width': 10, 'length': 20, 'latitude': 34.123, 'longitude': -118.456},
    {'width': 15, 'length': 25, 'latitude': 34.567, 'longitude': -118.789},
    # Add more farms as needed
]

farms_with_square_footage = calculate_square_footage(farm_data)

# Print the result
for farm in farms_with_square_footage:
    print(farm)