#!/usr/bin/env python

import sys
import yaml

def document_class():
  print "\documentclass{resume}"

def packages():
  print "\usepackage[left=0.75in,top=0.6in,right=0.75in,bottom=0.6in]{geometry}"

def about(about_dictionary):
  print "\\name{"+about_dictionary['first']+" "+about_dictionary['last']+"}"
  print "\\contact{" + about_dictionary['phone'] + "}"
  print "\\contact{" + about_dictionary['email']+"}" 

def begin():
  print "\\begin{document}"

def education(education_dictionary):
  print "\\begin{rSection}{Education}"
  
  for key in education_dictionary:
    print "{\\bf " + key['school'] + ", " + key['location'] + \
            "} \hfill {\em " + str(key['start']) + " - " + \
            str(key['end'])+ "} \\\\ "
    print key['qualification'] + "\\\\"
  
  print "\end{rSection}"

def experience(experience_dictionary):
  print "\\begin{rSection}{Experience}"

  for key in experience_dictionary:
    print "\\begin{rSubsection}{" + key['employer'] + "}{" + \
            str(key['start']) + " - " + str(key['end']) +"}{"+ \
            key['title']+"}{"+ key['location']+"}"
    for item in key.get('notes'):
        print "\item " + item 
    print "\end{rSubsection}"
  print "\end{rSection}"

def end():
  print "\\end{document}"

def main():
  cv_file = sys.argv[1]
  stream = file(cv_file, 'r')
  cv_object = yaml.load(stream)
  document_class()
  packages()
  about(cv_object.get('about'))
  begin()
  education(cv_object.get('education'))
  experience(cv_object.get('experience'))
  end()

if __name__ == '__main__':
  main()
