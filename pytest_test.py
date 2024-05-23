import itertools

sz ='test_raid_create_paramet.py::Test_create_all_raids::test_create_various_raids[Raid0]'
sep = '::'
sz =  sz.split(sep)[1:]
print(sz)

sz = [[each, each.split('[')[0]]   if '[' in each else [each] for each in sz]

print(sz)

sz =list(itertools.chain(*sz))
sz = set(sz)
print(sz)