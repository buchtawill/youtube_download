#make sure to use modified pytube not pytube from pip if you want status updates on download speed
from pytube import YouTube 
from moviepy.editor import *
import sys
import time

def dieWithError(s: str):
    print(s)
    exit()
    

if __name__ == '__main__':
        
    if(len(sys.argv) < 2):
        dieWithError('Python script to download a youtube video.\nUsage: python download_video.py <url>')
        
    url = sys.argv[1]
    
    yt = YouTube(url)
    
    print(f"Selected video: \'{yt.title}\' from the channel \'{yt.author}\'")
    
    #get video and audio streams
    video_only = yt.streams.filter(only_video=True)
    audio_only = yt.streams.filter(only_audio=True)
    
    #choose which video stream to download
    print("\nChoose a video stream to download by entering itag:")
    for stream in video_only:
        s = str(stream)[9:]
        s = s[0:(s.find('progressive'))]
        s += f' filesize(MB):{stream.filesize_mb}'
        s = s.replace(' ','\t')
        print('\t' + s)
        
    videoitag = input("itag: ")
    if(not videoitag.isdigit()):
        dieWithError(f"Your input \'{videoitag}\' is not an integer. Exiting.")
    
    videoitag = int(videoitag)
    video_stream = yt.streams.get_by_itag(videoitag)
    
    
    #choose which audio stream to download
    print("\nChoose an audio stream to download by entering itag:")
    for stream in audio_only:
        s = str(stream)[9:]
        s = s[0:(s.find('progressive'))]
        s += f' filesize(MB):{stream.filesize_mb}'
        s = s.replace(' ','\t')
        print('\t' + s)
    audioItag = input("itag: ")
    if(not audioItag.isdigit()):
        dieWithError(f"Your input \'{audioItag}\' is not an integer. Exiting.")
    audio_stream = yt.streams.get_by_itag(int(audioItag))
    
    #download the video and audio to temporary files
    #add unix time to make sure the path is unique
    
    print("Downloading video...")
    videopath = video_stream.download(filename=f"tempvideo_{int(time.time())}.mp4")
    print("Downloading audio...")
    audiopath = audio_stream.download(filename=f"tempaudio_{int(time.time())}.mp3")
    
    # Load the audio and video files
    audio = AudioFileClip(audiopath)
    video = VideoFileClip(videopath)

    # Combine the audio and video
    final_clip = video.set_audio(audio)

    # Save the combined video
    final_clip.write_videofile(input("Enter name for video: ")+'.mp4')
    audio.close()
    video.close()
    
    #remove temporary files
    os.remove(videopath)
    os.remove(audiopath)
    