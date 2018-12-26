import glob
import os
import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
ep = ExecutePreprocessor(timeout=600, kernel_name='kernel-spec')

files = glob.glob('*/*/Program.cs', recursive=True)
meta = {'kernelspec': {'display_name': 'C#',
  'language': 'csharp',
  'name': 'kernel-spec'},
 'language_info': {'file_extension': '.cs',
  'mimetype': 'text/x-csharp',
  'name': 'C#',
  'pygments_lexer': 'c#',
  'version': '4.0.30319'}}

for f in files:
    fn = f.replace('\\','/')
    fgit = fn.replace(" ","%20").replace(chr(0x2002),"%E2%80%82")
    fn = fn.replace(chr(0x2002), " ")
    name_git = fn.split('/')[0]
    fn = fn.replace("1.1", "1-1 ")
    name = fn.split('/')[0]
    if not "-" in name:
        continue

    list_chapter, nr_title = name.split("-")
    chapter = list_chapter.replace("LISTING ", "")
    nr = nr_title.split(" ")[0]
    title = nr_title.replace(nr+" ", "")
    #print(chapter, "%02d"%int(nr), title)
    fname = "LISTING %s-%02d %s.ipynb"%(chapter, int(nr), title)
    #print(fgit)

    nb = nbf.v4.new_notebook()

    s = "# Info"
    nb['cells'].append(nbf.v4.new_markdown_cell(s))
    s = """This example is from
* [github.com/ExamRef70-483/Sample-Code](https://github.com/ExamRef70-483/Sample-Code)
* [%s](https://github.com/ExamRef70-483/Sample-Code/blob/master/%s)\n

## Remember
* Main() is not called automatically. Has to be called manual. Remember '**public**'
* Console.ReadKey() should not be used.
"""%(name_git, fgit)
    nb['cells'].append(nbf.v4.new_markdown_cell(s))

    with open(f, encoding="utf-8-sig") as fs: lines = fs.readlines()
    s = ""
    nspace = "LISTING"
    for line in lines:
        line = line.rstrip()
        line = line.replace("static void Main", "static public void Main")
        line = line.replace("Console.ReadKey", "//Console.ReadKey")
        if "namespace" in line:
            nspace = line.split(" ")[-1]
        s += line + "\n"
    nb['cells'].append(nbf.v4.new_code_cell(s))

    s = "%s.Program.Main(new string[0]);"%(nspace)
    nb['cells'].append(nbf.v4.new_code_cell(s))
    nb['metadata'] = meta

    #ep.preprocess(nb, {'metadata': {}})

    file_path = "./notebooks/"+fname
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    nbf.write(nb, file_path)
    print(file_path)