"""
This programm allows users to enter the link of the video that they want to download from youtube and saves them to their computers as they want them to be
"""

from pytube import YouTube
import os

def Download(link, save_path, file_name):
    youtubeObject = YouTube(link)

    # Get the highest resolution stream
    youtubeStream = youtubeObject.streams.get_highest_resolution()

    # Download the video with the specified file name
    try:
        # Specify the file name and extension (e.g., video.mp4)
        file_path = os.path.join(save_path, f"{file_name}.mp4")
        youtubeStream.download(output_path=save_path, filename=f"{file_name}.mp4")
        print("Download is completed successfully.")
    except:
        print("An error has occurred.")


# Ask the user for the YouTube video URL
link = input("Enter the YouTube video URL: ")

# Ask the user for the path where they want to save the video
save_path = input("Enter the folder path to save the video (or press Enter for default. i.e, Downloads): ")

# If the user didn't specify a save path, use the Downloads folder
if not save_path:
    save_path = os.path.expanduser("~/Downloads")

# Ask the user for the desired file name (without extension)
file_name = input("Enter the desired file name (without extension): ")

# Call the Download function with the specified link, save path, and file name
Download(link, save_path, file_name)


#@@@@@@@@@@@@@@
# from pytube import YouTube
# import os
#
#
# def Download(link, save_path):
#     youtubeObject = YouTube(link)
#
#     # Get the highest resolution stream
#     youtubeStream = youtubeObject.streams.get_highest_resolution()
#
#     # Download the video
#     try:
#         # Specify the file extension as .mp4
#         youtubeStream.download(output_path=save_path, filename="video.mp4")
#         print("Download is completed successfully.")
#     except:
#         print("An error has occurred.")

