[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/anujshah645)

# Useful Scripts for Handling Data

Small Python scripts and notebooks for preparing, inspecting, visualizing, and organizing data for machine learning and deep learning projects.

## Topics

| Topic | Location | What it does |
| --- | --- | --- |
| Create dataset CSV files | [`creating_csv_files.py`](creating_csv_files.py) | Reads flower image folders, assigns labels, checks images, and writes train/test CSV files. |
| Convert data distributions | [`converting_data_distribution/`](converting_data_distribution/) | Notebook examples for converting and visualizing data distributions. |
| Dynamic OpenCV bars | [`drawing_dynamic_bar_OpenCV/`](drawing_dynamic_bar_OpenCV/) | Draws data-driven bars on image frames and creates an annotated video. See the [topic README](drawing_dynamic_bar_OpenCV/README.md). |
| Images to video | [`generating_video_from_seq_of_images/`](generating_video_from_seq_of_images/) | Converts one image sequence, or multiple image folders, into MP4 videos. |
| Plotly graphs | [`plotly_graphs/`](plotly_graphs/) | Interactive HTML charts for hardware and model performance comparisons. |
| Record camera data | [`recording_and_saving_live_data_from_camera/`](recording_and_saving_live_data_from_camera/) | Captures webcam frames and saves them as numbered images. |
| Rename files in sequence | [`renaming_multiple_files_in_sequence/`](renaming_multiple_files_in_sequence/) | Renames files in one or more folders using consistent numbered names. |
| Compare images in Streamlit | [`streamlit_image_comparison_app_demo/`](streamlit_image_comparison_app_demo/) | Runs a web app for comparing single or multiple image pairs. See its [README](streamlit_image_comparison_app_demo/README.md). |

## Getting started

1. Clone or download the repository.
2. Create and activate a Python virtual environment.
3. Install the packages required by the example you want to use. Common packages include `opencv-python`, `numpy`, `pandas`, `matplotlib`, `plotly`, `tqdm`, and `streamlit`. The image comparison app has its own [`requirements.txt`](streamlit_image_comparison_app_demo/requirements.txt).
4. Read the selected script before running it and update its input/output paths, filenames, labels, and camera settings for your data.
5. Run a script from its project directory, for example:

```bash
python creating_csv_files.py
python drawing_dynamic_bar_OpenCV/draw_dynamic_rect.py
streamlit run streamlit_image_comparison_app_demo/streamlit_image_comp_multiple_files.py
```

## Important notes

- Most examples operate on local data and do not download input files automatically.
- Several scripts expect specific folder layouts such as `DATA`, `frames`, or class-named image folders.
- Some older examples use absolute Windows paths; replace those paths before running them.
- The camera and video examples require OpenCV and access to a webcam or suitable image frames.
- Jupyter notebooks can be opened and run with Jupyter Notebook, JupyterLab, or VS Code.
