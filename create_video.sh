#!/bin/bash
# Script to generate a video from frames and move it to the videos folder

# Usage: ./create_video.sh <frames_dir> <fps> <video_name.mp4>

set -e  # Exit if any command fails

# Input validation
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <frames_dir> <fps> <video_name.mp4>"
    exit 1
fi

frames_dir=$1
fps=$2
video_name=$3
videos_dir="./assets/large_files/videos"
init_dir=$(pwd)

# Ensure frames directory exists
if [ ! -d "$frames_dir" ]; then
    echo "Error: Frames directory '$frames_dir' does not exist."
    exit 1
fi

# Ensure videos directory exists (create if not)
mkdir -p "$videos_dir"

# Step 1: Go to frames folder and create filelist.txt
cd "$frames_dir"
ls *.png | sort -V | sed 's/^/file /' > filelist.txt

# Step 2: Generate video with ffmpeg
ffmpeg -y -f concat -safe 0 -r "$fps" -i filelist.txt -c:v libx264 -pix_fmt yuv420p "$video_name"

# Step 3: Move the video to the videos folder
cd "$init_dir"
mv "$frames_dir/$video_name" "$videos_dir/"

echo "✅ Video created and moved to $videos_dir/$video_name"
