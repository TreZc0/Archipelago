from __future__ import annotations


import os
import sys
vendor_dir = os.path.join(os.path.dirname(__file__), "worlds", "poe", "poeClient", "vendor")
vendor_dir = os.path.join(os.path.dirname(__file__), "worlds", "poe", "poeClient")
if vendor_dir not in sys.path:
    sys.path.insert(0, vendor_dir)

from worlds.poe.Client import launch
import Utils

if __name__ == "__main__":
    Utils.init_logging("poe", exception_logger="Client")
    launch()
