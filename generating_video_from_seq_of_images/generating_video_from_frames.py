import os
import cv2

def convert_frames_to_video(input_list,output_file_name,fps,size):
    
    '''
    Function to write the sequence of frames into a video 
    
    Arguments:
        input_list - list - list of image names/frame names that need to be converted to a video 
        output_file_name - string - the output file path along with the file name
                                    where the created video will be saved. e.g- 
                                    path/output.mp4
        fps - float - the frame rate of the created video. e.g 25
        size - tuple - the size of each frame. e.g. (640,480)
    '''
    
    # Define the output video writer object 
    out = cv2.VideoWriter(output_file_name, fourcc, fps, size)
    num_frames = len(input_list)

    for i in range(num_frames):
        base_name='img'
        img_name = base_name + '_{:06d}'.format(i) + '.png'
        img_path = os.path.join(input_frame_path,img_name)
        
        try:
            img = cv2.imread(img_path)
            out.write(img) # Write out frame to video
        except:
            print(img_name + ' does not exist')
        
        if img is not None:
            cv2.imshow('img',img)
            cv2.waitKey(1)
    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
    print("The output video is {} is saved".format(output_file_name))

if __name__=='__main__':
    
    path = os.getcwd()
    data_dir='DATA'
    data_subdir = 'phone'
    output_vid_dir = 'output_video'

    if not os.path.exists(output_vid_dir):
        os.mkdir(output_vid_dir)
    #PATH = os.getcwd()
    input_frame_path = os.path.join(path,data_dir,data_subdir)
    
    img_list = os.listdir(input_frame_path)
#    img_list = glob.glob(input_frame_path+'/*.png')
    #num_frames = 2000
    frame = cv2.imread(os.path.join(input_frame_path,'img_000000.png'))
    height, width, channels = frame.shape
    fps = 20
    output_file_name = 'output_video/{0}_{1}fps.mp4'.format(data_subdir,fps)
    # Define the codec.FourCC is a 4-byte code used to specify the video codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    size = (width,height)
    convert_frames_to_video(img_list,output_file_name,fps,size)
