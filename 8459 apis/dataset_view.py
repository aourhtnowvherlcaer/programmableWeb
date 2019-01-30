import codecs
import json

with codecs.open('api_info.json', 'r', encoding='utf-8') as reader:
    apis = json.loads(reader.readline())


counter = [0 for _ in range(20)]
length = 0
for api in apis:
    counter[api['api_prim_cate']] += 1
    length += len(api['api_desc'].split())
print(counter)
print(sum(counter))
print(length / sum(counter))