import numpy as np
import glob as glob

u = 2.5
v = 0.0
w = 0.0

ifilename = glob.glob('*.fds')[0]

with open(ifilename) as ifile:
    lines = ifile.readlines()

for line in lines:
    if line[:5] == '&MESH':
        break

istart = line.find('IJK=') + 4
iend   = line.find('XB')
line = line[istart:iend]
i,j,k,_ = line.split(',')
i = int(i)
j = int(j)
k = int(k)

nvel = (i+1)*(j+1)*(k+1)

#--------------------------------

with open(ifilename) as ifile:
    lines = ifile.readlines()
for line in lines:
    if line.find('I_UPPER') > 0:
        break

istart = line.find('I_UPPER=')+8
iend   = line.find(',', istart)
npx = int(line[istart:iend]) + 1

jstart = line.find('J_UPPER=')+8
jend   = line.find(',', jstart)
npy = int(line[jstart:jend]) + 1

kstart = line.find('K_UPPER=')+8
kend   = line.find(',', kstart)
if kend==-1:
    kend   = line.find('/', kstart)
npz = int(line[kstart:kend]) + 1

np = npx*npy*npz

#-------------------------------

for ip in range(1,np+1):

    ofilename = 'initial_velocity_field_m' + f'{ip:03}.csv'

    with open(ofilename,'w') as ofile:
        ofile.write(f'0,{i:d},0,{j:d},0,{k:d}\n')
        for i in range(nvel):
            ofile.write(f'{u:f},{v:f},{w:f}\n')

