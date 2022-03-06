# !/usr/bin/env python3

# author: greyshell

import subprocess
import logging
import logging.config
import yaml
import re


class Downloader:
    SLEEP_VALUE = 3
    HTTP_PROXY = "http://127.0.0.1:8080"
    proxy_dict = {
        "http": HTTP_PROXY,
        "https": HTTP_PROXY,
    }

    @staticmethod
    def clean_up(path):
        special_chars = "+:\!#$%^&*()';,/"
        for special_char in special_chars:
            path = path.replace(special_char, '')
        return path

    @staticmethod
    def is_valid_url(url):
        # Regex to check valid URL
        regex = ("((http|https)://)(www.)?" +
                 "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                 "{2,256}\\.[a-z]" +
                 "{2,6}\\b([-a-zA-Z0-9@:%" +
                 "._\\+~#?&//=]*)")

        if url is None:
            return False

        pattern = re.compile(regex)
        return True if re.search(pattern, url) else False

    def __init__(self, location, module_name):
        self.module_name = module_name
        self.location = location

        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        self.logger = logging.getLogger(__name__)

    def file_download(self, video_link, download_path):
        if self.is_valid_url(video_link) is False:
            self.logger.error(f"video_name: {download_path} invalid link: {video_link}")
            return

        # when the url is valid
        args = f"curl --proxy '{self.HTTP_PROXY}' '{video_link}' --insecure -o '{download_path}'"
        result = subprocess.call([args], shell=True)  # nosemgrep
        if result == 0:
            self.logger.info(f"Download Success: {download_path}")
        else:
            self.logger.error(f"video_name: {download_path} link: {video_link}")
