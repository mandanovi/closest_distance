from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def location_(address):
    geolocator = Nominatim(user_agent="Closest_Distance")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


def get_distance(address1, address2):
    first_loc = location_(address1)
    second_loc = location_(address2)
    return float(geodesic(first_loc, second_loc).miles)


user_address = input("reference address: ")
count_address = 0
try :
    count_address = int(input('how many locations you want to compare with the reference address? '))
except Exception as e:
    print(e)

my_dict = {}
my_list = []

for i in range(0, count_address):
    compare_address = input(f"{i+1}. address to compare: ")
    try :
        my_dict[compare_address] = get_distance(user_address, compare_address)
        my_list.append(get_distance(user_address, compare_address))
    except Exception as e:
        print(e)

closest_place = min(my_dict, key=my_dict.get)
closest_distance = min(my_list)
farthest_distance = max(my_list)
farthest_place = max(my_dict, key=my_dict.get)
print(f"The closest location from reference address: {closest_place} with distance: {closest_distance} miles.")
print(f"The farthest location from reference address: {farthest_place} with distance: {farthest_distance} miles.")


# 'Refshalevej 173A, 1432 København'
# 'Prins Jørgens Gård 1, 1218 København'
# '175 5th Avenue NYC'
# 'Peder Hvitfeldts stræde 4 1173'
