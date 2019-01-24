
file = open("/home/mufo/PycharmProjects/helloworld2/input.txt", 'r')
dik = {}


def dupa(inkey, a, b):
    result = None

    if '+' in value:
        print(inkey + " = " + str(a) + " + " + str(b))
        result = (a + b)
    if '-' in value:
        print(inkey + " = " + str(a) + " - " + str(b))
        result = (a - b)
    if '*' in value:
        print(inkey + " = " + str(a) + " * " + str(b))
        result = (a * b)
    if '/' in value:
        print(inkey + " = " + str(a) + " / " + str(b))
        result = (a / b)

    if result:
        print('key: ' + inkey + ' is ' + str(result))
        dik[inkey] = result


# Reads and saves input in a dictionary dik = {variable: value}
for line in file:   # Reads line
    els = line.strip()  # Removes new line character \n
    els = els.split(' ')  # Splits string at whitespace character, creates array of substrings
    dik.update({  # Saves substrings in dictionary
        els[0]: els[2:]
    })


for key, value in dik.items():  # Search dictionary dik by key, value
    value_a = dik.get(value[0])  # Assuming value[0] contains variable(key),
    # then search dik keys if one is present. If so, save its value. If no, returns None.
    value_b = dik.get(value[2])
    if not value_a and not value_b: #
        dupa(key, int(value[0]), int(value[2]))
    elif value_a and not value_b:
        dupa(key, int(dik.get(value[0])), int(value[2]))
    elif not value_a and value_b:
        dupa(key, int(value[0]), dik.get(value[2]))
    elif value_a and value_b:
        dupa(key, int(dik.get(value[0])), int(dik.get(value[2])))

print(dik['answer'])
print(dik)
