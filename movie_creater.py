#movie_creater
import os
import moviepy.video.io.ImageSequenceClip
image_folder='C:\\Users\\KelseyRamsey\\Videos\\Animation\\'
fps=19
image_files = []

number_of_images = len(os.listdir(image_folder))
print('number of files ' + str(number_of_images))


for i in range(0, number_of_images):    
    image_filename = str(i) + '.jpg'
    print(image_filename)
    image_files.append(os.path.join(image_folder + image_filename))
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('C:\\Users\\KelseyRamsey\\Videos\\Animation\\Red_Salmon.mp4')

#for img in os.listdir(image_folder):
#    if img.endswith('.jpg'):
#        print(img)
#        image_files.append(os.path.join(image_folder + img))
#clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
#clip.write_videofile('C:\\Users\\KelseyRamsey\\Videos\\Animation\\my_video.mp4')


#image_files = [os.path.join(image_folder+ img) for img in os.listdir(image_folder) if img.endswith(".jpg")]
#clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
#clip.write_videofile('C:\\Users\\KelseyRamsey\\Videos\\Animation\\my_video.mp4')