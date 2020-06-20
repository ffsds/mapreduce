import ast
import sys

energy_weight = 0.75	
location_weight = 0.25	

attrd = ['energy','location']

def normalize_min(x,y):
 if max(x) - min(x) != 0:
  m = (max(x) - y) / (max(x) - min(x))
 if max(x) - min(x) == 0:
  m = 1
 return m
	
def normalize_max(x,z):
 if max(x) - min(x) != 0:
  m = (z - min(x)) / (max(x) - min(x))
 if max(x) - min(x) == 0:
  m = 1
 return m

def cr(difference_attr, zeta, g):
 if max(difference_attr) != 0:
  h = min(difference_attr) + (zeta * (max(difference_attr))) / (g + (zeta * (max(difference_attr))))
  return h
 elif max(difference_attr) == 0:
  h = 1
  return h

rd_range = ast.literal_eval(sys.argv[1])
n = len(rd_range) + 1

l= [0] * n
q = [0] * n

for a in range(1, (int(n) + 1)):  
 if a in rd_range:
  num = a
  rd = "rd" + str(a) + ".txt"
  k = "rd" + str(a)
  a = open("./reduce/"+rd,"r")
  a = a.read()
  a = ast.literal_eval(a)
  l[num - 1] = a
  exec("%s = %s" % ("attr",[]))
  for i in a:	
   exec("%s = %s" % (i,[]))
   exec("%s = %s" % (k,[]))
   exec("%s = %s" % (k + "_normalized",[]))
   exec("%s = %s" % (k + "_normalized_cr",[]))
   exec("%s = %s" % (i + "_normalized",[]))
   exec("%s = %s" % (i + "_normalized_r",[0] * n))  

attr = attrd
attr.sort(key=len)
for z in range(1, (int(n) + 1)):         
 if z in rd_range:
  for ij in attrd:
   exec("rd" + str(z) + ".append(float(l[z-1][ij]))")	

for x in l:  
 if x != 0: 
  for b in x:
   if b == 'energy':
    energy.append(x[b])
   if b == 'location':
    location.append(x[b])   

for i in range(1,len(l)+1):	
 if i in rd_range:
  g = str(i)	
  exec("z = rd" + g)
  for k in z:
   if z.index(k) == 0:
    m = float((normalize_max(energy, k)))
    exec("rd" + g + "_normalized.append(m)")
    energy_normalized.append(m)
   if z.index(k) == 1:
    m = (normalize_min(location, k))
    m = float(m)
    exec("rd" + g + "_normalized.append(m)")
    location_normalized.append(m)   

zeta = 0.5

for attr in attrd:		
 exec("ds_" + attr + "= max(" + attr + "_normalized)")
 exec("p = "+attr+"_normalized")
 exec("%s = %s" % ("difference_"+attr,[]))
 for ij_normalized in p:
  exec("f = ds_" + attr + " - ij_normalized")
  exec("difference_"+attr+".append(f)")
 exec("h = difference_"+attr)
 c = 1
 d = 0
 for n in range(1, len(l) + 1):
  if n in rd_range:      
   exec("o = difference_"+attr+"[d]")
   t = cr(h, zeta, o)
   if c != len(l):
     d = d + 1
   exec("rd"+str(n)+"_normalized_cr.append(t)")   
   c = c + 1
  else:
   c = c + 1

for n in range(1, len(l) + 1):
 if n in rd_range:
  b = str(n)                                  
  exec("%s = %s" % ("rd"+b+"_score",[0,0]))
  exec("z = rd"+b+"_normalized_cr")
  exec("rd"+b+"_score[0]=z[0] * energy_weight")
  exec("rd"+b+"_score[1]=z[1] * location_weight")
  
for rd_number in range(1, (int(n) + 1)):	
 if rd_number in rd_range:
  index = str(rd_number-1)
  rd_number = str(rd_number)
  exec("q["+ index + "]=(sum(rd" + rd_number + "_score))")

print("rd" + str(q.index(max(q)) + 1))