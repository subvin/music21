import pprint
import re

from lxml import etree #need to install lxml
from music21 import instrument
from music21.braille.translation import lookup

#-------------------------------------------------------------------------------

def music():
    """
    http://www.music.vt.edu/musicdictionary/appendix/translations/Translations.html
    """
    f = open('websites/music.html')
    html = etree.HTML(f.read())
    
    englishFrench = {}
    englishGerman = {}
    englishItalian = {}
    englishSpanish = {}
    englishAbbreviations = {}
    
    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        for col in allCols:
            items = [a.text.lower() for a in col.iter("a") if a.text is not None]
            items.extend([p.text.lower() for p in col.iter("p") if p.text is not None])
            if col.text is not None:
                items.append(col.text.lower())
            allSols.append(items)
        for cell in allSols[0]:
            cell = u" ".join(cell.split())
            englishFrench[cell] = [u" ".join(s.split()) for s in allSols[1]]
            englishGerman[cell] = [u" ".join(s.split()) for s in allSols[2]]
            englishItalian[cell] = [u" ".join(s.split()) for s in allSols[3]]
            englishSpanish[cell] = [u" ".join(s.split()) for s in allSols[4]]
            englishAbbreviations[cell] = [u" ".join(s.split()) for s in allSols[5]]

    allDicts = [englishFrench, englishGerman, englishItalian, englishSpanish, englishAbbreviations]
    for dict in allDicts:
        del dict[u'']
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    print "englishFrench = ", 
    pprint.pprint(englishFrench)
    print "\nenglishGerman = ", 
    pprint.pprint(englishGerman)
    print "\nenglishItalian = ", 
    pprint.pprint(englishItalian)
    print "\nenglishSpanish = ", 
    pprint.pprint(englishSpanish)
    print "\nenglishAbbreviations = ", 
    pprint.pprint(englishAbbreviations)

#-------------------------------------------------------------------------------

def dolmetsch():
    """
    http://www.dolmetsch.com/musictheory29.htm#translatednames
    """
    f = open('websites/dolmetsch.html')
    html = etree.HTML(f.read())
    
    englishFrench = {}
    englishGerman = {}
    englishItalian = {}
    englishSpanish = {}
    
    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        for col in allCols:
            items = [td.text.lower() for td in col.iter("td") if td.text is not None]
            items.extend([br.tail.lower() for br in col.iter("br") if br.tail is not None])
            allSols.append([unicode(s.encode("latin_1")) for s in items])
        for cell in allSols[0]:
            cell = u" ".join(cell.split("(")[0].split())
            englishItalian[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[1]]
            englishGerman[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[2]]
            englishFrench[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[3]]
            englishSpanish[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[4]]

    allDicts = [englishFrench, englishGerman, englishItalian, englishSpanish]
    for dict in allDicts:
        try:
            del dict[u'']
        except KeyError:
            pass
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    merge(lookup.englishFrench, englishFrench)
    merge(lookup.englishGerman, englishGerman)
    merge(lookup.englishItalian, englishItalian)
    merge(lookup.englishSpanish, englishSpanish)
    
    print "englishFrench = ", 
    pprint.pprint(englishFrench)
    print "\nenglishGerman = ", 
    pprint.pprint(englishGerman)
    print "\nenglishItalian = ", 
    pprint.pprint(englishItalian)
    print "\nenglishSpanish = ", 
    pprint.pprint(englishSpanish)

#-------------------------------------------------------------------------------

def dolmetsch2():
    """
    http://www.dolmetsch.com/musictheory29.htm#instrumentabbrev
    """
    f = open('websites/dolmetsch2.html')
    html = etree.HTML(f.read())
    
    englishAbbreviations = {}
    
    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        for col in allCols:
            items = [td.text.lower() for td in col.iter("td") if td.text is not None]
            allSols.append([unicode(s.encode("latin_1")) for s in items])
        for cell in allSols[0]:
            cell = u" ".join(cell.split("(")[0].split())
            items = []
            for a in allSols[1]:
                items.extend([x.strip() for x in a.split("(")[0].split(",")])
            englishAbbreviations[cell] = items
    
    allDicts = [englishAbbreviations]
    for dict in allDicts:
        try:
            del dict[u'']
        except KeyError:
            pass
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
            while(True):
                try:
                    dict[key].remove(u'-')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    merge(lookup.englishAbbreviations, englishAbbreviations)
    print "englishAbbreviations = ", 
    pprint.pprint(englishAbbreviations)

#-------------------------------------------------------------------------------

def yale():
    """
    http://www.library.yale.edu/cataloging/music/instname.htm#wind
    """
    f = open('websites/yale.html')
    html = etree.HTML(f.read())
    
    englishFrench = {}
    englishGerman = {}
    englishItalian = {}
    englishSpanish = {}
    englishRussian = {}
    
    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        for col in allCols:
            items = []
            for f in col.iter("font"):
                if f.text is not None:
                    items.extend(re.split("[,;/]",f.text.lower()))
            for br in col.iter("br"):
                if br.tail is not None:
                    items.extend(re.split("[,;/]",br.tail.lower()))
            allSols.append(items)
        for cell in allSols[0]:
            cell = u" ".join(cell.split("(")[0].split())
            englishFrench[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[1]]
            englishGerman[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[2]]
            englishItalian[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[3]]
            englishRussian[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[4]]
            englishSpanish[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[5]]

    allDicts = [englishFrench, englishGerman, englishItalian, englishSpanish, englishRussian]
    for dict in allDicts:
        try:
            del dict[u'']
        except KeyError:
            pass
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    merge(lookup.englishFrench, englishFrench)
    merge(lookup.englishGerman, englishGerman)
    merge(lookup.englishItalian, englishItalian)
    merge(lookup.englishSpanish, englishSpanish)
    merge(lookup.englishRussian, englishRussian)
    
    print "englishFrench = ", 
    pprint.pprint(englishFrench)
    print "\nenglishGerman = ", 
    pprint.pprint(englishGerman)
    print "\nenglishItalian = ", 
    pprint.pprint(englishItalian)
    print "\nenglishSpanish = ", 
    pprint.pprint(englishSpanish)
    print "\nenglishRussian = ", 
    pprint.pprint(englishRussian)

#-------------------------------------------------------------------------------

def ukItalian():
    """
    http://www.musictheory.org.uk/res-musical-terms/italian-musical-terms.php
    """
    f = open('websites/ukItalian.html')
    html = etree.HTML(f.read())
    
    englishItalian = {}
    englishAbbreviations = {}

    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        if len(allCols) == 0:
            continue
        for td in allCols[3].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower())
                allSols.append([unicode(s.encode("latin_1")) for s in items])
        for td in allCols[2].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower()[1:-1])
                allSols.append([unicode(s.encode("latin_1")) for s in items])
        for td in allCols[0].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower())
                allSols.append([unicode(s.encode("latin_1")) for s in items])

        for cell in allSols[0]:
            cell = u" ".join(cell.split("(")[0].split())
            englishAbbreviations[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[1]]
            englishItalian[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[2]]

    allDicts = [englishItalian, englishAbbreviations]
    for dict in allDicts:
        try:
            del dict[u'']
        except KeyError:
            pass
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    merge(lookup.englishItalian, englishItalian)
    merge(lookup.englishAbbreviations, englishAbbreviations)

    print "englishItalian = ", 
    pprint.pprint(englishItalian)
    print "\nenglishAbbreviations = ", 
    pprint.pprint(englishAbbreviations)

#-------------------------------------------------------------------------------

def ukGerman():
    """
    http://www.musictheory.org.uk/res-musical-terms/german-musical-terms.php
    """
    f = open('websites/ukGerman.html')
    html = etree.HTML(f.read())
    
    englishGerman = {}
    englishAbbreviations = {}

    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        if len(allCols) == 0:
            continue
        for td in allCols[3].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower())
                allSols.append([unicode(s.encode("latin_1")) for s in items])
        for td in allCols[2].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower()[1:-1])
                allSols.append([unicode(s.encode("latin_1")) for s in items])
        for td in allCols[0].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower())
                allSols.append([unicode(s.encode("latin_1")) for s in items])

        for cell in allSols[0]:
            cell = u" ".join(cell.split("(")[0].split())
            englishAbbreviations[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[1]]
            englishGerman[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[2]]

    allDicts = [englishGerman, englishAbbreviations]
    for dict in allDicts:
        try:
            del dict[u'']
        except KeyError:
            pass
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    merge(lookup.englishGerman, englishGerman)
    merge(lookup.englishAbbreviations, englishAbbreviations)

    print "englishGerman = ", 
    pprint.pprint(englishGerman)
    print "\nenglishAbbreviations = ", 
    pprint.pprint(englishAbbreviations)

#-------------------------------------------------------------------------------

def ukFrench():
    """
    http://www.musictheory.org.uk/res-musical-terms/french-musical-terms.php
    """
    f = open('websites/ukFrench.html')
    html = etree.HTML(f.read())
    
    englishFrench = {}
    englishAbbreviations = {}

    table = html.iter("tr")
    for row in table:
        allCols = list(row.iter("td"))
        allSols = []
        if len(allCols) == 0:
            continue
        for td in allCols[3].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower())
                allSols.append([unicode(s.encode("latin_1")) for s in items])
        for td in allCols[2].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower()[1:-1])
                allSols.append([unicode(s.encode("latin_1")) for s in items])
        for td in allCols[0].iter("td"):
            if td.text is not None:
                items = re.split("/;", td.text.lower())
                allSols.append([unicode(s.encode("latin_1")) for s in items])

        for cell in allSols[0]:
            cell = u" ".join(cell.split("(")[0].split())
            englishAbbreviations[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[1]]
            englishFrench[cell] = [u" ".join(s.split("(")[0].split()) for s in allSols[2]]

    allDicts = [englishFrench, englishAbbreviations]
    for dict in allDicts:
        try:
            del dict[u'']
        except KeyError:
            pass
        for key in dict:
            while(True):
                try:
                    dict[key].remove(u'')
                except ValueError:
                    break
        for key in dict.keys():
            if len(dict[key]) == 0:
                del dict[key]

    merge(lookup.englishFrench, englishFrench)

    print "englishFrench = ", 
    pprint.pprint(englishFrench)

#-------------------------------------------------------------------------------

def merge(source, target):
    """
    Merge source dictionary with target dictionary.
    """
    for srcKey in source.keys():
        if not target.has_key(srcKey):
            target[srcKey] = source[srcKey]
        else:
            for item in source[srcKey]:
                if not item in target[srcKey]:
                    target[srcKey].append(item)

#-------------------------------------------------------------------------------

def allToEnglish():
    allDicts = [lookup.englishFrench,lookup.englishGerman,lookup.englishAbbreviations,
                lookup.englishItalian,lookup.englishSpanish, lookup.englishRussian]
    masterDict = {}
    pass

if __name__ == "__main__":
    #allToEnglish()
    #print lookup.englishFrench["a double sharp"]

#------------------------------------------------------------------------------
# eof