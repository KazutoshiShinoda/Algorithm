# -*- coding :utf-8 -*-
s = input()
candidates = []
for i in set(s):
    candidates.append( max( list( map( len, s.split(i) ) ) ) )
print(min(candidates))
