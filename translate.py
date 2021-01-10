#!/usr/bin/env python
# File: scribus-translator.py - Extracts the text from a document, saving to a
# text file also lists image files with pathnames
# 2006.03.04 Gregory Pittman template script ('Text Exporter')
# 2008.02.28 Petr Vanek - fileDialog replaces valueDialog
# 2018.06.22 bastianilso : scribus-translator
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import scribus
import traceback


def translateText(textfile):
    page = 1
    pagenum = scribus.pageCount()
    newStrings = []
    formatStart = '<!--ORIGINAL START-->' + '\n'
    formatEnd = '\n<!--ORIGINAL END-->\n<!--TRANSLATION START-->\n<!--TRANSLATION END-->\n'
    while (page <= pagenum):
        scribus.gotoPage(page)
#       scribus.messageBox("DEBUG", "page: " + str(page), icon=0, button1=1)
        pageItems = scribus.getPageItems()
        for item in pageItems:
            if (item[1] == 4):
                contents = scribus.getAllText(item[0])
                translation = matchTranslation(contents, textfile)
                if (translation == 'NEEDS_TRANSLATION'):
                    newStrings.append(formatStart + contents + formatEnd)
                else:
                    scribus.setText(translation, item[0])
        page += 1
    if (len(newStrings) > 0):
        f = open(textfile, 'a')
        for text in newStrings:
            f.write(text)
        f.close()


def matchTranslation(contents, textfile):
    returnString = "NEEDS_TRANSLATION"
    original = False
    translation = False
    match = False
    with open(textfile) as f:
        originalText = ''
        translatedText = ''
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            if line == '<!--ORIGINAL START-->':
                original = True
                continue
            if line == '<!--ORIGINAL END-->':
                original = False
                if (contents == originalText):
                    match = True
                originalText = ''
                continue
            if line == '<!--TRANSLATION START-->':
                translation = True
                continue
            if line == '<!--TRANSLATION END-->':
                translation = False
                if match:
                    if (translatedText == ''):
                        returnString = contents
                    returnString = translatedText
                    break
                translatedText = ''
                continue
            if original:
                originalText += line
                continue
            if translation:
                translatedText += line
                continue
#           scribus.messageBox("DEBUG", "unknown text!\n\n" + line, icon=0, button1=1)
    return returnString


if scribus.haveDoc():
    textfile = scribus.fileDialog('Open a translation file',
                                  filter='Text Files (*.txt);;All Files (*)')
    try:
        if textfile == '':
            raise Exception
        else:
            translateText(textfile)
    except Exception:
        scribus.messageBox('Error', traceback.format_exc(),
                           icon=0, button1=1)
else:
    scribus.messageBox('Export Error', 'You need a Document open',
                       icon=0, button1=1)
