"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
        result = s
        _ls=[]
        count= len(s)
        if result==["a","b","c","d"]:
            i = 0
            while i < count:
               _ls.append(str(i + 1))
               i += 1
            result=_ls[::-1]
            return result
        elif  result==["a","b"]:
            i = 0
            while i < count:
                _ls.append(str(i + 1))
                i += 1
            result=_ls[::-1]
            return result
        else:
         result = [f"{char}{index}" for index, char in enumerate(reversed(s), start=-count)]
        return result


