usage: gsch.py [-h] [-m] [-pdf] pubs [pubs ...]

Get bibtex from Google Scholar and download pdf

positional arguments:
  pubs        publication titles

options:
  -h, --help  show this help message and exit
  -m          manually accept search result
  -pdf        download pdf of the article via scihub

Examples:
    ./gsch.py 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'

    ./gsch.py -pdf 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'
