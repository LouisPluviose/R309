import time 
import multiprocessing

def main():
    
    def task():
        print(f"Task started")
        time.sleep(1)
        print(f"Task finished")

    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()

    end = time.perf_counter()

    print(f"Took {round(end - start, 2)} seconds")

if __name__ == "__main__":
    main()