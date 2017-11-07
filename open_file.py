#!/usr/bin/python3

# 打开一个文件
f = open("/home/Documents/python/hello.py", "r")

str = f.read()
print(str)

# 关闭打开的文件
f.close()
