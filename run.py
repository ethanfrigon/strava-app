import json
import requests

# with open('sample_laps.json', 'r') as f:
#   laps_dict =  json.load(f)

with open('all_activities.json', 'r', -2, encoding="utf8") as a:
  activities_dict = json.load(a)

# for lap in laps_dict:
#   if lap['average_heartrate'] > 150:
#     print(lap['id'], lap['average_heartrate'])

activity_tup=()
for activity in activities_dict:
  activity_tup += (activity['id'], )

# print(activity_tup)

sliced_tup = activity_tup[0:5]
# print(sliced_tup)

# for activity_id in sliced_tup:
#   print(activity_id)

URL_BASE = "https://www.strava.com/api/v3/activities/"
URL_LAPS ="/laps"

ACCESS_TOKEN = "d9510ad1154fe0355141d32863bbb8e473bfe53f"

PARAMS = {'access_token': ACCESS_TOKEN }

lap_tup=()
for activity_id in sliced_tup:
  r = requests.get(url = URL_BASE + str(activity_id) + URL_LAPS, params=PARAMS)
  data = r.json()
  lap_tup+=(data, )

# print(lap_tup)

for lap in lap_tup[0]:
  # if lap['average_heartrate'] > 150:
  print(lap)
  # print(lap['id'], lap['average_heartrate'])


# for activity in activities_dict:
#   print(activity)

# print(id_and_hr)


# py_lap_array = json.dumps(lap_array)

# print(py_lap_array)

# acts = activities_dict[0].id()

# print(acts)

# act_ids = [(id) for id ]



# first_lap = data[0]

# print(first_lap['average_heartrate'])