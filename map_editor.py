# -*- coding: utf-8 -*-
"""
    pubg telemap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    pubg map editor 구현. 
    :copyright: (c) 2018 by rico0821.
    :license: 

"""

from PIL import Image, ImageDraw


class MapEditor:
    
    def __init__(self, mapFile, mapSize):
        
        try:
            self.img = Image.open(mapFile)
            self.rescale = self.img.size[0] / mapSize
        
        except Exception as e:
            raise(e)
            
    def draw_flight(self, fit, color, width):
        
        m = fit[0]
        c = fit[1] * self.rescale
        size = self.img.size[0]
        
        x1 = 0
        y1 = m*x1 + c
        if y1 < 0:
            y1 = 0
            x1 = -c / m
        if y1 > size:
            y2 = size
            x1 = (size-c) /m 
            
        x2 = size
        y2 = m*x2 + c
        if y2 < 0:
            y2 = 0
            x2 = -c / m 
        if y2 > size:
            y2 = size
            x2 = (size-c) / m
        
        try:
            draw = ImageDraw.Draw(self.img, 'RGBA')
            draw.line([(x1, y1), (x2, y2)], fill=color['outline'], width=width)
        
        except Exception as e:
            print(str(e))
    
    def draw_magnetic(self, xy_magnetic):
        
        for data in xy_magnetic:
            
            x = data['x'] * self.rescale
            y = data['y'] * self.rescale
            r = data['r'] * self.rescale
            
            try:
                draw = ImageDraw.Draw(self.img, 'RGBA')
                draw.ellipse((x-r,y-r,x+r,y+r), outline=(255,255,255,255),fill=((255,255,255,0)))
                
            except Exception as e:
                print(str(e))
        
    def draw_flags(self, xy_type, color, flagSize):
        
        for data in xy_type:
            
            x = data['x'] * self.rescale
            y = data['y'] * self.rescale

            try:
                draw = ImageDraw.Draw(self.img, 'RGBA')
                offset = (flagSize-1)/2
                draw.ellipse((x-offset, y-offset, x+offset, y+offset), outline=color['outline'], fill=color['fill'])

            except Exception as e:
                print(str(e))
    
    def draw_path(self, xy_path, color, width):
        
        coords = [(data['x']*self.rescale, data['y']*self.rescale) for data in xy_path]
        
        try:
            draw = ImageDraw.Draw(self.img, 'RGBA')
            draw.line(coords, fill=color['outline'], width=width)
            
        except Exception as e:
            print(str(e))
    
    def save_map(self, fileName):
        
        self.img.save(fileName)