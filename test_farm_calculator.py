from farm_calculator import calculate_square_footage

def test_calculate_square_footage():
    farm_data = [
    {'width': 10, 'length': 20, 'latitude': 34.123, 'longitude': -118.456},
    {'width': 15, 'length': 25, 'latitude': 34.567, 'longitude': -118.789},    
    ]

    updated_farm_data = calculate_square_footage(farm_data);

    assert updated_farm_data[0].get('square_footage') == 200

    assert updated_farm_data[1].get('square_footage') == 375
