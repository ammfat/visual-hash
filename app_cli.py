#!/usr/bin/env python

from identicon import Identicon
from datetime import datetime
import sys

def main():
    start = datetime.now()

    try:
        uname = str(sys.argv[1])
    except:
        uname = 'init'

    idcon = Identicon(uname.lower())

    idcon_data = idcon.identicon_data

    print(f"String to visualize\t: {uname}")
    print(f"Hash value\t\t: {idcon_data['hash']}")
    print(f"Foreground Color\t: {idcon_data['rgb']}")
    
    print()

    idcon.calculate()
    idcon.get_image()

    end = datetime.now()
    print(f"Time to execute: {end - start}")


if __name__ == "__main__":
    main()