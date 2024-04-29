from pytube import YouTube #make sure to use modified pytube not pytube from pip
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
    
    video_only = yt.streams.filter(only_video=True, file_extension='mp4')
    audio_only = yt.streams.filter(only_audio=True)
    
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
        
    #add unix time to make sure the path is unique
    
    print("Downloading video...")
    videopath = video_stream.download(filename=f"tempvideo_{int(time.time())}.mp4")
    
    print("Downloading audio...")
    audiopath = audio_stream.download(filename=f"tempaudio_{int(time.time())}.mp3")
    
    