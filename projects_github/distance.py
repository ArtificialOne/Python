def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        'miles': {
            'meters' : 1609.3435021075908935,
            'centimeter' : 160934.35021075909026,
            'kilometers': 1.609344,
            'yard' : 1759.9994554982401951,
            'foot' : 5279.9983664947203579,
            'inch' : 63359.980397936655208,
            'nautical_mile' : 1 / 1.151,
            'meters': 1609.344,
            'feet': 5280
        },
        'kilometers': {
            'miles': 1 / 1.609344,
            'centimeter' : 100000,
            'meters': 1000,
            'feet': 3280.84
        },
        'meters': {
            'miles': 1 / 1609.344,
            'kilometers': 1 / 1000,
            'feet': 3.28084
        },
        'feet': {
            'miles': 1 / 5280,
            'kilometers': 1 / 3280.84,
            'meters': 1 / 3.28084
        }
        # Add more conversion factors as needed
    }

    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        conversion_factor = conversion_factors[from_unit][to_unit]
        return distance * conversion_factor
    else:
        return "Conversion not supported or units not recognized"
    
print(convert_distance(1, 'miles', 'nautical_mile'))