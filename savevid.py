from regex import F
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# SaveVideo
# Coded by Mugi F.
# Github https://github.com/SaveVideo
# 2022-04-28

print(""" \033[35m
 _____             __ __ _   _         
|   __| __ _ _ ___|  |  |_|_| |___ ___ 
|__   ||. | | | -_|  |  | | . | -_| . |
|_____|___|\_/|___|\___/|_|___|___|___|\033[39m\n""")

sirah = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'identity',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '127',
    'Origin': 'https://savevideo.me',
    'Connection': 'keep-alive',
    'Referer': 'https://savevideo.me/en/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
    
}
def pilihan():
        print(" 1. Single Download")
        print(" 2. Mass Download")
        choice = input(" >>> ")
        choice = int(choice)
        if choice == 1:
            link = input(" Input Link : ")
            isi = {
                "url": link,
                "form": "Download"
                }
            get = requests.post('https://savevideo.me/en/get/', data=isi, headers=sirah)
            try:
                filename = BeautifulSoup(get.text, 'html.parser').find_all(href=True)[0]
                video = requests.get(filename['href'], stream=True, verify=False)
                ukuran = int(video.headers.get('content-length', 0))
                block_size = 1024
                progress_bar = tqdm(total=ukuran, unit='iB', unit_scale=True)
                with open(filename['href'].rsplit('/', 1)[-1].split('.mp4')[0]+".mp4", 'wb') as file:
                    for data in video.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)
                    progress_bar.close()
                    print("\033[32m File Saved\033[39m : "+filename['href'].rsplit('/', 1)[-1].split('.mp4')[0]+".mp4")
            except IndexError:
                        print(" "+link+" \033[31m[FAILED]\033[39m")
        elif choice == 2:
            fn = input(" Input Filename : ")
            with open(fn, 'r') as filelink:
                for line in filelink:
                    xline = line.replace('\n', '')
                    isi = {
                        "url": xline,
                        "form": "Download"
                        }
                    get = requests.post('https://savevideo.me/en/get/', data=isi, headers=sirah)
                    try:
                        filename = BeautifulSoup(get.text, 'html.parser').find_all(href=True)[0]
                        video = requests.get(filename['href'], stream=True, verify=False)
                        ukuran = int(video.headers.get('content-length', 0))
                        block_size = 1024
                        progress_bar = tqdm(total=ukuran, unit='iB', unit_scale=True)
                        with open(filename['href'].rsplit('/', 1)[-1].split('.mp4')[0]+".mp4", 'wb') as file:
                            for data in video.iter_content(block_size):
                                progress_bar.update(len(data))
                                file.write(data)
                            progress_bar.close()
                            print("\033[32m File Saved\033[39m : "+filename['href'].rsplit('/', 1)[-1].split('.mp4')[0]+".mp4")
                            print("-"*80)
                    except IndexError:
                        print(" "+xline+" \033[31m[FAILED]\033[39m")
                        print("-"*80)
pilihan()