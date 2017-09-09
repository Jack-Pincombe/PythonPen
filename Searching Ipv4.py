


'''
outputs all of the IP's within  a give range
'''


def loop(ip):
    for i in range(1,256):
        print(ip + '.' + str(i) )


loop('192.168.2')

