# PUBG data map

A python program for processing PUBG match telemetry data and visualising on game map image. 

Currently supports location events [all, specific], kill events [all, victim, killer], item pickup events, safety zone and flight path.

# How to use 

1. Create a TeleProcessor instance passing telemetry data filepath as argument. 
2. Use TeleProcessor methods to extract the desired data. 
3. Create a MapEditor instance passing in map filepath and map size as arguments. 
4. Use MapEditor methods to draw desired elements on map image and then save edited image as new file. 
