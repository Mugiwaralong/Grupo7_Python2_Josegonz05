"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"]
"""



def fn_hack_6(s):
    result = s
    _ls = []

    if not s:
        result=(['0'])
        return result

    for i in range(len(result)):
        if (i + 1) % 2 == 0:
            _ls.append('{}'.format('-'))
        else:
            _ls.append('{}'.format(i + 1))

            result=_ls
    return result




