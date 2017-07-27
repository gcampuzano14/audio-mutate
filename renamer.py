import os
import re
import easygui as eg


def repl(m):
    inner_word = m.group(1)
    return "".join(['_0', inner_word, '_'])

msg = ""
title = "Select root directory"
default = os.path.abspath("PATHTOFILE_HERE")
root_path = eg.diropenbox(msg, title, default)
print(root_path)
dirs = next(os.walk(root_path))[1]
print(dirs)

for d in dirs:
    files = os.listdir(os.path.join(root_path, d))
    for f in files:
        sub_str = re.sub(r'_(\d{1})_', repl, f)
        print(sub_str)
        os.rename(os.path.join(root_path, d, f),
                  os.path.join(root_path, d, sub_str))
