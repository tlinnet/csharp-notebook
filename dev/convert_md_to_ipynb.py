import glob
import os
import nbformat as nbf

files1 = glob.glob('../*.md', recursive=True)
files2 = glob.glob('../*/*.md', recursive=True)

files = files1 + files2

for f in files:
    fname = f[:-3]

    nb = nbf.v4.new_notebook()
    s = open(f, "r").read()
    s = s.replace(".md", ".ipynb")
    nb['cells'].append(nbf.v4.new_markdown_cell(s))
    nbf.write(nb, fname+".ipynb")
