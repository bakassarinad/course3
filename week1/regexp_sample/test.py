import re


def calculate(data, findall):
    matches = findall(r"([abc])([+-]?=)([abc])?([+-]?\d+)?")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if n == "":
            n = 0
        if s == "=" and v2 == "":
            data[v1] = int(n)
        elif s == "=" and v2 != "":
            data[v1] = data[v2] + int(n)
        elif s == "-=" and v2 != "":
            data[v1] -= data[v2] + int(n)
        elif s == "-=" and v2 == "":
            data[v1] -= int(n)
        elif s == "+=" and v2 != "":
            data[v1] += data[v2] + int(n)
        elif s == "+=" and v2 == "":
            data[v1] += int(n)
            
    return data

def findall(regexp):
    text = """
    a=1
    a=+1
    a=-1
    a=b
    a=b+100
    a=b-100
    
    b+=10
    b+=+10
    b+=-10
    b+=b
    b+=b+100
    b+=b-100
    
    c-=101
    c-=+101
    c-=-101
    c-=b
    c-=b+101
    c-=b-101
    """

    return re.findall(regexp, text)


result = calculate({'a': 1, 'b': 2, 'c': 3}, findall)
correct = {"a": -98, "b": 196, "c": -686}
if result == correct:
    print ("Correct")
else:
    print ("Incorrect: %s != %s" % (result, correct))
