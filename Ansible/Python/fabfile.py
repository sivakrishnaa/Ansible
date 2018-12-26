#!/usr/bin/python

import os

def package():
 exitcode = os.system("apt --help")

 if exitcode == 0:
   print "Debian family OS detected."
   os.system("sudo apt install git -y")
 elif exitcode != 0:
   print "RedHat family OS detected."
   os.system("yum install vsftpd -y")
 else:
   print "Unsupported OS detected."
