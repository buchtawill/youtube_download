from pytube import YouTube #make sure to use modified pytube not pytube from pip
import sys

def dieWithError(s: str):
    print(s)
    exit()
    

if __name__ == '__main__':
        
    if(len(sys.argv) < 2):
        dieWithError('Python script to download a youtube video.\nUsage: python download_video.py <url>')
        
    url = sys.argv[1]
    
    yt = YouTube(url)
    
    print(f"Selected video: \'{yt.title}\' from the channel \'{yt.author}\'")
    
    audio_only = yt.streams.filter(only_audio=True)
    
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
    fname = input("Enter filename for audio: ")   
    print("Downloading audio...")
    audiopath = audio_stream.download(filename=f"{fname}.mp3")
    
    