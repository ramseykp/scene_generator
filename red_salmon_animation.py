#project for using this script is saved within Osprey2. Global Scene
import math
from numpy import arctan2
import os

#import arcpy
#---4 lines below initiate the current project. Gotta have a 3d scene open named Map_3D7 and a layout open named Layout
aprx = arcpy.mp.ArcGISProject('CURRENT')
red_salmon_scene = aprx.listMaps('Map_3D7')[0]
lyt = aprx.listLayouts('Layout')[0]
scene_frame = lyt.listElements('MAPFRAME_ELEMENT', 'Map Frame')[0]

#---set camera atlitude and pitch to remain constant for animation
scene_frame.camera.Z = 25000 #in meters
scene_frame.camera.pitch = -34.5 # -90 looking straight down and 90 looking up at sky



center_lat = 41.13  #---center point of RedSalmon
center_lon = 123.41 #---center point of RedSalmon
RE = 6378100        #---earth radius in m
dn_dlat = RE*math.pi/180
print('dn_dlat' + str(dn_dlat))
de_dlon = dn_dlat*math.cos(center_lat*math.pi/180)
print('dn_dlon' + str(de_dlon))

def get_bearing(lat1, lat2, long1, long2):
    #print('long1 is = '+ str(type(long1)))
    dL = long2-long1
    X = math.cos(lat2)* math.sin(dL)
    Y = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)* math.cos(dL)
    bearing = arctan2(X,Y)
    brng = ((math.degrees(bearing)+360) % 360)
    return brng

list_of_group_layers = []
for lyr in red_salmon_scene.listLayers():
    if lyr.isGroupLayer:
        print(lyr.name + ' added to list of group layers')
        list_of_group_layers.append(lyr.name)
    else:
        print(lyr.name + ' not added')
num_of_group_layers = len(list_of_group_layers)
# --------------------------------------------------------------------------------



#print(list_of_group_layers)
print('number of group layers is = ' + str(len(list_of_group_layers)))
layer_index = 0
for item in list_of_group_layers:
    print('index value = ' + str(layer_index) + ' ' + item)
    layer_index += 1


basemap_layer = red_salmon_scene.listLayers('World Hillshade (Dark)')[0]
#current_layer = red_salmon_scene.listLayers(list_of_group_layers[layer_index])
#red_salmon_scene.moveLayer(current_layer, basemap_layer, 'BEFORE')


#-----------------------------------------------------------------------------------
#circle radius = 36590km
num_points = 1008 #---number of frames you want in the animation (script will evenly places these throughout the 360)
r = 36590
for i in range(num_points):
    
    frame_hold = 2 #---how many frames you want the layer to be present before transitioning to the next frame
    frame_freeze = i//frame_hold

    layer_index = frame_freeze
    if layer_index > 62: #---62 is the number of layers being cycled through in the animation
       layer_index = (i % num_of_group_layers)
    print(str(list_of_group_layers[layer_index]))
    current_layer = red_salmon_scene.listLayers(str(list_of_group_layers[layer_index]))[0]
    current_layer.visible = True
    red_salmon_scene.moveLayer(red_salmon_scene.listLayers()[0], current_layer, 'BEFORE')
    red_salmon_scene.moveLayer(current_layer, basemap_layer, 'AFTER')
    
    camera_lon = (center_lon+r*(1/de_dlon)*math.sin(2*math.pi*i/num_points))
    scene_frame.camera.X = -1 * camera_lon
    print('camera_lon = ' + str(camera_lon))
    camera_lat = center_lat+r*(1/dn_dlat)*math.cos(2*math.pi*i/num_points)
    scene_frame.camera.Y = camera_lat
    print('camera_lat = ' + str(camera_lat))
    camera_heading = get_bearing(camera_lat, center_lat, camera_lon, center_lon)
    scene_frame.camera.heading = camera_heading
    print('camera_heading = ' + (str(camera_heading)))
    filename = str(i) + '.jpg'
    lyt.exportToJPEG(os.path.join('''C:\\Users\\OWI-Osprey2\\Videos\\Animation''', filename))

    current_layer.visible = False






#example of how to change map layers around 
#Perimeter_Layer = Big_Map.listLayers(Heat_Perimeter)[0] # needs more testing
#Intense_Layer = Big_Map.listLayers(Intense_Heat)[0]  # needs more testing
#Scattered_Layer = Big_Map.listLayers(Scattered_Heat)[0] # needs more testing
#Isolated_Layer = Big_Map.listLayers(Isolated_Heat_Sources)[0] # needs more testing
##---Ensure Layer order is correct (reorder each of heat layers)
#Big_Map.moveLayer(Big_Map.listLayers()[0], Perimeter_Layer, 'BEFORE') # needs more testing
#Big_Map.moveLayer(Big_Map.listLayers()[1], Intense_Layer, 'BEFORE') # needs more testing
#Big_Map.moveLayer(Big_Map.listLayers()[2], Scattered_Layer, 'BEFORE') # needs more testing
#Big_Map.moveLayer(Big_Map.listLayers()[3], Isolated_Layer, 'BEFORE') # needs more testing