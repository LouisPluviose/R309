import threading
import time

def main():

    def task(i):
        print(f"Task {i} started")
        time.sleep(1)
        print(f"Task {i} finished")

    start = time.perf_counter()

    t1 = threading.Thread(target=task, args=(1,))
    t1.start()

    t2 = threading.Thread(target=task, args=(2,))
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"Took {round(end - start, 2)} seconds")

if __name__ == "__main__":
    main()