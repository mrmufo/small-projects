import json
from pprint import pprint


with open('nested.json') as f:
    data = json.load(f)


def unpack_dict(data_obj):
    global s
    for key, value in data_obj.items():
        if type(value) is dict:
            s += key + '.'
            unpack_dict(data_obj[key])
        else:
            if s.endswith('.'):
                s += key
            else:
                s += "." + key
            dik[s] = value
            s = s.rsplit('.', 1)[0] + '.'


dik = {}
s = ""
unpack_dict(data)
for k, v in dik.items():
    print("{0}: {1},".format(k, v))

pprint(dik)

# def unpack_dict(data_obj):
#     output = {}
#
#     def unpack(x, name=''):
#         if type(x) is dict:
#             for each in x:
#                 unpack(x[each], name + each + '_')
#         elif type(x) is list:
#             i = 0
#             for each in x:
#                 unpack(each, name + str(i) + '_')
#         else:
#             output[name[:-1]] = x
#
#     unpack(data_obj)
#     return output


# pprint(data)

