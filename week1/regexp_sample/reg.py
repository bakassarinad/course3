import re
text = """
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
data = {"a":1, "b":2, "c": 3}
def calculate(data):
	matches = re.findall(r"([abc])([+-]?=)([abc])?([+-]?\d+)?",text)
	for v1, s, v2, n in matches:
		if n == "":
			n = 0
		if s =="="and v2 =="":
			data[v1] = int(n)
		elif s=="="and v2 !="":
			data[v1]=data[v2]+int(n)
			print("eee")
		elif s == "+="and v2 =="":
			data[v1]+=int(n)
		elif s =="+=" and v2 !="":
			data[v1] += data[v2] + int(n)
		elif s == "-="and v2 =="":
			data[v1]-=int(n)
		elif s =="-=" and v2 !="":
			data[v1] -= data[v2] + int(n)
calculate(data)
print(data)