#!/usr/bin/env python

# Find Cost of Tile to Cover W x H Floor
def tile_calc(width,height,cost):
    # Cost is for 1x1 tile
    return width * height * cost

if __name__ == '__main__':
    tile_width = float(input('Enter the tile width:'))
    tile_height = float(input('Enter the tile height:'))
    tile_cost = float(input('Enter the cost of 1x1 tile:'))
    
    res = tile_calc(tile_width,tile_height,tile_cost)

    print('Cost of the {} x {} tile is {}$'.format(tile_width,tile_height,res))