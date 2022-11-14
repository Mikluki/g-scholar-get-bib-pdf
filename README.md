Based on:
- https://github.com/Tishacy/SciDownl
- https://github.com/scholarly-python-package/scholarly

usage: gsch.py [-h] [-m] [-pdf] pubs [pubs ...]

positional arguments:
  pubs        publication titles

options:
- -h, &emsp; --help  show this help message and exit
- -m    &emsp;      manually accept search result
- -pdf    &emsp;    download pdf of the article via scihub

Saved pdf is automatically named: year_name(delimeter = '-')

Example: 2016_Production-of-highly-monolayer-enriched-dispersions-of-liquid-exfoliated-nanosheets-by-liquid-cascade-centrifugation.pdf

Examples:

    ./gsch.py 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'
    ./gsch.py -pdf 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors' 'Del Rio Castillo A E et al 2018 High-yield production of 2D crystals by wet-jet milling Mater. Horiz. 5 890–904' 'Karagiannidis P G et al 2017 Microfluidization of graphite and formulation of graphene-based conductive inks ACS Nano'
