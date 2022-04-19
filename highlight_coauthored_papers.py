#!/usr/bin/python
# author: Mathieu Renzo
# synposys: python highlight_coauthored_papers.py <author> <*.bbl> <OPTIONAL: output bbl file>

import sys

def check_author(bibitem, author):
    """
    Given a string for a bibitem and a string for an author, returns
    true if author appears in bibitem
    """
    if author.lower() in bibitem.lower():
        return True
    else:
        return False


def highlight_coauthored_papers(bbl, author, outfile=None):
    """
    Creates a new bbl file from a bbl file created by bibtex with ultracompact.bst style
    wrapping \textbf around entries containing the string author

    Parameters:
    ----------
    bbl: `str` path to bbl file. This has to exist as created by BibTex
    author: `string` author last name. Not case sensitive
    outfile: `str` or None, optional. Name of output file. If not given, use same prefix and _highlighted.bbl at the end

    Returns:
    -------
    nothing, but creates a new file.
    """
    # open input as read only to prevent accidents
    with open(bbl, "r") as b:
        if not outfile:
            outfile = bbl.rstrip(".bbl")+"_highlighted.bbl"
        with open(outfile, "w") as bbl_out:
            bibitem_running = "" # to read one bibitem at a time
            found_first_bibitem = False
            for i, line in enumerate(b):
                # copy verbatim lines until first \bibitem
                if (r"\bibitem" not in line) and (not found_first_bibitem):
                    bbl_out.writelines(line)
                    continue
                # copy last line too
                elif "\end{thebibliography}" in line:
                    bbl_out.writelines(line)
                    continue # should exit
                else:
                    found_first_bibitem = True # to never log lines verbatim again
                    # build the bibitem we are reading by adding the line
                    bibitem_running += str(line)
                    # empty line indicates end of bibitem
                    if (len(line.strip()) == 0):
                        # found end of bibitem
                        # check if author is coauthor
                        coauthor = check_author(bibitem_running, author)
                        if coauthor:
                            # add latex bold face to this one
                            bibitem_running = "\n"+r"\textbf{"+"\n"+bibitem_running.rstrip("\n")+"\n"+r"}"+"\n\n"
                            # add to file
                    bbl_out.writelines(bibitem_running)
                    # reset bibitem_running
                    bibitem_running = ""
    print("Done!")
    print("Find the new bbl file with your citations highlighted at")
    print(outfile)


if __name__=="__main__":
    author = sys.argv[1]
    bbl = sys.argv[2]
    try:
        outfile = sys.argv[3]
        highlight_coauthored_papers(bbl, author, outfile)
    except IndexError:
        highlight_coauthored_papers(bbl, author)
