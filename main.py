from pytube import YouTube #pip install pytube
import os

while True:
    url = input("Моля въведи адрес на връзката.")
    print("url:" + url)

    # url = 'https://www.youtube.com/watch?v=0UZqilsvq-Qqqq'

    video = YouTube(url)

    print(f'Име на Видеото: {video.title}')
    print(f'Приблизително време за изтегляне:{video.length} secunde')
    print(f'Големина на видеото:{video.streams.get_highest_resolution().filesize / (1024 ** 2): .2f} MB')

    destop_path = os.path.expanduser("~/Dekstop")

    video.streams.get_highest_resolution().download(output_path=destop_path)
    print('Готово')