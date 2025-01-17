# -*- coding: utf-8 -*-
"""NovelGen.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KOKJX7fWceT86fgYKyKVXH0dsrxCIUjH
"""

!pip install -q markovify
!pip install weasyprint

import markovify
from weasyprint import HTML

with open("Lord.txt") as f:
  text = f.read()

text_model = markovify.Text(text)

for i in range(5):
  print(text_model.make_sentance())


#∞

from google.colab import files

FF = files.upload()
for fn in FF.keys():
  text = FF[fn].decode()

from google.colab import files

FF = files.upload()
for fn in FF.keys():
  text = FF[fn].decode()

with open("BEN.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5):
    print(text_model.make_sentence())

print(text)

text_model = markovify.Text(text)

for i in range(100):
    print(text_model.make_sentence())

# First, import a couple things we need
import random
from weasyprint import HTML

# Then, generate the novel 

novel ='<h1>Tolken Fast Tolken Furious</h1><h2>By HP® Spectre x360 2017 Model</h2><br><br><p>'
for i in range(49):
  novel += f"</p><h2>Chapter {i + 1}</h2>"
  for i in range(150):
    novel += str(text_model.make_sentence())
    

# Now, add the novel into an HTML template
# note the 'f' at the beginning of this string, and the {novel} which is the 
# placeholder for substitution.

html_template = f"""
<html>
  <head>
  <title>FF∞</title>
  </head>
  <body>
  {novel}
  </body>
</html>
"""

# Finally, this line saves that template as a PDF using the HTML module of WeasyPrint
HTML(string=html_template).write_pdf("Tolken Fast Tolken Furious.pdf")
word_count = len(novel.split(" "))
print("word count: " + str(word_count))

word_count = len(novel.split(" "))
print("word count: " + str(word_count))

#  <style>
#   body {{
#     font-family: "Times New Roman";
#   }}
#   </style>

# all scripts obtained from https://www.springfieldspringfield.co.uk/