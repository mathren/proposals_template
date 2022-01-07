(TeX-add-style-hook
 "template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "12pt" "letter")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "colorlinks" "citecolor=red" "linkcolor=red" "urlcolor=red") ("natbib" "sort&compress" "numbers")))
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl12"
    "epsfig"
    "amsmath"
    "amsfonts"
    "amssymb"
    "listings"
    "booktabs"
    "setspace"
    "hyperref"
    "xcolor"
    "natbib"
    "lipsum"
    "wrapfig"
    "xhfill"
    "sectsty"
    "pgfgantt"
    "multicol"
    "caption"
    "paralist"
    "enumitem"
    "framed")
   (TeX-add-symbols
    '("Secref" 1)
    '("Tabref" 1)
    '("Figref" 1)
    '("Eqref" 1)
    '("sectionLine" 1)
    '("highlight" 1)
    '("todo" 1)
    "bull"
    "udef"
    "olditem"
    "newblock"
    "tempone"
    "temptwo"
    "aj"
    "apj"
    "apss"
    "apjl"
    "apjs"
    "aa"
    "aap"
    "araa"
    "mnras"
    "mnrasl"
    "cqg"
    "prl"
    "natexlab")
   (LaTeX-add-counters
    "TODOLIST"))
 :latex)

