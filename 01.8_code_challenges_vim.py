# Python3 program to Validate the Roman numeral
import re
 
def ValRoman(string):
    pat = re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    print(bool(pat, string)))
 
string=input()
 
ValRoman(string)
