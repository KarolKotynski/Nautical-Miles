import csv

from distances import calculate_distances

"""
This script is to calculate distance from point to point for flight route in Nautical Miles.
Input file is CSV file with cities, IATA code (departire and arrival) and its lat and lon
Input file have to be in this same folder as python file.

Nautical miles are calculated from every row in CSV file from given lat and lon using geopy module

as a result is a new CSV file with additional column named "NM".
"""

basic_file = 'Flight Distance Test.csv'

# reading file as a dictionary
with open(basic_file, 'r') as my_file:
    csv_reader = csv.DictReader(my_file)
    
    calculated_routes = 'Flight_Distance_Test_NM.csv'

    with open(calculated_routes, 'w', newline='') as new_file:
        fieldnames = [
            'Normalised City Pair',
            'Departure Code',
            'Arrival Code',
            'Departure_lat',
            'Departure_lon',
            'Arrival_lat', 
            'Arrival_lon',
            'NM'
            ]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for row in csv_reader:
            row = calculate_distances(row)
            csv_writer.writerow(row)
