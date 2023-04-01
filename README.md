# Iterborea Bot

Iterborea Bot is a bot that can be used to level up the Iterborea website level. It is written in Python and uses OpenCV to read the QR code from the webcam and Requests to interact with the website. To improve the speed of the bot, many requests are sent in parallel.

## Disclaimer

This bot is developed for educational purposes only.

## Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/iammatthi/iterborea.git
```

Move into the project directory:

```bash
cd iterborea
```

Create a `config.yml` file by copying the `config.yml.example` file:

```bash
cp config.yml.example config.yml
```

Update the values in the `config.yml` file with your own configuration.

- `base_url`: The base URL of the Iterborea website.
- `video_source`: The URL of the webcam used to record the QR code.
  - 0 or 1 for the default webcam in the system.
  - URL of an IP Webcam. An IP Webcam app can also be used to stream the camera of a mobile device (e.g. [IP Webcam Android App](https://play.google.com/store/apps/details?id=com.pas.webcam)).
  - See [OpenCV documentation](https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html) for more information.
- `requests_each_scan`: The number of requests to send each time a QR code is scanned.

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the bot:

```bash
python main.py
```
