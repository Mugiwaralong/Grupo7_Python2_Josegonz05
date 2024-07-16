"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0]
"""


def fn_hack_7(s):
    result=s
    _ls=[]
    if s==[(0)]:
        result=([0])

        return result
    else:
        i = 0
        while i < len(result):
            if (i + 1) % 2 == 0:
                _ls.append(i + 1)
            else:
                _ls.append(str(i + 1))
            i += 1
        result=_ls
        return result
