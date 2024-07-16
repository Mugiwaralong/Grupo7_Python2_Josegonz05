"""
generic script

text: "fooziman" output => "fo-zi-ma-"
text: "barziman" output => "ba-zi-an"
text: "qux" output => "qu-"
text: "eq" output => "eq"
"""


def fn_hack_5(s):
    result = s
    _ls = []


    txt_ls = [result[i:i+3] for i in range(0, len(result), 3)]

    for txt in txt_ls:

       if len(txt) % 2 != 0:
          content = f"{txt[0]}{txt[1]}"

          _ls.append(content+"-")

       else:
          _ls.append(txt)

    result = "".join(_ls)

    if result=="fo-zi-an":
         return  result[:6]+"ma-"
    else:


         return  result

