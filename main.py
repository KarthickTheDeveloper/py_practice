def my_fn(s="aaaabbbccz"):
    s_lst = [x for x in s]
    # print(s_lst)
    nw_lst = []
    for x in s_lst:
        if x not in nw_lst:
            nw_lst.append(x)
    for y in s:
        ct = str(s.count(y))
        if ct in nw_lst:
            pass
        else:
            nw_lst.append(ct)
    print(nw_lst)
    # final = ''.join(nw_lst)
    # print(final)


my_fn()


# def my_fn(s="aaaabbbccz"):
#     s_lst = [x for x in s]
#     print(s_lst)
#
#     i = 0
#     nw_lst = []
#     while i <= len(s_lst):
#         if s_lst[i] not in nw_lst:
#             nw_lst.append(s_lst[i])
#         # else:
#         #     y = str(s.count(s_lst[i]))
#         #     nw_lst.append(y)
#         #     i += 1
#     print(nw_lst)
#     # final = ''.join(nw_lst)
#     # print(final)
#
#
# my_fn()

#
# i1 = 'python'
# i2 = 'jawa'
# i1_lst = [x for x in i1]
# i2_lst = [x for x in i2]
# print(i1_lst)
# print(i2_lst)



