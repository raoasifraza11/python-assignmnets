#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*-  This Assignments implements 40 builtin str func() -*-
# Encoding schema https://www.python.org/dev/peps/pep-0263
""" ▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬
                 1 
    ▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
from core import feture_requested  ## imported function form file
import traceback


feture_requested("1")

greeting = "hello, how are you?!!!"
print str.capitalize.__doc__, "\n" ,greeting.capitalize()


feture_requested("2")
myString = "this is string example....wow!!!" 

# Returns a space-padded string with the original string centered to a total of width columns.
print str.center.__doc__, "\n", myString.center(50, 'a')


feture_requested("3")
secondString = "this is string example....wow!!!" 

sub = "i" 
print "count(sub, 4, 40) : ", secondString.count(sub, 4, 40)
sub = "wow" 
print "count(sub) : ", secondString.count(sub)

feture_requested("4")
thirdString = "this is string example....wow!!!"
thirdString = thirdString.encode('base64', 'strict')

print "Encoded String: " + thirdString
print "Decoded String: " + thirdString.decode('base64', 'strict')

feture_requested("5")
print "Encoded String: " + thirdString.encode('base64','strict')

feture_requested("6")
print "Encoded String: " + thirdString.decode('base64','strict')

feture_requested("7")
forthString = "this is string example....wow!!!"

print forthString
suffix = "wow!!!" 
print forthString.endswith(suffix) , ":: endwith(suffix)->" ,suffix
print forthString.endswith(suffix,20) , ":: endwith(suffix, 20)->" ,suffix

suffix = "is" 
print forthString.endswith(suffix, 2, 4) , ":: endwith(2, 4)->" ,suffix
print forthString.endswith(suffix, 2, 6) , ":: endwith(2, 6)->" ,suffix


feture_requested("8")
fifthString = "this is\tstring example....wow!!!" 


print "Original string: " + fifthString
print "Defualt exapanded tab: " + fifthString.expandtabs()
print "Double exapanded tab: " + fifthString.expandtabs(16)

feture_requested("9")
inputString = "this is string example....wow!!!" 
searchingQuery = "exam" 
print "string:: ", inputString
print "Query:: ", searchingQuery
print inputString.find(searchingQuery), "index"
print inputString.find(searchingQuery, 10), "index"
print inputString.find(searchingQuery, 40), "index mean not found"

feture_requested("10")
print "return index"
print inputString.index(searchingQuery)
print inputString.index(searchingQuery, 10)

feture_requested("11")
numberTest = "this2009"
print numberTest.isalnum()

alphastring = "this is string example....wow!!!"
print alphastring.isalnum()

feture_requested("12")
alphastirngexample = "thisisstring"
print alphastirngexample.isalpha()

feture_requested("13")
a = "124"
print a.isdigit()

feture_requested("14")
print alphastirngexample.islower()

feture_requested("15")
print alphastirngexample.isupper()

feture_requested("16")
alphastirngexample = u"this0234"        # litral string
print alphastirngexample.isnumeric()

feture_requested("17")
alphastirngexample = u"this0234"        # litral string
alphastirngexample1 = u"  "        # litral string
print alphastirngexample.isspace()
print alphastirngexample1.isspace()

feture_requested("18")
alphastirngexample = u"this0234"        # litral string
print alphastirngexample.istitle()

feture_requested("19")
s = "-" 
seq = ("a", "b", "c")  # This is sequence of strings.
print s.join( seq )

feture_requested("20")
lenghtstring = "this is string example....wow!!!" 

print "Length of the string: ", len(lenghtstring)

feture_requested("21")
lenghtstring = "this is string example....wow!!!" 

print lenghtstring.ljust(50, '0')

feture_requested("22")
lenghtstring = "this is string example....wow!!!" 

print lenghtstring.upper()

feture_requested("23")
lenghtstring = "this is string example....wow!!!" 

print lenghtstring.lower()

feture_requested("24")
print lenghtstring.lstrip()
updatestr = "88888888this is string example....wow!!!8888888" 
print updatestr.lstrip('8')

feture_requested("25")
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

mystring = "this is string example....wow!!!"
print mystring.translate(trantab)


feture_requested("26")
print "Max character: " + max(mystring)


feture_requested("27")
print "Max character: " + min("this-is-real-string-example....wow!!!")

feture_requested("28")
replaceStr = "this is string example....wow!!! this is really string"
print replaceStr.replace("is", "was")
print replaceStr.replace("is", "was", 3)

feture_requested("29")
string1 = "this is really a string example....wow!!!" 
string2 = "is" 

print string1.rfind(string2)

print string1.rfind(string2, 0, 10)
print string1.rfind(string2, 10, 0)

print string1.find(string2)
print string1.find(string2, 0, 10)
print string1.find(string2, 10, 0)

feture_requested("30")
string1 = "this is really a string example....wow!!!"
string2 = "is"

print string1.rindex(string2)
print string1.index(string2)

feture_requested("31")
string1 = "this is really a string example....wow!!!"
print string1.rjust(50, '0')

feture_requested("32")
string1 = "this is really a string example....wow!!!"
print string1.rstrip()
string2 = "88888888this is string example....wow!!!8888888"
print string2.rstrip('8')

feture_requested("33")
splitstringEx = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print splitstringEx.split()
print splitstringEx.split(' ', 1)

feture_requested("34")
linestring = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d"
print linestring.splitlines()
print linestring.splitlines(0)
print linestring.splitlines(3)
print linestring.splitlines(1)
print linestring.splitlines(4)

feture_requested("35")
linestring = "this is the world"
print linestring.startswith( 'this' )

feture_requested("36")
linestring = "this is the world"
print linestring.swapcase()

feture_requested("37")
linestring = "this is the world"
print linestring.title()

feture_requested("38")
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

trans = "this is string example....wow!!!"
print trans.translate(trantab)

feture_requested("39")
trans = "this is string example....wow!!!"
print trans.zfill(40)
print trans.zfill(50)

feture_requested("40")
trans = u"this is string example....wow!!!"
print trans.isdecimal()






