#!/usr/bin/python
import os
os.system("dnf update -y")
os.system("dnf upgrade -y")
os.system("dnf clean all -y")
os.system("updatedb")
print "\n"
print "Great job =)"

