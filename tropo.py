#!/usr/bin/env python3
import re
import sys
from subprocess import run, PIPE


cidr_re = re.compile(r'^_netblocks\.tropo\.com\s+text = "(.+)"', re.M)


def main():
    cmd = "nslookup -q=TXT _netblocks.tropo.com 8.8.8.8"
    txt = run(cmd.split(), encoding="utf8", stdout=PIPE).stdout
    for cidr in cidr_re.findall(txt):
        print(f"tropo,{cidr}")


if __name__ == "__main__":
    sys.exit(main())
