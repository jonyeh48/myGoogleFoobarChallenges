def solution(l):
    ord_list = []
    ver_list = l
    while ver_list != []:
        ver_intlist_min = [int(i) for i in ver_list[0].split(".")]
        if len(ver_intlist_min) < 3:
            for i in range(3-len(ver_intlist_min)):
                ver_intlist_min.append(-1)
        for ver_temp in ver_list:
            ver_listint_temp = [int(i) for i in ver_temp.split(".")]
            if len(ver_listint_temp) < 3:
                for i in range(3-len(ver_listint_temp)):
                    ver_listint_temp.append(-1)
            #find smallest version number
            for i in range(3):
                if ver_listint_temp[i] < ver_intlist_min[i]:
                    ver_intlist_min = ver_listint_temp
                    ver_min = ver_temp
                    break
                elif ver_listint_temp[i] > ver_intlist_min[i]:
                    break
            if ver_listint_temp == ver_intlist_min:
                ver_min = ver_temp
        ord_list.append(ver_min)
        ver_list.remove(ver_min)
    return ord_list
