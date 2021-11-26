#!./venv/Scripts/python.exe

# For legal reasons, this script has been made only of the sake of learning #

from downloader import download_audio
import os
from multiprocessing.dummy import Pool as ThreadPool


def download_songs_from_file(file_name: str) -> None:
    '''
    downloads all songs from the given file
    '''
    if not os.path.isfile(file_name):
        print('File not exists')
        return

    with open(file_name, 'r') as file:
        for line in file:
            print('\n' + line.strip())
            download_audio(line.strip())


def download_songs_from_file_multithreading(file_name: str, number_of_threads: int) -> None:
    '''
    downloads all songs from the given file, with multiple threads
    useful for bulk downloads
    '''
    if not os.path.isfile(file_name):
        print('File not exists')
        return

    pool = ThreadPool(number_of_threads)

    with open(file_name, 'r') as file:
        raw_lines = file.readlines()
        lines = list(map(str.strip, raw_lines))

    pool.map(download_audio, lines)

    pool.close()
    pool.join()
