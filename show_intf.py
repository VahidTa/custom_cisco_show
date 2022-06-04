import subprocess
import sys

DOWN = '\xE2\x9D\x8C ' # down emoji.
UP_DOWN = '\xE2\x9A\xA0 ' # up-down emoji.
TOTAL_DOWN = '\xF0\x9F\x98\xB4' # sleepy emoji.
TOTAL_ADMIN_DOWN = '\xf0\x9f\x91\xa8\xf0\x9f\x92\xbb' # man and laptop emoji
UP = '\xE2\x9C\x85 ' # up emoji.
TOTAL_UP = '\xF0\x9F\x9A\x80' # rocket emoji.

try:
    vrf = sys.argv[1]
except:
    vrf = 'default'

p = subprocess.Popen(["show_ip_interface", "-b", "-v", vrf ], stdout=subprocess.PIPE)
(output, Err) = p.communicate()
p.wait()


for i, v in enumerate(output.split('\n')):
    if 'Interface' in v:
        input_index = i+1
        break
else:
    print 'No Interface found. Check the VRF \033[93m\033[1m"{}"\033[0m name.'.format(vrf)
    exit(1)

output = output.split('\n')[input_index:]

res = []
total_up = 0
total_down = 0
total_admin_down = 0

for line in output:
    data = line.split()
    if data:
        if data[2] == 'Up' and data[3] == 'Up':
            data[0] = '{}'.format(UP) + data[0]
            total_up += 1
        elif data[2] == 'Shutdown':
            data[0] = '{}'.format(DOWN) + data[0]
            total_admin_down += 1
        elif data[2] == 'Up' and data[3] == 'Down':
            data[0] = '{}'.format(UP_DOWN) + data[0]
            total_down += 1
        else:
            data[0] = '{}'.format(DOWN) + data[0]
            total_down += 1

        res.append(data)

del output

print "_"*100
print
print "{0:<3}{1: <27}{2: <20}{3: <20}{4: <20}{5}".format('','Interface', 'IP-Address', 'Status', 'Protocol', 'Vrf-Name')
print "_"*100
print 
for i in res:
    print '{0: <31}{1: <20}{2: <20}{3: <20}{4}'.format(*i),
    print

print '\nTotal \033[1m\033[92mUp\033[0m: {0} {1}'.format(total_up, TOTAL_UP)
print 'Total \033[1m\033[91mDown\033[0m: {0} {1}'.format(total_down, TOTAL_DOWN)
print 'Total \033[1m\033[94mAdmin Down\033[0m: {0} {1} \n'.format(total_admin_down, TOTAL_ADMIN_DOWN)
