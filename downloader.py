#!./venv/Scripts/python.exe

# For legal reasons, this script has been made only of the sake of learning #

from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

DOWNLOAD_FOLDER = 'videos'


def download_video(url: str) -> None:
    '''
    downloads a video from url
    '''
    yt = YouTube(url)
    final_stream = yt.streams.get_highest_resolution()

    if final_stream is None:
        print('No stream is available')
        return

    if os.path.isfile(f'{DOWNLOAD_FOLDER}/{final_stream.default_filename}'):
        print('File already exists')
        return

    print(f'Downloading {yt.title}')
    final_stream.download('videos/')


def download_audio(url: str) -> None:
    '''
    downloads a video from url and converting it to audio
    '''
    yt = YouTube(url)
    final_stream = yt.streams.get_highest_resolution()
    print(f'Downloading audio {yt.title}')

    # remove .mp4 extention
    filename_without_extention = \
        os.path.splitext(final_stream.default_filename)

    if os.path.isfile(f'{DOWNLOAD_FOLDER}/{filename_without_extention}.mp3'):
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
    os.remove(f'{DOWNLOAD_FOLDER}/{final_stream.default_filename}')

    '''
    "Get highest bitrate audio stream for given codec (defaults to mp4)"
    downloads the audio as mp4 file with black screen
    '''
    # another_stream = yt.streams.get_audio_only()


def convert_to_mp3(video_file_name: str) -> None:
    '''
    converts mp4 file to mp3 file
    '''
    with VideoFileClip(f'{DOWNLOAD_FOLDER}/{video_file_name}') as video:
        audio = video.audio
        audio.write_audiofile(f'{DOWNLOAD_FOLDER}/{video_file_name[:-4]}.mp3')


def menu() -> None:
    '''
    a menu.
    '''
    margin = 3
    title = 'python yt downloader'

    print(' ' * margin + title + ' ' * margin +
          '\n' + '-' * (2 * margin + len(title)))

    menu_options = [
        '1. download a video (mp4)',
        '2. download a song (mp3)',
        'Q. quit'
    ]

    print('\n'.join(menu_options))

    choice = ''
    while choice.lower() not in ['1', '2', 'q']:
        choice = input(': ')

    if choice.lower() == 'q':
        exit()
    elif choice == '1':
        url = input('Enter the url: ')
        download_video(url)
    elif choice == '2':
        url = input('Enter the url: ')
        download_audio(url)


if __name__ == "__main__":
    menu()
