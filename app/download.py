import os
from os.path import join, abspath, dirname
import requests

# change to backslash while deploying
path = join(dirname(abspath("__file__")), 'static\\app\\img')

link = "https://source.unsplash.com/random/1920x1080"
response = requests.get(link, allow_redirects=True)
open(f"{path}\\bg.jpg",     # also here
     "wb").write(response.content)
