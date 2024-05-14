import os
import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def title():
    print(Fore.GREEN + "\nImage Crawler" + Style.RESET_ALL)

# Function to download image
def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

# Function to search for images
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
        print(Fore.BLUE + f"Downloading image {i+1} of {len(images)}..." + Style.RESET_ALL)
        download_image(img_url, f'{save_dir}/image{i}.jpg')
        time.sleep(1)

    print(Fore.GREEN + "Download complete!" + Style.RESET_ALL)
    return len(images)

# Print Title And Provide Choices
title()

print(Fore.RED + "\nDisclaimer: The author is not responsible for any misuse of this application.")
print("Please respect copyright laws and terms of service of any website you use this on." + Style.RESET_ALL)

while True:
    url = input(
        Fore.YELLOW + "\nEnter a website URL to crawl for images (or 'q' to quit): " + Style.RESET_ALL)
    if url.lower() == 'q':
        break

    print(Fore.YELLOW + "\n1. Download to the default Downloads folder" + Style.RESET_ALL) 
    print(Fore.YELLOW + "2. Specify a different folder" + Style.RESET_ALL)
    choice = input(Fore.YELLOW + "\nEnter your choice (1 or 2): " + Style.RESET_ALL)

    if choice == '1':
        save_dir = os.path.expanduser('~/Downloads')
    else:
        save_dir = input(
            Fore.YELLOW + "\nEnter a directory to save the images: " + Style.RESET_ALL)

    print(Fore.GREEN + "\nStarting image crawl..." + Style.RESET_ALL)
    time.sleep(2)

    try:
        num_images = crawl_images(url, save_dir)
        print(Fore.GREEN + f"\nFound {num_images} images." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\nAn error occurred: {e}" + Style.RESET_ALL)