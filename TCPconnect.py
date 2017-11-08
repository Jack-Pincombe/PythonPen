import optparse
from socket im

parser = optparse.OptionParser('usage %prog -K '+ \
                               '<target host> -p <target port>' )

parser.add_option('-H', dest='tgtHost', type='string',\
                  help='specify target host')

parser.add_option('-p', dest='tgtPort', type=int, \
                  help='Specify the target port')

(options, args ) =  parser.parse_args()


tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost == None) | (tgtPort == None):
    print(parser.usage)
    exit(0)