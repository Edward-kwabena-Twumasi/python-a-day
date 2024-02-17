import glob
import os

# Get all files matching the pattern
files = glob.glob("frame_*.jpg")
print("deleting {} files matching the pattern => frame_*.jpg".format(len(files)))

# Delete each file
for file in files:
    os.remove(file)