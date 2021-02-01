import argparse
from pytube import YouTube

parser = argparse.ArgumentParser(description="CLI Tool to download Youtube Videos")
parser.add_argument('-u','--url',help="Url for the Video")
parser.add_argument('-o','--out_dir',help="Output Location")
args = parser.parse_args()

def download(url,out_dir):
    try:
        yt = YouTube(url)
    except:
        print("Connection Error")
        return

    videos = yt.streams

    resolution_list = []
    for i in range(len(videos)):
        resolution_list.append((videos[i]).resolution)
    resolution_list = set(resolution_list)
    resolution_list.remove(None)
    print('Available Resolutions -')
    print(resolution_list)
    res = str(input('\n Enter your desired Resolution - '))
    video = videos.filter(resolution=res)
    video.first().download(out_dir)

download(args.url,args.out_dir)