# video_downloader
Download course videos

# How to use
1. Configure the burpsuite tool with your browser.
2. Burpsuite -> Project Options -> sessions -> Edit session handling rule -> scope -> enable the proxy
3. Login to the course.
4. Capture the course name from the url bar.
5. Run the script with following details

```python
└─$ python video_downloader -h                                                                                                                                                                                                                      2 ⨯
usage: video_downloader [-h] -d DOWNLOAD_LOCATION {talk_python} ...

download videos

optional arguments:
  -h, --help            show this help message and exit
  -d DOWNLOAD_LOCATION, --download_location DOWNLOAD_LOCATION
                        provide the download location

courses:
  {talk_python}         see [course] --help for more details

```

