import threading
import time

def download_file(file_name):
    print(f"Starting download of {file_name}...")
    time.sleep(2)  # Simulate a delay in downloading
    print(f"Finished downloading {file_name}.")

t1 = threading.Thread(
    target = download_file("file1.csv")
)

t2 = threading.Thread(
    target = download_file("file2.csv")
)

t3 = threading.Thread(
    target = download_file("file3.csv")
)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All files downloaded...!!!!")