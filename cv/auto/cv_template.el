(TeX-add-style-hook
 "cv_template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "12pt" "letter")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "colorlinks" "citecolor=blue!80!black" "linkcolor=blue!80!black" "urlcolor=blue!80!black") ("textpos" "absolute" "overlay")))
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl12"
    "epsfig"
    "amsmath"
    "amsfonts"
    "amssymb"
    "fontawesome5"
    "listings"
    "booktabs"
    "setspace"
    "hyperref"
    "xcolor"
    "lipsum"
    "xhfill"
    "sectsty"
    "textpos"
    "tabularx"
    "eurosym"
    "paralist"
    "enumitem"
    "framed"
    "fancyhdr")
   (TeX-add-symbols
    '("subSection" 1)
    '("sectionLine" 1)
    '("todo" 1)
    '("Icon" 1)
    "tempone"
    "temptwo")
   (LaTeX-add-counters
    "TODOLIST"))
 :latex)

