import requests
from django.shortcuts import render


def calculate_distance(request):
    if request.method == 'POST':
        origin_name = request.POST.get('origin')
        destination_name = request.POST.get('destination')

        # Geocode the locations
        origin = geocode_location(origin_name)
        destination = geocode_location(destination_name)

        if origin and destination:
            # Call Bing Maps API for distance
            distance = get_distance_from_bing_maps(origin, destination)
            return render(request, 'result.html', {'distance': distance})
        else:
            return render(request, 'result.html', {'error': 'Geocoding failed'})

    else:
        return render(request, 'envdata/distances/form-distance.html')


def geocode_location(location_name):
    BING_MAPS_API_KEY = 'your_api_key'  # Replace with your Bing Maps API key
    url = f"http://dev.virtualearth.net/REST/v1/Locations?query={location_name}&key={BING_MAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Parse the response to extract latitude and longitude
    coordinates = data['resourceSets'][0]['resources'][0]['point']['coordinates']
    return coordinates if coordinates else None


def get_distance_from_bing_maps(origin, destination):
    BING_MAPS_API_KEY = 'your_api_key'
    url = f"https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key={BING_MAPS_API_KEY}"
    payload = {
        'origins': [{'latitude': origin[0], 'longitude': origin[1]}],
        'destinations': [{'latitude': destination[0], 'longitude': destination[1]}],
        'travelMode': 'driving'
    }
    response = requests.post(url, json=payload)
    data = response.json()
    distance = data['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']
    return distance
