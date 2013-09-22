#!/usr/bin/python

import socket
import sys

UDP_IPADDR = "127.0.0.1"
UDP_PORT = 2047

byteArray = bytearray(2);
byteArray[0] = 17;
byteArray[1] = 33;

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

bytelimit = 0;
while True:
    client.sendto(byteArray, (UDP_IPADDR, UDP_PORT));
    bytelimit=bytelimit+1

    if bytelimit == sys.argv[1]:
        break
