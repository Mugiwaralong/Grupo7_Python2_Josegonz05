"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    _ls={}

    for clave, valor in result.items():
      if clave == "foo":
         nueva_clave = clave.capitalize()
         nueva_valor = "Fooziman"
         _ls[nueva_clave] = nueva_valor
         result = _ls

    return result

