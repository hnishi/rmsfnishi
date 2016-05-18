# rmsfnishi.py v 2.0

fn_trj = './sample/coord_ext.dat'
compo = 21  #The num of atoms

############################################## CODE
import sys
import numpy as np

print "rmsfnishi.py"

dim = 3
print "dimension: ",dim
print "the number of atoms: ",compo

f = open(fn_trj)
cord = np.array(f.read().split(),dtype=float)
f.close()
structure = len(cord)/dim/compo
print "the number of structures: ", structure

#cord = cord.reshape(len(cord)/dim,dim)
#print cord

##### CALCULATE AVERAGE STRUCTURE
ave = [0] * (compo*dim) #initialize 0 up to 63 components
for n in xrange(structure):
    #print n
    for i in xrange(compo*dim):
        #print i
        ave[i] += cord[n*compo*dim+i]
        #print ave[i]
for i in xrange(compo*dim):
    ave[i] = ave[i]/structure
    #print ave[i]

##### CALCULATE RMSF
rmsf = [0] * (compo)
for n in xrange(structure):
    for i in xrange(compo):
        #rmsf[i*dim] += (cord[n*compo*dim+i*dim]-ave[i*dim]) ** 2
        #rmsf[i*dim+1] += (cord[n*compo*dim+i*dim+1]-ave[i*dim+1]) ** 2 
        #rmsf[i*dim+2] += (cord[n*compo*dim+i*dim+2]-ave[i*dim+2]) ** 2
        x = (cord[n*compo*dim+i*dim]-ave[i*dim]) ** 2
        y = (cord[n*compo*dim+i*dim+1]-ave[i*dim+1]) ** 2 
        z = (cord[n*compo*dim+i*dim+2]-ave[i*dim+2]) ** 2
        rmsf[i] += x + y + z
for i in xrange(compo):
    rmsf[i] = np.sqrt( rmsf[i]/structure )
    print rmsf[i]



#print np.shape(dots)
#print dots 

##### OUTPUT PC COORDINATES OF ALL STRUCTURES  
#fn_pcc = 'c1.dat'
#if opts.fn_pcc:
#   fn_pcc = opts.fn_pcc
#output = open(fn_pcc,'w')
#for i in dots:
#   print >> output, i
#output.close()

