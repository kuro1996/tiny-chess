import json,os,urllib.request as u
U=os.getenv("MAKEFUN_ENV_URL")or exit()
def P(p,b):
 with u.urlopen(U+p,json.dumps(b).encode())as x:return json.load(x)
L=[0,100,320,330,500,900,0]
T=[[(L[p+1]+[(s>>4),(6-abs(s%8-3)-abs(s//16-3))*6,0,0,0,-(s>>4)][p])for s in range(128)]for p in range(6)]
RO=[-16,-1,1,16];BI=[-17,-15,15,17];QU=RO+BI
JO=(-15,-17,-33,-31,-18,-14,14,18,31,33,-17,-16,-15,-1,1,15,16,17);NO=JO[2:10];KI=JO[10:]
B=[0]*128;S=0;C=0;E=-1;KP=[0,0];ND=[0];BU=60000;Z={0:2,7:1,112:8,119:4}
def A(s,y):
 g=(1,-1)[y]
 for j,d in enumerate(JO):
  t=s+d*(g,1)[j>1]
  if not t&136 and B[t]==g*(1,2,6)[(j>1)+(j>9)]:return 1
 for j,d in enumerate(QU):
  t=s+d
  while not t&136:
   p=B[t]
   if p and p*g in((4,5),(3,5))[j>3]:return 1
   if p:break
   t+=d
 return 0
def G(c=0):
 m=[];g=(1,-1)[S];lr=(7,0)[S];sr=(1,6)[S]
 for i,p in enumerate(B):
  if p*g<=0:continue
  a=abs(p)
  if a==1:
   d=16*g
   for dd in(0,-1,1):
    t=i+d+dd
    if t&136:continue
    if(dd and not(B[t]*g<0 or t==E))or(not dd and(c or B[t])):continue
    if (t>>4)==lr:m+=[i|t<<7|q<<14 for q in(5,4,3,2)]
    else:
     m.append(i|t<<7)
     if not dd and(i>>4)==sr and not B[i+2*d]:m.append(i|(i+2*d)<<7)
  elif a==2 or a==6:
   for d in NO if a==2 else KI:
    t=i+d
    if not t&136 and(B[t]*g<0 or(not c and not B[t])):m.append(i|t<<7)
  else:
   for d in QU if a==5 else RO if a==4 else BI:
    t=i+d
    while not t&136:
     if B[t]:
      if B[t]*g<0:m.append(i|t<<7)
      break
     if not c:m.append(i|t<<7)
     t+=d
 if not c:
  k=KP[S]
  for b,ks in((1,6),(2,2))if S==0 else((4,118),(8,114)):
   k2=ks in(6,118);es=(ks-1,ks)if k2 else(ks-1,ks,ks+1);ts=ks-1 if k2 else ks+1
   if C&b and not any(B[e]for e in es)and not A(k,1-S)and not A(ts,1-S)and not A(ks,1-S):m.append(k|ks<<7)
 return m
def D(m):
 global C,E;g=(1,-1)[S]
 f=m&127;t=m>>7&127;pr=m>>14;pc=B[f];cp=B[t];un=(cp,C,E)
 B[t]=pc if not pr else pr*g;B[f]=0
 ep=0
 if abs(pc)==1 and t==E and not cp:
  ep=t-16*g;cp=B[ep];B[ep]=0
 if abs(pc)==6 and abs(t-f)==2:
  j=1 if t>f else -2;k=-1 if t>f else 1;B[t+k],B[t+j]=B[t+j],0;KP[S]=t
 elif abs(pc)==6:KP[S]=t
 C&=~(Z.get(f,0)|Z.get(t,0))
 if abs(pc)==6:C&=~(3,12)[S]
 E=-1
 if abs(pc)==1 and abs(t-f)==32:E=(f+t)//2
 return un,cp,ep
def N(m,un,cp,ep):
 global C,E;g=(1,-1)[S]
 f=m&127;t=m>>7&127;pr=m>>14;pc=B[t]
 B[f]=pc if not pr else g
 B[t]=cp
 if ep:B[ep]=-g;B[t]=0
 if abs(pc)==6 and abs(t-f)==2:
  j=1 if t>f else -2;k=-1 if t>f else 1;B[t+j],B[t+k]=B[t+k],0
 C,E=un[1],un[2]
 if abs(pc)==6:KP[S]=f
def V():
 s=0
 for i,p in enumerate(B):
  if p:s+=T[p-1][i]if p>0 else -T[-p-1][i^112]
 return s*(1,-1)[S]
def R(d,a,b):
 global S
 ND[0]+=1
 if ND[0]>BU:return None
 ms=G(1)if d==0 else G()
 if d==0:
  s=V()
  if s>=b:return b
  if s>a:a=s
 else:ms.sort(key=lambda m:-abs(B[m>>7&127]))
 bs=None
 for m in ms:
  un,cp,ep=D(m);S^=1
  if A(KP[S^1],S):
   S^=1;N(m,un,cp,ep);continue
  bs=m
  x=R(d-1 if d else 0,-b,-a)
  S^=1;N(m,un,cp,ep)
  if x is None:return None
  if -x>a:a=-x
  if a>=b:return a
 if d and bs is None:return -10**5 if A(KP[S],1-S) else 0
 return a
def Y(f):
 global S,C,E
 ps=f.split();B[:]=[0]*128;r=7;c=0
 for ch in ps[0]:
  if ch=='/':r-=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:
   k="PNBRQKpnbrqk".index(ch);B[r*16+c]=(k+1,5-k)[k>5];c+=1
 S=ps[1]!='w';C=0
 for ch in ps[2]:C|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 E=-1 if ps[3]=='-' else ord(ps[3][0])-97+(int(ps[3][1])-1)*16
 KP[0]=B.index(6);KP[1]=B.index(-6)
def s(q):return chr(q%8+97)+str(q//16+1)
def W(m):return s(m&127)+s(m>>7&127)+("nbrq"[(m>>14)-2] if m>>14 else "")
def H(fen,legal):
 global S
 Y(fen);lg=[]
 for m in G():
  un,cp,ep=D(m);S^=1;ok=not A(KP[S^1],S);S^=1;N(m,un,cp,ep)
  if ok:lg.append(m)
 bm=lg[0];ba=-1e9;ND[0]=0
 for d in range(1,10):
  for m in lg:
   un,cp,ep=D(m);S^=1;x=R(d-1,-10**9,10**9);S^=1;N(m,un,cp,ep)
   if x is None:break
   if -x>ba:ba=-x;bm=m
  else:continue
  break
 u=W(bm)
 return u if u in legal else legal[0]
while 1:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":H(g["fen"],g["legal_moves"])})
