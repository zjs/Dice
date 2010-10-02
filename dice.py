from Dice import *
import cgi
import random
import re

def _parse_string(string):
    parsed = re.search('^([0-9]+)(d([0-9]+))?(k([0-9]+))?(x([0-9]+))?$', string)

    if parsed == None:
        raise ValueError
    else:
        pieces = parsed.groups()
        r = pieces[0]
        d = pieces[2]
        k = pieces[4]
        n = pieces[6]

        if r == None:
            r = 1
        else:
            r = int(r)

        if d == None:
            d = 1
        else:
            d = int(d)

        if k == None:
            k = r
        else:
            k = int(k)

        if n == None:
            n = 1
        else:
            n = int(n)

    return {'count':r,'sides':d,'keep':k,'number':n}

def _string_to_strings(input):
    return input.split('+')

def _string_to_sets(input):
    setStrings = _string_to_strings(input)

    diceSets = []
    for setString in setStrings:
        pieces = _parse_string(setString)

        for i in range(0,pieces['number']):
            diceSets.append(DiceSet(pieces['count'],pieces['sides'],pieces['keep']))

    return diceSets

def _result_to_string(result):
    r = result.getResults()

    output = []
    for (die, kept) in r:
        if kept:
            s = "%s*" % die
        else:
            s = "%s" % die

        output.append(s)

    return '<br />'.join(output) + "<br />=>%s<br />" % result.getValue()

def roll(req):
    input = ""
    output = ""
    total = ""
    form = req.form

    if form.has_key('input'):
        input = form['input'].value
        
        diceSets = _string_to_sets(input)

        results = [s.roll() for s in diceSets]

        output = ''.join([_result_to_string(result) for result in results])

        total = sum([result.getValue() for result in results])

    return '<html><body><div id="output"><div id="details">%s</div><div id="result">%s</div></div><div><form method="post"><input type="text" name="input" value="%s" /><input type="submit" value="Roll"></body></html>' % (output, total, input)
