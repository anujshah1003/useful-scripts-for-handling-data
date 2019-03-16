import cv2
import os

PATH = os.getcwd()
output_data_dir = 'DATA'

if not os.path.exists(output_data_dir):
    os.mkdir(output_data_dir)


# Read a single frame for the camera to define the properties of video writer object
cap = cv2.VideoCapture(0)
ret, img = cap.read()
height,width,channel = img.shape
cap.release()
#fourcc – 4-character code of codec used to compress the frames. 
#List of codes can be obtained at Video Codecs by FOURCC page.
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
size = (width,height)
fps=25

# Function to record and save video
def record_video(output_name='vid',write_video=False):
    # Start Video
    # Initializing the input device
    cap = cv2.VideoCapture(0)
    # Defining the frame resolution
#    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    if cap.isOpened():
        ret, img = cap.read()
        print (img.shape)
    else:
        ret = False
        
    video_name = output_name
    
    frame_num = 0
    # Defining the output path
    folder_name = os.path.join(PATH,output_data_dir,video_name) + '/'
    
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        
    # Define the output vide writer object which will be writing the frames to video
    output_file_name = 'DATA/{0}_{1}fps.mp4'.format(output_name,fps)
    out = cv2.VideoWriter(output_file_name, fourcc, fps, size)

    while ret:
        
        ret, img = cap.read()
        base_name='img'
        output_file_name = base_name + '_{:06d}'.format(frame_num) + '.png'
        output_file_path = folder_name + output_file_name
        if write_video:
            cv2.imwrite(output_file_path, img) # writing frames to defined location
            out.write(img) # writing frames to video writer
        frame_num += 1
        print("Frame no. ", frame_num)
        cv2.putText(img,"Frame: {}".format(frame_num), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255),2)
        cv2.imshow("image",img)
        print (img.shape)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Release everything if job is finished
            cv2.destroyAllWindows()
            out.release()
            cap.release()
            break

if __name__ == "__main__":
    record_video(output_name='test_2',write_video=True) 

