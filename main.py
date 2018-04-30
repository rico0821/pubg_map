# -*- coding: utf-8 -*-

import json, os, time
import pymongo
from pymongo import MongoClient

from telemetry import TeleProcessor
from map_editor import MapEditor


color = {
    'red' : {
        'outline' : (255, 0, 0 , 255),
        'fill' : (255, 0, 0, 100)
    },
    'blue' : {
        'outline' : (1, 1, 198, 255),
        'fill' : (1, 1, 198, 100)
    },
    'white' : {
        'outline' : (255, 255, 255, 255),
        'fill' : (255, 255, 255, 100)
    },
    'orange' : {
        'outline' : (255, 165, 0, 255),
        'fill' : (255, 165, 0, 100)
    }
}


if __name__ == '__main__':
   
    print("----------------------------------")
    print('STARTING TASK...')
    print("----------------------------------")
    start_data = time.time()
    print("----------------------------------")
    print('PROCESSING DATA...')
    print("----------------------------------")

    tele = TeleProcessor('telemetry/0b11d030-ed76-4f5b-bf42-d92c00bebb21.json)
                         
    xy_loc = tele.getPlayerXY()
    xy_kills = tele.getKillsXY()
    xy_magnetic = tele.getMagneticXY()
    fit_flight = tele.getFlightFit()
                         
    delta_data = time.time() - start_data
    print('Data processing took: %f seconds.' % delta_data)
    start_img = time.time()

    print("----------------------------------")
    print('PROCESSING IMAGE...')
    print("----------------------------------")

    editor = MapEditor('map_img/Erangel.jpg', 816001)
    editor.draw_flags(xy_kills, color['red'], 25)
    editor.draw_flags(xy_locs, color['blue'], 25)
    editor.draw_magnetic(xy_magnetic)
    editor.draw_flight(fit_flight, color['white'], 10)
                         
    editor.save_map('results/erangel_test.jpg')

    delta_img = time.time() - start_img
    print('Image processing took: %f seconds.' % delta_img)
    print("----------------------------------")
    print('TASK DONE... TOOK %f seconds total.' % (delta_data + delta_img))
    print("----------------------------------")
