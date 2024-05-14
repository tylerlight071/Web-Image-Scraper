import os
import requests
from bs4 import BeautifulSoup


def title():
    print("""
 ___  _____ ______   ________  ________  _______           ________  ________  ________  ___       __   ___       _______   ________     
|\  \|\   _ \  _   \|\   __  \|\   ____\|\  ___ \         |\   ____\|\   __  \|\   __  \|\  \     |\  \|\  \     |\  ___ \ |\   __  \    
\ \  \ \  \\\__\ \  \ \  \|\  \ \  \___|\ \   __/|        \ \  \___|\ \  \|\  \ \  \|\  \ \  \    \ \  \ \  \    \ \   __/|\ \  \|\  \   
 \ \  \ \  \\|__| \  \ \   __  \ \  \  __\ \  \_|/__       \ \  \    \ \   _  _\ \   __  \ \  \  __\ \  \ \  \    \ \  \_|/_\ \   _  _\  
  \ \  \ \  \    \ \  \ \  \ \  \ \  \|\  \ \  \_|\ \       \ \  \____\ \  \\  \\ \  \ \  \ \  \|\__\_\  \ \  \____\ \  \_|\ \ \  \\  \| 
   \ \__\ \__\    \ \__\ \__\ \__\ \_______\ \_______\       \ \_______\ \__\\ _\\ \__\ \__\ \____________\ \_______\ \_______\ \__\\ _\ 
    \|__|\|__|     \|__|\|__|\|__|\|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|\|____________|\|_______|\|_______|\|__|\|__|
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         """)


def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)


def crawl_images(url, save_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, img in enumerate(images):
        img_url = img.get('src')
        if not img_url.startswith('http'):
            img_url = url + img_url
        download_image(img_url, f'{save_dir}/image{i}.jpg')


# Print Title And Provide Choices
title()

print("\nDisclaimer: The author is not responsible for any misuse of this application.")
print("Please respect copyright laws and terms of service of any website you use this on.")


url = input("Enter a website URL to crawl for images: ")

print("1. Download to the default Downloads folder")
print("2. Specify a different folder")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    save_dir = os.path.expanduser('~/Downloads')
else:
    save_dir = input("Enter a directory to save the images: ")

crawl_images(url, save_dir)
