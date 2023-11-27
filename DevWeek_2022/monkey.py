
for i in range(10000000000):
    string =  str(i)
    item = string.zfill(10)
    print(item)
    ok = 0
    for a in range(10):
        print(a)
        print(f' num {item[a]}')
        print(f' count {item.count(str(a))}')
        if not int(item[a]) == item.count(str(a)):
            continue
        else:
            ok += 1
    if ok == 10:
        print(item)    


6210001000