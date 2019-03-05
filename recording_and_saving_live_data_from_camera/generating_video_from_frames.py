import os
import cv2
data_path= 'D:\\incabin-monitoring\\module-1-cleanliness-detection\\DATA\\cleanliness_detection_IR\\dataset_17_Jan_2018'
frame_dir = 'cleanliness_detection_IR'
frame_subdir = 'wallet_car_2_640x480'
output_vid_dir = 'cleanliness_detection_video'

#PATH = os.getcwd()
frame_path = os.path.join(data_path,frame_subdir)

img_list = os.listdir(frame_path)
#num_frames = 2000
frame = cv2.imread(os.path.join(frame_path,'0.png'))
height, width, channels = frame.shape
output = 'raw_{}'.format(frame_subdir)+'_20fps.mp4'
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
img_list = os.listdir(frame_path)

num_images = len(img_list)
num_frames =num_images
for i in range(num_frames):
    img_name = os.path.join(frame_path,str(i) +'.png')
#    img = None
#    print (img_name)
    try:
        img = cv2.imread(os.path.join(frame_path,img_name))
        out.write(img) # Write out frame to video
    except:
        print(img_name + ' does not exist')
    
    if img is not None:
        cv2.imshow('img',img)
        cv2.waitKey(1)
        # Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))
