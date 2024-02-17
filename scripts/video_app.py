import streamlit as st
import cv2
import os
from pathlib import Path as pt

def extract_frames(video_path,frames):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Read the frames
    success, frame = video.read()
    count = 0

    # Extract frames until there are no more frames left
    while (count<frames and success):
        # Save the frame as an image file
        cv2.imwrite(f"data/{pt(video_path).name.replace('.','')}{count}.jpg", frame)

        # Read the next frame
        success, frame = video.read()
        count += 1

    # Release the video file
    video.release()

    st.success(f"Frames extracted: {count}")

def main():
    st.title("Video Frame Extractor")

    # File uploader
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])

    if video_file is not None:
        # Play the video file
        st.video(video_file)

        st.write(f"Entity name: {video_file.name.split('.')[0]}")

        if "frames" not in st.session_state:
            st.session_state.frames = 0

        try:

            # Save the video file to the file system
            video_path = os.path.join("data", video_file.name)
            with open(video_path, "wb") as f:
                f.write(video_file.read())

        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        # Add a selection for choosing number of frames to extract or extract all
        extract_option = st.radio("Frames to extract", ("All", "Specify"))

        if extract_option == "All":
            st.session_state.frames = 1000000
        else:
            st.session_state.frames = st.number_input("Number of frames to extract", min_value=1, value=1000, key="frames-count")

            

        # Extract frames when the user clicks the button
            
        if st.button("Extract Frames"):
            st.write(f"Extracting {st.session_state.frames} frames")
            extract_frames(video_path,st.session_state.frames)


if __name__ == "__main__":
    main()