from randomapi import *
random_client = RandomJSONRPC('5a85f2c8-a622-4f9f-81b8-6c3ba23bcea8')
nums = random_client.generate_integers(n=1, min=1, max=1248)
num = str(nums)
linestr = num.translate(None, '[]')
lineint = int(linestr)
print(lineint)
file = open('file.txt')
content = file.readlines()
print(content[lineint])