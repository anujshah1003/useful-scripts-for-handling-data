import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image

def main():

    st.set_page_config(layout="wide", page_title="Image Comparison APP")

    st.write("## Compare two images")

    st.sidebar.write("## Upload the images to compare :gear:")
    file1=None
    file2=None

    # Upload the images
    file1 = st.sidebar.file_uploader("Upload image 1", type=["png", "jpg", "jpeg"],accept_multiple_files=False)
    file2 = st.sidebar.file_uploader("Upload image 2", type=["png", "jpg", "jpeg"],accept_multiple_files=False)

    filename_1, filename_2 = st.columns([1, 1])

    if file1 and file2:
        img1 = Image.open(file1)
        img2 = Image.open(file2)

        ## Display image
        with filename_1: st.write(f"Image 1: {file1.name}")
        with filename_2: st.write(f"Image 2: {file2.name}")

        image_comparison(img1,img2,label1="Image 1",label2="Image 2",width=1100)
    else:
        st.write("select images to compare")

if __name__ == "__main__":
    main()