#!/bin/bash

chmod 777 data
nohup ./data ann -p pkt1q4k0cqtmhtlhyw9w2dha3dxn2fe9u8ez4zvgkad https://stratum.zetahash.com http://pool.pkt.world http://pool.pktpool.io http://pool.pkteer.com > nohup.out
