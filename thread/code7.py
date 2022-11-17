import time 
import concurrent.futures
import requests

def main():
    
    img_urls = ['https://pixabay.com/images/id-7546974/','https://pixabay.com/images/id-19830/']

    def download_image(img_url):
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[4]
        img_name = f'{img_name}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{img_name} was downloaded...')

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()

    print(f'Took {round(end - start, 2)} seconds')

if __name__ == "__main__":
    main()