import json

#variables
bright_min = 450
title = "US Fires - 9/1/2020 through 9/13/2020"

#file reading & writing
infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fire_9_1.json", "w")
fire_data = json.load(infile)
json.dump(fire_data, outfile, indent=4)



list_of_fires = fire_data

lats, lons, brights = [], [], []


for fire in list_of_fires:
    lat = fire["latitude"]
    lon = fire["longitude"]
    bright = fire["brightness"]

    lats.append(lat)
    lons.append(lon)
    if bright >= bright_min:
        brights.append(bright)



#html map plotting
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [20 for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title=title)

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_fires.html")
