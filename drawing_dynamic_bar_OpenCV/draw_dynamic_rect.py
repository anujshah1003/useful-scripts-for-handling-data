import os
import pandas as pd
import cv2
import numpy as np
from tqdm import tqdm

root_path=r"D:/youtube/data_handling/drawing_dynamic_bar_OpenCV"
frames_path=os.path.join(root_path,"frames")
dest_dir=os.path.join(root_path,"frames_with_plot")
csv_path=os.path.join(root_path,"data.csv")

data_df=pd.read_csv(csv_path)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    
num_frames=len(os.listdir(frames_path))
img=cv2.imread(os.path.join(frames_path,os.listdir(frames_path)[0]))
img_h,img_w,img_c=img.shape
    
RECT_HEIGHT_PX=140
RECT_WIDTH_PX=60

left_eye_rect_st_pt=(1320, 100)
right_eye_rect_st_pt=(1400, 100)
rect_dim=(60,140)
thickness=3
color_valid=(255,0,0)
color_invalid=(0,0,255)

# video writer parameters
video_name="video_dynamic_rect.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 35
video_write = cv2.VideoWriter(video_name, fourcc, fps, (img_w, img_h))

def eye_opening_helper(df,max_dist_px):
    
    """
    returns the number of pixels corresponding to per unit of measurement


    Parameters
    ----------
    df : pandas dataframe
        pandas dataframe containing the data.
    max_dist_px : int
        The height the rectangle 

    Returns
    -------
    le_pixels_per_unit_mm : float
        
    re_pixels_per_unit_mm : float
        DESCRIPTION.

    """

    left_eye_opening_mm=df["left_eyelid_opening_mm"]
    right_eye_opening_mm=df["right_eyelid_opening_mm"]
    leod_min=np.min(left_eye_opening_mm)
    leod_max=np.max(left_eye_opening_mm)
    print(leod_min,leod_max)
    reod_min=np.min(right_eye_opening_mm)
    reod_max=np.max(right_eye_opening_mm)
    print(reod_min,reod_max)

    le_pixels_per_unit_mm=max_dist_px/leod_max
    re_pixels_per_unit_mm=max_dist_px/reod_max

    return le_pixels_per_unit_mm,re_pixels_per_unit_mm

def draw_box(img,st_pt,bbox_dim,color=(255,0,0),thickness=3):
    
    """
    draw bounding box. if thicknes is -1 the box is filled inside

    Parameters
    ----------
    img : np.ndarray
        The image in which teh rectangle would be drawn
    st_pt : tuple
        starting point of the rectangle
    bbox_dim : tuple
        (width,height) of the rectangle
    color : tuple, optional
        The color code of the rectangle. The default is (255,0,0).
    thickness : real number, optional
        The thickness of teh rectangle. if thickness is -1 teh box is filled. 
        The default is 3.

    Returns
    -------
    img.

    """
    x,y=st_pt
    bb_w,bb_h=bbox_dim
    img=cv2.rectangle(img, (x, y), (x+bb_w, y+bb_h), color, thickness)
    return img

# get the pixels per unit distance
le_pixels_per_unit_mm,re_pixels_per_unit_mm = eye_opening_helper(data_df,max_dist_px=RECT_HEIGHT_PX)


for i in tqdm(range(0,num_frames,2)):
    img_name="frame_{}.png".format(i)
    img_path=os.path.join(frames_path,img_name)
    img=cv2.imread(img_path)
    
     # draw left eye and right eye empty bbox
    img = draw_box(img,left_eye_rect_st_pt,rect_dim,color=(255,0,0),thickness=3)
    img = draw_box(img,right_eye_rect_st_pt,rect_dim,color=(255,0,0),thickness=3)
    
    img = cv2.putText(img, "Frame-{}".format(i), (100,100), cv2.FONT_HERSHEY_SIMPLEX,
                           0.7, [255, 255, 255], 1, cv2.LINE_AA)
    
    img = cv2.putText(img, "Left", (left_eye_rect_st_pt[0],left_eye_rect_st_pt[1]-30), cv2.FONT_HERSHEY_SIMPLEX,
                           0.7, [0, 255, 0], 1, cv2.LINE_AA)
    img = cv2.putText(img, "Eye", (left_eye_rect_st_pt[0],left_eye_rect_st_pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX,
                           0.7, [0, 255, 0], 1, cv2.LINE_AA)
    img = cv2.putText(img, "Right", (right_eye_rect_st_pt[0],right_eye_rect_st_pt[1]-30), cv2.FONT_HERSHEY_SIMPLEX,
                           0.7, [0, 255, 0], 1, cv2.LINE_AA)
    img = cv2.putText(img, "Eye", (right_eye_rect_st_pt[0],right_eye_rect_st_pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX,
                           0.7, [0, 255, 0], 1, cv2.LINE_AA)
    
    # check if the signal is valid , if signal is not valid draw a red box
    left_eye_valid=data_df.loc[i,"left_eyelid_opening_valid"]
    right_eye_valid=data_df.loc[i,"right_eyelid_opening_valid"]
    
    #left_eye_valid=0
    if left_eye_valid:
        left_eye_open=data_df.loc[i,"left_eyelid_opening_mm"]
        #left_eyeOpening = f"  Left eye opening in mm: {left_eye_open:.1f}"
        # draw eye opening of left eye
        eye_opening_h=int(np.ceil(left_eye_open*le_pixels_per_unit_mm))
        # the height of the box should not be greater than the defined box
        eye_opening_h=min(eye_opening_h,RECT_HEIGHT_PX) 
        
        leod_st_pt=(left_eye_rect_st_pt[0],left_eye_rect_st_pt[1]+RECT_HEIGHT_PX-eye_opening_h)
        leod_bbox_dim=(RECT_WIDTH_PX,eye_opening_h)
        
        img = draw_box(img,leod_st_pt,leod_bbox_dim,thickness=-1)
    else:
        #left_eyeOpening = f"  Left eye opening in mm: n/a"
        img = draw_box(img,left_eye_rect_st_pt,rect_dim,color=(0,0,255),thickness=3)
        
    if right_eye_valid:
        right_eye_open=data_df.loc[i,"right_eyelid_opening_mm"]

        #right_eyeOpening = f"  Right eye opening in mm: {right_eye_open:.1f}"
        # draw eye opening of right eye
        eye_opening_h=int(np.ceil(right_eye_open*re_pixels_per_unit_mm))
        # the height of the box should not be greater than the defined box
        eye_opening_h=min(eye_opening_h,RECT_HEIGHT_PX)
        
        reod_st_pt=(right_eye_rect_st_pt[0],right_eye_rect_st_pt[1]+RECT_HEIGHT_PX-eye_opening_h)
        reod_bbox_dim=(RECT_WIDTH_PX,eye_opening_h)
        
        img = draw_box(img,reod_st_pt,reod_bbox_dim,thickness=-1)
    else:
        #right_eyeOpening = f"  Right eye opening in mm: n/a"
        img = draw_box(img,right_eye_rect_st_pt,rect_dim,color=(0,0,255),thickness=3)

    dest_img_name=os.path.join(dest_dir,img_name)
    cv2.imwrite(dest_img_name,img)
    video_write.write(img)
video_write.release()
cv2.destroyAllWindows()
print("finished generating ",video_name)
