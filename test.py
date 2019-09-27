import re

print("Run script? (y/n)")
file = open('test.html')
fileString = file.read()

fileString = fileString.replace("--", "&mdash;")
fileString = fileString.replace("&nbsp;", "")
fileString = fileString.replace("W.P. Carey", "W.&nbsp;P.&nbsp;Carey")
fileString = fileString.replace("W. P. Carey", "W.&nbsp;P.&nbsp;Carey")
fileString = fileString.replace("W.P.Carey", "W.&nbsp;P.&nbsp;Carey")
fileString = fileString.replace("<strong>","<h2>")
fileString = fileString.replace("</strong>","</h2>")
fileString = fileString.replace("<p><h2>","<h2>")
fileString = fileString.replace("<p></h2>","</h2>")
fileString = fileString.replace("Economy@W. P. Carey", "Economy@W.&nbsp;P.&nbsp;Carey")



print(fileString)

file.close()