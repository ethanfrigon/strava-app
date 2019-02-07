import json
import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template():
  return render_template('template.html', lap_tup=lap_tup)

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

ACCESS_TOKEN = "5795d5436fd887179045070f33b460ffdcc1e8f0"

PARAMS = {'access_token': ACCESS_TOKEN }

lap_tup=()
for activity_id in sliced_tup:
  r = requests.get(url = URL_BASE + str(activity_id) + URL_LAPS, params=PARAMS)
  data = r.json()
  lap_tup+=(data, )

# print(lap_tup)

# for ride in lap_tup:
#   # if lap['average_heartrate'] > 150:
#   # print(ride)
#   for lap in ride:
#     if lap.get('average_heartrate'):
#       print(lap['id'], lap['average_heartrate'])
#       # lap.get('average_heartrate')
#     else:
#       print(lap['id'])
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

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)    