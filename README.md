
# Usage

```
usage: google_scholar.py [-h] [-f bibtex] pubs

Get bibtex from Google Scholar

positional arguments:
  pubs        publication title

optional arguments:
  -h, --help  show this help message and exit
  -f bibtex   look up this bibtex before searching Google Scholar

Examples:
    ./google_scholar.py 'ZygOS: Achieving Low Tail Latency for Microsecond-scale Networked Tasks'
    ./google_scholar.py 'Snap: a Microkernel Approach to Host Network' -f ref.bib
```