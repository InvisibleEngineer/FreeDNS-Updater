#!/usr/bin/python
import sys
import os
import time
import stat
from urllib.request import urlopen
import socket
import argparse

socket.setdefaulttimeout(120)

debug = False
def msg(str):
    if debug:
        print(str)

parser = argparse.ArgumentParser(description = "Updates the IP of a freedns domain")
parser.add_argument('update_key',
                    help='The update key of the domain, located at the end of the direct update link')
parser.add_argument('ip_file', default='/var/freedns_ip',
                    nargs = '?', help='The file where the last known IP address is stored')
parser.add_argument('-d', '--debug', action='store_true', help='Turn on debugging')
args = parser.parse_args()

debug = args.debug
msg("Arguments passed:")
msg(str(args))

# FreeDNS Update URL
update_url = "http://freedns.afraid.org/dynamic/update.php?" + args.update_key
msg("Using update url " + update_url)

# External IP URL (must return an IP in plain text)
ip_url = "http://automation.whatismyip.com/n09230945.asp"
msg("Using IP checking url " + ip_url)

# Open URL to return the external IP
external_ip = urlopen(ip_url).read().decode('utf-8')
msg("Got external IP " + external_ip)

# Create the file if it doesnt exist otherwise update old IP
if not os.path.exists(args.ip_file):
    fh = open(args.ip_file, "w")
    fh.write(external_ip)
    fh.close()
    last_external_ip = "Unknown"
    print("Created FreeDNS IP log file: " + args.ip_file)
    print("External IP updated to (" + str(external_ip) + ")")
else:
    fh = open(args.ip_file, "r")
    last_external_ip = fh.readline()

# Check old IP against current IP and update if necessary
if last_external_ip != external_ip and last_external_ip != "Unknown":
    urlopen(update_url)
    print("External IP updated FROM (" + str(last_external_ip) + ") TO (" + str(external_ip) + ")")
    fh = open(args.ip_file, "w")
    fh.write(external_ip)
    fh.close()
elif last_external_ip != "Unknown":
    last_ip_update = time.ctime(os.stat(args.ip_file).st_mtime)
    print("External IP (" + str(external_ip) + ") has not changed. Last update was " + str(last_ip_update))
