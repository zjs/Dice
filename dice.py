from Dice import *
import cgi
import random
import re

def _string_to_sets(input):
    setStrings = []
    # TODO: Find a cleaner way to do this
    for s in [r.split('-') for r in input.split('+')]:
        setStrings.extend(s)

    diceSets = []
    for setString in setStrings:
        parsed = re.search('^([0-9]+)(d([0-9]+))?(k([0-9]+))?(x([0-9]+))?$', setString)

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

            for i in range(0,n):
                diceSets.append(DiceSet(r,d,k))

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

def main(req):
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

    return '<html><body><div>%s</div><div style="font-weight:bold">%s</div><div><form method="post"><input type="text" name="input" value="%s" /><input type="submit" value="Roll"></body></html>' % (output, total, input)
