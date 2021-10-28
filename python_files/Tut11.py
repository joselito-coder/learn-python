s = set()
# print(type(s))

# l = [1,2,3,4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))

#adding elements to set
s.add(1)
s.add(2)
# s1 = s.intersection({1,2,3})
s1 = {4,6}
print(s.isdisjoint(s1))

print(s,s1)

# print(len(s))
# print(max(s))
# print(min(s))