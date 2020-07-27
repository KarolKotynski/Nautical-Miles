import csv
from geopy.distance import geodesic
def calculate_distances(row):
    try:
        coords_1 = (row['Departure_lat'], row['Departure_lon'])
        coords_2 = (row['Arrival_lat'], row['Arrival_lon'])
        dist = round(geodesic(coords_1, coords_2).nm, 2)
        row['NM'] = dist
    except:
        pass
    
    return row
