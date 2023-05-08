
import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
import time

def next():
    st.session_state.counter += 1
def prev():
    st.session_state.counter -= 1
if 'counter' not in st.session_state: 
    st.session_state.counter = 0

def main():

    st.set_page_config(layout="wide", page_title="Image Comparison APP")

    st.write("## Compare two images")

    st.sidebar.write("## Upload the images to compare :gear:")
    file1=None
    file2=None

    # Upload the images

    file1 = st.sidebar.file_uploader("Upload image 1", type=["png", "jpg", "jpeg"],accept_multiple_files=True)
    file2 = st.sidebar.file_uploader("Upload image 2", type=["png", "jpg", "jpeg"],accept_multiple_files=True)

    # App layout
    #container = st.empty()
    cols = st.columns(2)
    # button_prev, button_next = st.columns([1, 1])
    button_prev, button_next = cols[0],cols[1]

    with button_next: 
        st.button("Next Image ➡️", on_click=next) #, use_container_width=True)
    with button_prev: 
        st.button("⬅️ Previous Image", on_click=prev) #, use_container_width=True)  

    filename_1, filename_2 = st.columns([1, 1])

    if file1 and file2:
        images1 = [Image.open(file) for file in file1]
        images2 = [Image.open(file) for file in file2]

        n_imgs = len(images1)

        ## Select image based on the current counter
        idx = st.session_state.counter%n_imgs
        img1 = images1[idx]
        img2 = images2[idx]

        ## Display filename
        st.write(f"Image Count: {idx+1}/{n_imgs}")
        with filename_1: st.write(f"Image 1: {file1[idx].name}")
        with filename_2: st.write(f"Image 2: {file2[idx].name}")

        ## Display image
        image_comparison(img1,img2,label1="Image 1",label2="Image 2",width=1100)
    else:
        st.write("select images to compare")
if __name__ == "__main__":
    main()
