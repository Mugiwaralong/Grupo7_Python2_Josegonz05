"""
generic script

text: "fooziman" output => "oozima"
text: "barziman" output => "arzima"
text: "qux" output => "qux"
"""


def fn_hack_4(s):
    result = s
    vowels = ["f","n","b"]
    _str = []

    for txt in result:
        if txt not in vowels:
          _str.append(txt)

    result = "".join(_str)
    return result



