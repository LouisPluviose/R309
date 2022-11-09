import time 
import multiprocessing
import threading
import concurrent.futures
import requests

def main():

    urls = ['https://pixabay.com/images/id-7546974/','https://pixabay.com/images/id-19830/']

    def download_image(img_url):
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[4]
        img_name = f'{img_name}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{img_name} was downloaded...')

    start = time.perf_counter()

    t1 = threading.Thread(target=download_image, args=(urls[0],))
    t2 = threading.Thread(target=download_image, args=(urls[1],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print("Threading.Thread")
    print(f'Took {round(end - start, 2)} seconds')
    print("\n")

    start = time.perf_counter()

    p1 = multiprocessing.Process(target=download_image, args=(urls[0],))
    p2 = multiprocessing.Process(target=download_image, args=(urls[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()

    print("Multithreading")
    print(f'Took {round(end - start, 2)} seconds')
    print("\n")

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)

    end = time.perf_counter()

    print("concurrent.futures.ThreadPoolExecutor")
    print(f'Took {round(end - start, 2)} seconds')

if __name__ == "__main__":
    main()