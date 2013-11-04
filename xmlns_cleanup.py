#!/usr/bin/python

import sys
import os.path
import re

# Codes to print bold text and reset to normal text
bold = "\033[1m"
reset = "\033[0;0m"
re_nmsp = re.compile(r'(xmlns:(\w+?)="http://.+?")')

all_nmsp = {\
'a4j': 'xmlns:a4j="http://richfaces.org/a4j"',\
'c': 'xmlns:c="http://java.sun.com/jsp/jstl/core"',\
'colorPicker': 'xmlns:colorPicker="http://richfaces.org/sandbox/colorpicker"',\
'composite': 'xmlns:composite="http://java.sun.com/jsf/composite"',\
'crt': 'xmlns:crt="http://sourceforge.net/projects/jsf-comp"',\
'e': 'xmlns:e="http://java.sun.com/jsf/composite/components"',\
'f': 'xmlns:f="http://java.sun.com/jsf/core"',\
'fn': 'xmlns:fn="http://java.sun.com/jsp/jstl/functions"',\
'h': 'xmlns:h="http://java.sun.com/jsf/html"',\
'o': 'xmlns:o="http://omnifaces.org/ui"',\
'of': 'xmlns:of="http://omnifaces.org/functions"',\
'p': 'xmlns:p="http://primefaces.org/ui"',\
'pe': 'xmlns:pe="http://primefaces.org/ui/extensions"',\
'pt': 'xmlns:pt="http://xmlns.jcp.org/jsf/passthrough"',\
'rich': 'xmlns:rich="http://richfaces.org/rich"',\
's': 'xmlns:s="http://jboss.org/schema/seam/taglib"',\
'ui': 'xmlns:ui="http://java.sun.com/jsf/facelets"',\
}

def processfile(flname):
  if not os.path.exists( flname ) :
    print ("Input file " + flname + " not found!")
    return
  f = open(flname)
  lines = f.read().splitlines()
  f.close()

  not_found = ()
  name_spaces = ()
  for line in lines:
    m = re_nmsp.search(line)
    while not m is None:
      if m.group(2) in all_nmsp and all_nmsp[m.group(2)] == m.group(1):
        name_spaces += (m.group(2),)
        s = "<" + m.group(2) + ":"
        not_found += (s,)
      else:
        print(flname + " : unknown namespace " + m.group(0))
      m = re_nmsp.search(line, m.end())
        
    if len(name_spaces) > 0 and ">" in line:
      break

  for line in lines:
    new_not_found = ()
    for n in not_found:
      if not n in line:
        new_not_found += (n,)
    not_found = new_not_found
    if len(not_found) == 0:
      break

#  for n in not_found:
#    print(n)
      
  
# Print script usage
def printusage(errorcode):
  print("Usage:", bold, "nmsp files...")
  sys.exit(errorcode);
 
# Check for arguments
argc = len(sys.argv)
getwhat = "content"
if argc >= 2:
  query = sys.argv[1]
  for i in range(1,argc):
    processfile(sys.argv[i])
else:
  printusage(1)
