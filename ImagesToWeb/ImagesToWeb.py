import glob, os

def main():
    os.chdir(".")
    text_file = open("images.html", "w")
    text_file.write("""<!DOCTYPE html>
    <html lang="en-US">
    <head>

    <title>HTML img tag</title>    <head></head>    <body>    """)
    
    for file in glob.glob("*.jpg"):
        text_file.write("<a href=\""+file+"\"><img src=\""+file+"\" width=800></a>\n")

    text_file.write("""</body>
    </html>""")

    text_file.close()

if __name__ == "__main__":
    main()