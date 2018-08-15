from autoinit import *
import re
from itertools import groupby

lines = [(re.compile('^(?P<heading>[#]+)(?P<text>(.*))$'), lambda x: Heading(len(x.group("heading")),x.group("text").strip())),
         (re.compile('^---$'), lambda x: Separator()),
         (re.compile('^\s$'), lambda x: Empty()),
         (re.compile('^\*(?P<text>(.*))$'), lambda x: UnorderedElement(x.group("text").strip())),
         (re.compile('^\d\.(?P<text>(.*))$'), lambda x: OrderedElement(x.group("text").strip())),
         (re.compile('^(.+)$'), lambda x: Paragraph(x.group())),
         ]

transforms = [(re.compile('(\*\*)(?P<text>.*)(\*\*)'), r"<strong>\g<text></strong>"),
              (re.compile('(\_)(?P<text>.*)(\_)'), r"<em>\g<text></em>"),
              (re.compile('(\`)(?P<text>.*)(\`)'), r"<code>\g<text></code>")
              ]

class Heading(metaclass=AutoInit):
    def __init__(self, gravity, content): pass
    def __str__(self): return "<h{0}> {1} </h{0}>".format(self.gravity, self.content)
class Separator(metaclass=AutoInit):
    def __init__(self): pass
    def __str__(self): return "<hr />"
class Empty(metaclass=AutoInit):
    def __init__(self): pass
    def __str__(self): return ""
class UnorderedElement(metaclass=AutoInit):
    def __init__(self, content): pass
    def __str__(self): return "\t<li> {} </li>".format(self.content)
class OrderedElement(metaclass=AutoInit):
    def __init__(self, content): pass
    def __str__(self): return "\t<li> {} </li>".format(self.content)
class Paragraph(metaclass=AutoInit):
    def __init__(self, content): pass
    def __str__(self): return "<p> {} </p>".format(self.content)

def parser(fn):
    with open(fn, encoding='utf-8') as file:
        lines = file.readlines()
        return stringer(grouper([transformer(liner(x)) for x in lines]))

def liner(x):
    for r,l in lines:
        if re.search(r,x) is not None:
            return l(r.search(x))

def transformer(x):
    if x.__dict__.get("content", None) is not None:
        for r,n in transforms:
            x.content = r.sub(n, x.content)
    return x

def grouper(l):
    return groupby([(type(x).__name__, x) for x in l], lambda x: x[0])

def stringer(l): #TODO: refactor this
    total = []
    for (k, x) in l:
        if k == "UnorderedElement": total.append("<ul>")
        if k == "OrderedElement": total.append("<ol>")
        for (_, y) in x:
            total.append(y)
        if k == "UnorderedElement": total.append("</ul>")
        if k == "OrderedElement": total.append("</ol>")
    return total

def translate(fn):
    result = parser(fn)
    return "<html>\n" + "\n".join([str(x) for x in parser(fn)]) + "\n</html>"
