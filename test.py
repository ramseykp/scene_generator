
num_of_group_layers = 62
num_points = 1008 #---number of frames you want in the animation (script will evenly places these throughout the 360)
r = 36590
for i in range(num_points):
    
    frame_hold = 2 #---how many frames you want the layer to be present before transitioning to the next frame
    frame_freeze = i//frame_hold

    layer_index = frame_freeze
    if layer_index > 62: #---62 is the number of layers being cycled through in the animation
       layer_index = (i % num_of_group_layers)//frame_hold
    print(layer_index)

    