n = int(input())
xy_list = [input() for _ in range(n)]

group_dict = {}
for i in range(n):
    x, y = map(int, xy_list[i].split())
    is_contain = False
    if i == 0:
        group_dict.update({0:[[x,y]]})
    else:
        for key in group_dict.keys():
            for item in group_dict[key]:
                if (x,y) in ((item[0]-1,item[1]-1), (item[0]-1,item[1]), (item[0],item[1]-1),(item[0],item[1]+1),  (item[0]+1,item[1]),(item[0]+1,item[1]+1)):
                    group_dict[key].append([x,y])
                    is_contain = True
                    break
        if not is_contain:
            max_key = max(group_dict.keys())
            group_dict.update({max_key+1:[[x,y]]})

# 同じ要素を持つgroupを結合
key_list = list(group_dict.keys())
del_key_list = []
for i, key in enumerate(key_list):
    if key in del_key_list:
        continue
    element_list = group_dict[key]
    for el in element_list:
        for key2 in key_list[i+1:]:
            if key2 == key:
                continue
            if key2 in del_key_list:
                continue
            if el in group_dict[key2]:
                group_dict[key] += group_dict[key2]
                del group_dict[key2]
                del_key_list.append(key2)

print(len(group_dict))
            