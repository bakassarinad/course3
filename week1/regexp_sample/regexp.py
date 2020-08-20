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
