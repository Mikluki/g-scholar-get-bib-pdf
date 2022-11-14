#!/usr/bin/env python3

### Imports ###

import argparse
import sys
from scidownl import scihub_download

from scholarly import scholarly
from fuzzy_match import algorithims
import re
from datetime import datetime

class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def query_bib_title(bibtex: dict) -> bool:
    return query_yes_no(bibtex["title"])

### ======================================================
# Scholarly get bibtex
def get_bibtex_for_pubs(pubs: str) -> str:
    """Returns bibtex"""
    search_query = scholarly.search_pubs(pubs)
    for result in search_query:
        if args.m != True:
            return result['pub_url'], scholarly.bibtex(result)
        else:
            if query_bib_title(result["bib"]):
                return result['pub_url'], scholarly.bibtex(result)

    raise NotFoundError(f"Can't find {pubs}")


def write_to_file(bibtex, url='', fname='out.bib'):
    print(f'Saving to {fname}\n')
    with open(fname, "a") as f:
        f.write(url+'\n'+bibtex)
        f.write('\n')


def download_one_paper(url, fname, folder='gsch-pdf'):
    fname.replace(' ','-')
    paper = url
    paper_type = "pmid"
    out = f"./{folder}/{fname}"
    scihub_download(paper, paper_type=paper_type, out=out)


def make_filename(bib):
    biblines = bib.split('\n')
    for line in biblines:
        line = re.sub(r"\s+", "", line, flags=re.UNICODE)
        # print(line)
        if bool(re.search(r'^title={', line)):
            try:
                title = line.split('title={')[1].split('}')[0]
            except:
                print("'title' was not found in bib")
                title = ''

        if bool(re.search(r'^pub_year={', line)):
            try:
                pub_year = line.split('pub_year={')[1].split('}')[0]
            except:
                print("'pub_year' was not found in bib")
    if pub_year+'-'+title != '':
        return pub_year+'_'+re.sub('[^A-Za-z0-9]+', '-', title)
    else:
        return datetime.now().strftime('%H-%M-%S')



# def search_pubs_in_bib(bib: str, pubs:str) -> str:
#     """Returns matched bibtex ID"""
#     with open(bib) as bibtex_file:
#         bib_database = bibtexparser.load(bibtex_file)

#     def match_algo(titlez, key) -> float:
#         if regex.search('(%s){e<=1}' % key, title, flags=regex.IGNORECASE):
#             return 0.8
#         return algorithims.trigram(title, key)


#     match_threshold = 0.7
#     results : List[Tuple[float, dict]] = []

#     for entry in bib_database.entries:
#         if 'title' in entry:
#             score = match_algo(entry['title'], pubs)
#             match_result = (score, entry)
#             results.append(match_result)

#     results.sort(key=lambda x: x[0], reverse=True)
#     for result in results:
#         if result[0] >= match_threshold and query_bib_title(result[1]):
#             return result[1]['ID']

#     raise NotFoundError(f"no match for 'l{pubs} in {bib}")


# def prepend_to_bib(new_entry: str, bibfile: str):
#     with open(bibfile) as bibtex_file:
#         bib_database = bibtexparser.load(bibtex_file)

#     new_database = bibtexparser.loads(new_entry)
#     bib_database.entries.insert(0, new_database.entries[0])

#     with open(bibfile, 'w') as bibtex_file:
#         bibtexparser.dump(bib_database, bibtex_file)


if __name__ == "__main__":
    example_text = """Examples:
    ./gsch.py 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'
    ./gsch.py -pdf 'Steep-Slope Hysteresis-Free Negative-Capacitance 2D Transistors'
    """
    description = "Get bibtex from Google Scholar and download pdf"

    parser = argparse.ArgumentParser(description=description,
            epilog=example_text,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('pubs', type=str, nargs='+', help="publication titles")
    parser.add_argument('-m', action='store_true', help="manually accept search result")
    parser.add_argument('-pdf', action='store_true', help="download pdf of the article via scihub")

    args = parser.parse_args()
    # print(args.m)


    for i, pub in enumerate(args.pubs):
        print(f"# Searching key words: {pub}")
        url, bibtex = get_bibtex_for_pubs(pub)

        print(url,'\n',bibtex)
        write_to_file(bibtex, url=url, fname='lit.bib')

        if args.pdf == True:
            print(f"## Dowloadingig: {pub}")

            try:
                fname = make_filename(bibtex)
                download_one_paper(url, fname, folder='gsch-pdf')
            except:
                print(f"Error: SciHub could not download {pub}")

