x=1000
graph =[[x,3,8,5,5,x,x],
        [x,x,2,x,x,5,x], 
        [x,x,x,3,6,x,7], 
        [x,x,x,x,3,x,2], 
        [x,x,x,x,x,1,x],
        [x,x,x,x,x,x,2],
        [x,x,x,x,x,x,x]]
V = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']
S=set()
NS=set()
d0={}
pre={}
S.add(V[0])
for i in range(len(graph[0])):
  if(graph[0][i]!=x):
    NS.add(V[i])
    d0[V[i]]=graph[0][i]
    pre[V[i]]=V[0]
  else:
    d0[V[i]]=x
d0[V[0]]=0

print("")
print("S:",S)
print("NS",NS)
print("d0:", d0)
print("pre:", pre)

while len(S) < len(V):
  min_d=x
  min_v=V[0]
  for v, d in d0.items():
    if v in NS and d < min_d:
        min_d = d
        min_v= v
  S.add(min_v)
  NS.remove(min_v)
  m = V.index(min_v)
  for i in range(len(graph[m])):
    if(graph[m][i]!=x):
      NS.add(V[i])
      if(graph[m][i]+d0[V[m]]<d0[V[i]]):
        d0[V[i]]=graph[m][i]+d0[V[m]]
        pre[V[i]]=V[m]
        
  print("")
  print("S:",S)
  print("NS",NS)
  print("d0:", d0)
  print("pre:", pre)

print("minimum cost=" ,d0[V[6]])
print("minimum path")
v=V[6]
print(v)
while(pre[v]!=V[0]):
  print(pre[v])
  v=pre[v]
print(V[0])



