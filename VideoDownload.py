# Import the required libraries
import os
from pytube import YouTube
# Set the URL of the video to be downloaded
url = input('Paste Video Link')


def VideoDownload():
    # Create a YouTube object
    yt = YouTube(url)
    # Get the video with the highest resolution
    video = yt.streams.filter(res="1080p").first()
    # Set the output file name
    output_name = "File1V.mp4"
    # Set the output directory
    output_dir = "/Users/nikhilnarula/Desktop/Tiktok"
    # Create the output path by joining the output directory and file name
    output_path = os.path.join(output_dir, output_name)
    # Download the video
    video.download(output_dir, output_name)
    print("Video downloaded successfully to:", output_path)

def AudioDownload():
    # Create a YouTube object
    yt = YouTube(url)
    # Get the audio stream
    audio_stream = yt.streams.get_audio_only()
    # Set the output file name
    output_name = "File1A.mp3"
    # Set the output directory
    output_dir = "/Users/nikhilnarula/Desktop/Tiktok"
    # Create the output path by joining the output directory and file name
    output_path = os.path.join(output_dir, output_name)
    # Download the audio
    audio_stream.download(output_dir, output_name)
    print("Audio downloaded successfully to:", output_path)

def Combine():
    import subprocess
    # Set the paths to the audio and video files
    audio_path = "/Users/nikhilnarula/Desktop/Tiktok/File1A.mp3"
    video_path = "/Users/nikhilnarula/Desktop/Tiktok/File1V.mp4"
    # Set the output file path
    output_path = "/Users/nikhilnarula/Desktop/Tiktok/Combined.mp4"
    # Use ffmpeg to combine the audio and video files
    subprocess.run(["ffmpeg", "-i", audio_path, "-i", video_path, "-c", "copy", output_path])
    print("Audio and video combined successfully!")


def Spiltter():
    # Replace with the path to the YouTube video file
    input_path = '/Users/nikhilnarula/Desktop/Tiktok/Combined.mp4'
    # Replace with the path to the folder where you want to save the video clips
    output_path = '/Users/nikhilnarula/Desktop/Tiktok'
    # Split the video into 30 second clips
    os.system(f"ffmpeg -i {input_path} -c copy -map 0 -segment_time 30 -f segment {output_path}/%d.mp4")

    # Convert the clips to 1080x1920 resolution
    for video in os.listdir(output_path):
        if video.endswith(".mp4"):
            os.system(f"ffmpeg -i {output_path}/{video} -vf scale=1080:1920 {output_path}/1080x1920_{video}")
            os.remove(f"{output_path}/{video}")
    print('Video Successfully Spilt!')

VideoDownload()
AudioDownload()
Combine()
Spiltter()


