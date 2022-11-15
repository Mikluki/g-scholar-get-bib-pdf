## Description
Script for batch download of bib files and corresponding pdf files, which uses publication titles (or bibliography references) as arguments.
- bibliography and publication url are automatically appended to the lit.bib file.
- Saved pdfs are automatically named: year_name(delimiter = '-'); with special characters removed.
    >2016_Production-of-highly-monolayer-enriched-dispersions-of-liquid-exfoliated-nanosheets-by-liquid-cascade-centrifugation.pdf

### Based on
- https://github.com/Tishacy/SciDownl
- https://github.com/scholarly-python-package/scholarly

### Important
Scholarly is used without proxy. Google scholar does not like bots, which means that sometimes your ip can be temporarily blocked (maybe several minutes). So ideally you want to set up your own proxy. Block criteria unclear. If it happened you can temporarily use vpn. I suppose the number of queries per some period of time is limited. Nonetheless, script was successfully tested for 25 publications several times.


## Usage 
    gsch.py [-h] [-m] [-pdf] pubs [pubs ...]

__Positional arguments:__  
    pubs  &emsp;&emsp; &emsp;    publication titles separated with space  

__Options:__  
-h, --help&emsp;&emsp;show this help message and exit  
-m    &emsp;&emsp; &emsp; &emsp;manually accept search result  
-pdf &emsp;&emsp;&emsp;&emsp;download pdf of the article via scihub  

### Examples:

    ./gsch.py 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'
    ./gsch.py -pdf "Winchester, A.; Ghosh, S.; Feng, S. M.; Elias, A. L.; Mallouk, T.; Terrones, M.; Talapatra, S. ACS Appl. Mater. Interfaces 2014, 6, 2125−2130." "Voiry, D.; Salehi, M.; Silva, R.; Fujita, T.; Chen, M.; Asefa, T.; Shenoy, V. B.; Eda, G.; Chhowalla, M. Nano Lett. 2013, 13, 6222−6227."
