#!/usr/bin/env python3

# author: greyshell

from bs4 import BeautifulSoup
from .downloader import Downloader
import time
import os
from os import path

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class TalkPython(Downloader):
    TALKPYTHON_BASE_URL = "https://training.talkpython.fm"

    def __get_link(self, video_id):
        """
        download the video file
        """
        headers = {'Referer': f"{self.TALKPYTHON_BASE_URL}/"}
        link_url = f"player/video/{video_id}?quality=direct&hi_dpi=True"
        response = requests.get(f"{self.TALKPYTHON_BASE_URL}/{link_url}",  # nosengrep
                                proxies=self.proxyDict,
                                headers=headers,
                                allow_redirects=False,
                                verify=False
                                )

        time.sleep(self.SLEEP_VALUE)
        if response.status_code == 302:
            return response.headers['Location']

    def process(self):
        """
        parse the HTML to get the download url
        """
        link_url = f"courses/details/{self.module_name}"
        res = requests.get(f"{self.TALKPYTHON_BASE_URL}/{link_url}",  # nosengrep
                           proxies=self.proxyDict,
                           allow_redirects=True,
                           verify=False
                           )

        html_body = BeautifulSoup(res.text, "html.parser")
        table_body = html_body.find('table', attrs={'class': 'table borderless'})

        # HTML parsing logic
        rows = table_body.find_all('tr')
        counter = ch_dir = None
        for row in rows:
            cols = row.find_all('td')
            link = cols[0].find('a')['href']
            video_id = link.split("/")[-1]
            video_title = cols[0].text.strip()
            if video_title.startswith('Ch '):
                ch_dir = self.location + "/" + self.module_name + "/" + video_title
                if not os.path.exists(ch_dir):
                    os.makedirs(ch_dir)
                    self.logger.info(f"Created directory: {ch_dir}")

                counter = 1
                continue

            video_link = self.__get_link(video_id)

            download_path = f"{ch_dir}/{counter} {video_title.replace('/', '')}.mp4"

            if path.exists(download_path):
                self.logger.warning(f"Skipped the file: {download_path}")
            else:
                result = self.file_download(video_link, download_path)

                if self.file_download(video_link, download_path) == 0:
                    self.logger.info(f"Downloaded: {download_path}")
                else:
                    self.logger.error(f"Unable to download: {download_path}")
            counter += 1
