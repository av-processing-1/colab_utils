import os
import subprocess
import youtube_dl

def youtubeDownload(url, filename,formats="best"):
    youtube_downloader_params = {"quiet": False, "outtmpl": output_video_file_path, "format": formats}
    with youtube_dl.YoutubeDL(params=youtube_downloader_params) as ydl:
        ydl.download([video_url])

def video2frames(filename, outPath):
    output_filename = os.path.join(outPath, '%06d.jpg')
    video_to_frames_command = ['ffmpeg', '-loglevel', 'debug', '-i', filename, '-vf', 'fps=24',output_filename]
    subprocess.check_call(video_to_frames_command)

 
