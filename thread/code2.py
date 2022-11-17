import time 

def main():

    def task(i):
        print(f"Task {i} started")
        time.sleep(1)
        print(f"Task {i} finished")

    start = time.perf_counter()

    task(1)
    task(2)

    end = time.perf_counter()

    print(f"Took {round(end - start, 2)} seconds")

if __name__ == "__main__":
    main()