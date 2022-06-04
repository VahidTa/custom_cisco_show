import subprocess
import sys


def convert_bytes(size):
    "It converts bytes to KB, MB, etc"
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.3f %s" % (size, x)
        size /= 1024.0

    return size

try:
    intf_name = sys.argv[1].replace('/', '_')
except:
    print 'Interface name is required. Please check the interface name.'
    exit(1)

if sys.argv[1].lower().startswith('loop'):
    print 'Loopback interface does not have statistics.'
    exit(1)

p = subprocess.Popen(["show_interface", "-i", intf_name ], stdout=subprocess.PIPE)
(output, Err) = p.communicate()
p.wait()

if 'not found' in output:
    print 'Interface \033[93m\033[1m"{}"\033[0m not found.'.format(intf_name)
    exit(1)

for i, v in enumerate(output.split('\n')):
    if 'packets input,' in v:
        input_index = i
        continue
    elif 'packets output,' in v:
        output_index = i
        break

output = output.split('\n')
in_data = output[input_index].split(',')[1].split()[0]
out_data = output[output_index].split(',')[1].split()[0]


print '\xf0\x9f\x87\xae\xf0\x9f\x87\xb7 \n'

print '\xE2\x9C\x85 ' + '\033[1minput data:\033[0m\t' + '\033[92m{}\033[0m'.format(convert_bytes(int(in_data))) + ' \xF0\x9F\x9A\x80 \n'
print '\xE2\x9C\x85 ' + '\033[1moutput data:\033[0m\t' + '\033[92m{}\033[0m'.format(convert_bytes(int(out_data)))+ ' \xF0\x9F\x9A\x80 \n'
print '\xF0\x9F\x98\x83' '\xF0\x9F\x98\x8D \n'