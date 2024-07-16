"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    mapeo = {
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6"
    }

    _ls = []
    for dic in result:
        nuevo_dic = {}
        for clave, valor in dic.items():
            nueva_clave = mapeo[clave]
            nuevo_valor = mapeo[valor]
            nuevo_dic[nueva_clave] = nuevo_valor
        _ls.append(nuevo_dic)

    result = _ls
    return result
