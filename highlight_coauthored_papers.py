#!/usr/bin/python
# author: Mathieu Renzo


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
            bibitem_running = "" # to read one entry at a time
            for i, line in enumerate(b):
                # copy verbatim first two lines, these are \begin{thebibliography} etc.
                if (i == 0) or\
                   (i == 1):
                    bbl_out.writelines(line)
                    continue
                # copy last line too
                if "\end{thebibliography}" in line:
                    bbl_out.writelines(line)
                    continue # should exit
                # add line 3+ to the bibitem we are reading
                bibitem_running += str(line)
                # empty line indicates end of bibitem
                if (len(line.strip()) == 0):
                    # found end of bibitem
                    # print(bibitem_running)
                    # print("---------------")
                    # check if author is coauthor
                    coauthor = check_author(bibitem_running, author)
                    if coauthor:
                        # add latex bold face to this one
                        bibitem_running = "\n"+r"\textbf{"+"\n"+bibitem_running.rstrip("\n")+"\n"+r"}"+"\n\n"
                    # add to file
                    bbl_out.writelines(bibitem_running)
                    # reset bibitem_running
                    bibitem_running = ""


if __name__=="__main__":
    bbl = sys.argv[1]
    author = sys.argv[2]
    try:
        outfile = sys.argv[3]
        highlight_coauthored_papers(bbl, author, outfile)
    except IndexError:
        highlight_coauthored_papers(bbl, author)
