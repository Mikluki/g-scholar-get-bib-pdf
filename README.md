usage: gsch.py [-h] [-m] [-pdf] pubs [pubs ...]

Script for batch download of bib files and corresponding pdfs

positional arguments:
  pubs        publication titles

options:
    -h, --help  show this help message and exit
    -m          manually accept search result
    -pdf        download pdf of the article via scihub

Examples:

    ./gsch.py 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'
    ./gsch.py -pdf 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors' 'Del Rio Castillo A E et al 2018 High-yield production of 2D crystals by wet-jet milling Mater. Horiz. 5 890–904' 'Karagiannidis P G et al 2017 Microfluidization of graphite and formulation of graphene-based conductive inks ACS Nano'
