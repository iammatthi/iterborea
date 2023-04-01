import yaml

from src.bot import Bot


def read_config():
    with open("config.yml", "r") as f:
        return yaml.safe_load(f)


def main():
    config = read_config()
    b = Bot(base_url=config["base_url"], video_source=config["video_source"])
    b.start(requests_each_scan=config["requests_each_scan"])


if __name__ == "__main__":
    main()
