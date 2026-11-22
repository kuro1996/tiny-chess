import json,os,urllib.request as u
def P(p,b):
 with u.urlopen(os.environ["MAKEFUN_ENV_URL"]+p,json.dumps(b).encode())as x:return json.load(x)
L=[0,100,320,330,500,900,0]
Q="kkkkuuuummoqllmpkkkoljiklmmgkkkkaceecgkkekmnelnoeknoelmncgklaceegiiiikkkiklmillmikmmimmmilkkgiiikkkklmmmjkkkjkkkjkkkjkkkjkkkkkklgiijikkkiklljkllkkllillliklkgiijeccaeccaeccaeccageecigggookkoqmk"
T=[[L[a+1]+(ord(Q[a*32+(7-(s>>4))*4+min(s&7,7-(s&7))])-107)*5 for s in range(128)]for a in range(6)]
RO=[-16,-1,1,16];BI=[-17,-15,15,17];QU=RO+BI
JO=(-15,-17,-33,-31,-18,-14,14,18,31,33,-17,-16,-15,-1,1,15,16,17);NO=JO[2:10];KI=JO[10:]
B=[0]*128;S=0;C=0;KP=[0,0];ND=0;BU=60000;TT={};M=10**5;CZ={0:2,7:1,112:8,119:4}
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
 m=[];g=(1,-1)[S]
 for i,p in enumerate(B):
  if p*g<=0:continue
  a=abs(p)
  if a==1:
   d=16*g
   for dd in(0,-1,1):
    t=i+d+dd
    if t&136:continue
    if(dd and B[t]*g>=0)or(not dd and(c or B[t])):continue
    if t>>4==7-S*7:m+=[i|t<<7|q<<14 for q in(5,4,3,2)]
    else:
     m.append(i|t<<7)
     if not dd and i>>4==1+S*5 and not B[i+2*d]:m.append(i|(i+2*d)<<7)
  else:
   for d in NO if a==2 else KI if a==6 else BI if a==3 else RO if a==4 else QU:
    t=i+d
    while not t&136:
     if B[t]:
      if B[t]*g<0:m.append(i|t<<7)
      break
     if not c:m.append(i|t<<7)
     if a in(2,6):break
     t+=d
 if not c:
  k=KP[S]
  for b,ks,k2 in((1,6,1),(2,2,0))if S==0 else((4,118,1),(8,114,0)):
   es=(ks-1,ks)if k2 else(ks-1,ks,ks+1);ts=ks-1 if k2 else ks+1
   if C&b and not any(B[e]for e in es)and not(A(k,1-S)or A(ts,1-S)or A(ks,1-S)):m.append(k|ks<<7)
 return m
def D(m):
 global C;g=(1,-1)[S];f=m&127;t=m>>7&127;pr=m>>14;pc=B[f];cp=B[t];un=(cp,C)
 B[t]=pc if not pr else pr*g;B[f]=0
 if abs(pc)==6:
  KP[S]=t;C&=~(3<<S*2)
  if abs(t-f)==2:
   j=1 if t>f else -2;k=-1 if t>f else 1;B[t+k],B[t+j]=B[t+j],0
 C&=~(CZ.get(f,0)|CZ.get(t,0))
 return un,cp,0
def N(m,un,cp,ep):
 global C;g=(1,-1)[S];f=m&127;t=m>>7&127;pr=m>>14;pc=B[t]
 B[f]=pc if not pr else g;B[t]=cp
 if abs(pc)==6:
  KP[S]=f
  if abs(t-f)==2:
   j=1 if t>f else -2;k=-1 if t>f else 1;B[t+j],B[t+k]=B[t+k],0
 C=un[1]
def V():
 s=0
 for i,p in enumerate(B):
  if p:s+=T[abs(p)-1][i]if p>0 else -T[-p-1][i^112]
 return s*(1,-1)[S]
def R(d,a,b,pl):
 global S,ND;ND+=1
 if ND>BU:return None
 e=0
 if d>0:
  k=(bytes([p+6 for p in B]),S,C);e=TT.get(k,0)
  ms=G()
 else:
  if d<-1:return V()
  a=max(a,V())
  if a>=b:return b
  ms=G(1)
 ms.sort(key=lambda m:(m!=e,-abs(B[m>>7&127])))
 bs=None
 for m in ms:
  un,cp,ep=D(m);S^=1
  if A(KP[S^1],S):S^=1;N(m,un,cp,ep);continue
  bs=m
  x=R(d-1,-b,-a,pl+1)
  S^=1;N(m,un,cp,ep)
  if x is None:return None
  if -x>a:a=-x
  if a>=b:break
 if d>0:
  if bs is None:return -M+pl if A(KP[S],1-S) else 0
  TT[k]=bs;return a
 return a
def Y(f):
 global S,C,KP;ps=f.split();B[:]=[0]*128;r=7;c=0
 for ch in ps[0]:
  if ch=='/':r-=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:
   k="PNBRQKpnbrqk".index(ch);B[r*16+c]=(k+1,5-k)[k>5];c+=1
 S=ps[1]!='w';C=0
 for ch in ps[2]:C|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 KP=[B.index(6),B.index(-6)]
s=lambda q:chr(q%8+97)+str(q//16+1)
def W(m):return s(m&127)+s(m>>7&127)+("nbrq"[(m>>14)-2] if m>>14 else "")
def H(fen,legal):
 global S,ND;Y(fen)
 lg=[]
 for m in G():
  un,cp,ep=D(m);S^=1;ok=not A(KP[S^1],S);S^=1;N(m,un,cp,ep)
  if ok:lg.append([m,0])
 bm=lg[0][0];ND=0
 for d in range(9):
  lg.sort(key=lambda e:-e[1]);ok=1;ba=-M
  for e in lg:
   m=e[0];un,cp,ep=D(m);S^=1;x=R(d,-M,M,1);S^=1;N(m,un,cp,ep)
   if x is None:ok=0;break
   e[1]=-x
   if -x>ba:ba=-x;bm=m
  if not ok:break
 u=W(bm)
 return u if u in legal else legal[0]
while(g:=P("/game",{}))["status"]!="done":
 TT.clear()
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":H(g["fen"],g["legal_moves"])})
