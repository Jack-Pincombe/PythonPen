
import time

'''
outputs all of the IP's within  a give range
'''


def loop(ip):
    for i in range(1,256):
        print("Checking: "+ ip + '.' + str(i) )
        time.sleep(0.1)


loop('192.168.2')

