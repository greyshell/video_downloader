# !/usr/bin/env python3

# author: greyshell

import subprocess
import logging
import logging.config
import yaml


class Downloader:

    SLEEP_VALUE = 10
    HTTP_PROXY = "http://127.0.0.1:8080"
    proxyDict = {
        "https": HTTP_PROXY,
    }

    def __init__(self, location, module_name):
        self.module_name = module_name
        self.location = location

        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        self.logger = logging.getLogger(__name__)

    def file_download(self, video_link, download_path):
        args = f"curl --proxy '{self.HTTP_PROXY}' '{video_link}' --insecure -o '{download_path}'"
        result = subprocess.call([args], shell=True)  # nosengrep
        return result

