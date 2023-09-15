from config import (geofence_min_lat, geofence_max_lat, 
                    geofence_min_lon, geofence_max_lon)

def validate_coordinates(latitude, longitude):
    if (-90 <= latitude <= 90) and (-180 <= longitude <= 180):
        return True
    else:
        return False

def generate_gps_data():
    while True:
        try:
            latitude = float(input("Enter Latitude: "))
            longitude = float(input("Enter Longitude: "))

            if validate_coordinates(latitude, longitude):
                if (
                    geofence_min_lat <= latitude <= geofence_max_lat
                    and geofence_min_lon <= longitude <= geofence_max_lon
                ):
                    return latitude, longitude
                else:
                    print("Coordinates are outside the geofence.")
            else:
                print("Invalid coordinates. Latitude must be between -90 and 90, and longitude between -180 and 180.")
        except ValueError:
            print("Invalid input. Please enter valid numeric coordinates.")

if __name__ == "__main__":
    latitude, longitude = generate_gps_data()
    print(f"Sending GPS data: Latitude={latitude}, Longitude={longitude}")
