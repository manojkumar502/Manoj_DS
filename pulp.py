import pandas as pd
import pulp
import re
import sys
sys.setrecursionlimit(10000)
data = [['A', 'blue', 'circle', 0.454], 
    ['B', 'yellow', 'square', 0.570],
    ['C', 'red', 'triangle', 0.789],
    ['D', 'red', 'circle', 0.718],
    ['E', 'red', 'square', 0.828],
    ['F', 'orange', 'square', 0.709],
    ['G', 'blue', 'circle', 0.696],
    ['H', 'orange', 'square', 0.285],
    ['I', 'orange', 'square', 0.698],
    ['J', 'orange', 'triangle', 0.861],
    ['K', 'blue', 'triangle', 0.658],
    ['L', 'yellow', 'circle', 0.819],
    ['M', 'blue', 'square', 0.352],
    ['N', 'orange', 'circle', 0.883],
    ['O', 'yellow', 'triangle', 0.755]]

df = pd.DataFrame(data, columns = ['item', 'color', 'shape', 'value'])
BlueMatch = lambda x: 1 if x=='blue' else 0
YellowMatch = lambda x: 1 if x=='yellow' else 0
RedMatch = lambda x: 1 if x=='red' else 0
OrangeMatch = lambda x: 1 if x=='orange' else 0
df['color'] = df['color'].astype(str)

df['isBlue'] = df.color.apply(BlueMatch)
df['isYellow'] = df.color.apply(YellowMatch)
df['isRed'] = df.color.apply(RedMatch)
df['isOrange'] = df.color.apply(OrangeMatch)

prob  = pulp.LpProblem("complex_napsack", pulp.LpMaximize)
x = pulp.LpVariable.dicts( "x", indexs = df.index, lowBound=0, cat='Integer')


prob += pulp.lpSum([x[i]*df.value[i] for i in df.index ])


prob += pulp.lpSum([x[i]*df.isBlue[i] for i in df.index])==2
prob += pulp.lpSum([x[i]*df.isYellow[i] for i in df.index])==2
prob += pulp.lpSum([x[i] for i in df.index ])==10

prob.solve()

        
for v in prob.variables():
    if v.varValue != 0.0:
        mystring = re.search('([0-9]*$)', v.name)
        print(v.name, "=", v.varValue)
        ind = int(mystring.group(1))
        print(df.item[ind])
		
output:
x_11 = 2.0
L
x_13 = 6.0
N
x_6 = 2.0
G