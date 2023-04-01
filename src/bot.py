import concurrent.futures
import os

import cv2
import names
from pyzbar.pyzbar import decode
from tqdm import tqdm

from src.req import Request
from src.utils import invert_image, simplify_image

MAX_THREADS = os.cpu_count()


class Bot:
    def __init__(self, base_url, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.request = Request(base_url)

    def start(self, requests_each_scan=1):
        print("Starting bot... (Press 'q' to quit)")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                continue

            frame = simplify_image(frame)

            # Show the frame
            cv2.imshow('QR code detector', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            url = self._search_url(frame)
            if url is None:
                # Try to invert the image
                frame = invert_image(frame)
                url = self._search_url(frame)

            if url is None:
                # Skip if url is None
                continue

            uid = url.split("/")[-1]
            self._process_uid(uid, amount=requests_each_scan)

    def _search_url(self, image):
        data = decode(image)
        if len(data) > 0 and (url := data[0].data.decode("utf-8")):
            return url

        return None

    def _process_uid(self, uid, amount):
        print(f"Sending {amount} requests to uid: {uid}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            future_to_uid = {executor.submit(
                self.request.send, uid, names.get_first_name()): uid for i in range(amount)}
            results = []

            with tqdm(total=len(future_to_uid)) as pbar:
                for future in concurrent.futures.as_completed(future_to_uid):
                    uid = future_to_uid[future]
                    try:
                        result = future.result()
                        results.append(result)
                        pbar.update(1)
                    except Exception as exc:
                        print(f"Failed to process {uid}: {exc}")

            print(f"Finished sending {amount} requests to uid: {uid}")
            print(f"Results: {results}")
