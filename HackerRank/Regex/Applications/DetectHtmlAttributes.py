import re

tag_regex = r'(<(\w+)(?: .*?)?>)'
attr_regex = r' (\w+)='

tags = []
tags_to_attr = {}

n = int(input())
for i in range(0,n):
    s = input()
    tag_matches = re.findall(tag_regex,s)
    if len(tag_matches)>0:
        for tag in tag_matches:
            if tag[1] not in tags:
                tags.append(tag[1])
                tags_to_attr[tag[1]] = []
            attr_matches = re.findall(attr_regex,tag[0])
            if len(attr_matches) > 0:
                for attr in attr_matches:
                    if attr not in tags_to_attr[tag[1]]:
                        tags_to_attr[tag[1]].append(attr)
tags.sort()
for tag in tags:
    res = tag + ':'
    attrs = tags_to_attr[tag]
    attrs.sort()
    attr_string = ''
    for attr in attrs:
        attr_string+=attr + ','
    if len(attr_string)>0:
        attr_string = attr_string[:len(attr_string)-1]
    print(res+attr_string)
