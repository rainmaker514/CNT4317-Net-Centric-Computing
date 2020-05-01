import sys, time

#Usage: pipe the output of this command into telnet
# tel.py www2.fiu.edu /~downeyt/index.html

if len(sys.argv) < 3:
    print ("Usage: tel.py host resource")
    sys.exit()

print ("open {0} 80".format(sys.argv[1]))
time.sleep( 2 )
print ('''\
GET {1} HTTP/1.1
Host: {0}

'''.format(sys.argv[1], sys.argv[2]))
time.sleep( 2 )
