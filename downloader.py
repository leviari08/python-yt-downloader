# For legal reasons, this script has been made only of the sake of learning #

from pytube import YouTube
from moviepy.editor import VideoFileClip
import os


def download_video(url):
    '''
    downloads a video from url
    '''
    yt = YouTube(url)
    final_stream = yt.streams.get_highest_resolution()

    if final_stream is None:
        print('No stream is available')
        return

    if os.path.isfile(f'videos/{final_stream.default_filename}'):
        print('File already exists')
        return

    print(f'Downloading {yt.title}')
    final_stream.download('videos/')


def download_audio(url):
    '''
    downloads a video from url and converting it to audio
    '''
    yt = YouTube(url)
    final_stream = yt.streams.get_highest_resolution()

    if os.path.isfile(f'videos/{final_stream.default_filename[:-4]}.mp3'):
        print('File already exists')
        return

    download_video(url)

    '''
    A problem I noticed
    the mp3 file shows longer length (by about 2.5%)
    The file itself is okay, my guess is metadata problem
    (also happens in ffmpeg)
    '''
    convert_to_mp3(final_stream.default_filename)
    os.remove(f'videos/{final_stream.default_filename}')

    '''
    "Get highest bitrate audio stream for given codec (defaults to mp4)"
    downloads the audio as mp4 file with black screen
    '''
    # another_stream = yt.streams.get_audio_only()


def convert_to_mp3(video_file_name):
    '''
    converts mp4 file to mp3 file
    '''
    with VideoFileClip(f'videos/{video_file_name}') as video:
        audio = video.audio
        audio.write_audiofile(f'videos/{video_file_name[:-4]}.mp3')


if __name__ == "__main__":
    print('python yt downloader')
