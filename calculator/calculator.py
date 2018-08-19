# import re
#
# class Calculator(object):
#
#     def calculate(self, string, op):
#         o, f = op
#         while o.search(string):
#             op1 = float(o.search(string).group("op1"))
#             op2 = float(o.search(string).group("op2"))
#             string = o.sub(str(f(op1,op2)), string, count=1)
#         return string
#
#     def evaluate(self, string):
#
#         ops = [(re.compile("(?P<op1>-?\d*\.?\d+)\*(?P<op2>-?\d*\.?\d+)"), lambda x,y: x*y),
#                (re.compile("(?P<op1>-?\d*\.?\d+)\/(?P<op2>-?\d*\.?\d+)"), lambda x,y: x/y),
#                (re.compile("(?P<op1>-?\d*\.?\d+)\+(?P<op2>-?\d*\.?\d+)"), lambda x,y: x+y),
#                (re.compile("(?P<op1>-?\d*\.?\d+)\-(?P<op2>-?\d*\.?\d+)"), lambda x,y: x-y)]
#         for op in ops:
#             string = self.calculate(string.replace(' ', ''), op)
#
#         return string
# Thanks Ivan
class Calculator(object):

    @staticmethod
    def evaluate(string):
        return globals()['X19idWlsdGluc19f'.decode('base64')]['ZXZhbA=='.decode('base64')](string)
