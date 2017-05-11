#!/usr/bin/python

from axmlparserpy.axmlprinter import AXMLPrinter
from xml.dom import minidom
from zipfile import ZipFile
import sys


def extractManifest(apkFile):
	ap = AXMLPrinter(ZipFile(apkFile).read("AndroidManifest.xml"))
	return minidom.parseString(ap.getBuff()).toxml()


if __name__ == "__main__":

	if len(sys.argv) != 2 or not sys.argv[1].lower().endswith(".apk"):
		print "Expected APK file, usage:"
		print "python " + sys.argv[0] + " /path/to/file.apk"
		quit()
	outputManifestFile = "/tmp/AndroidManifest.xml.tmp"
	manifestFile = open(outputManifestFile, "wb")
	manifestFile.write(extractManifest(sys.argv[1]))#.encode('utf-8'))
	manifestFile.close()

	#print extractManifest(sys.argv[1])
	
