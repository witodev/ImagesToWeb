import glob, os
import re

#http://stackoverflow.com/questions/4623446/how-do-you-sort-files-numerically

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

def main():
    os.chdir(".")
    text_file = open("images.html", "w")
    text_file.write("""<!DOCTYPE html>
<html lang="en-US">
<head>

<title>HTML img tag</title></head><body>""")

    files = glob.glob("*.jpg")
    sort_nicely(files)

    for file in files:
        text_file.write("<a href=\""+file+"\"><img src=\""+file+"\" width=500></a>\n")

    text_file.write("""</body>
    </html>""")

    text_file.close()

if __name__ == "__main__":
    main()