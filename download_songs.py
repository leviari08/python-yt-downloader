from downloader import download_audio
import os

def download_songs_from_file(file_name):
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


if __name__ == "__main__":
    download_songs_from_file(file_name='songs.txt')
