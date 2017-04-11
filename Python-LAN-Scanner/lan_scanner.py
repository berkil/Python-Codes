#!/usr/bin/python

"""
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
| Built By Boris Bakshiyev |       v1.1          |   
| ~~~~~~~~~~~~~~~~~~~~~~~~ | ~~~~~~~~~~~~~~~~~~~ |
"""

import sys,logging,socket,os,sys, webbrowser,time
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def main():

    arp_scanner(sanity_check())
    print '\n\n\t\tThe Network Has Been Scanned- The Log Will Be Opened Now'
    time.sleep(2)
    webbrowser.open('lan_log.txt')
    time.sleep(2)


def sanity_check():
    
    computer = (ARP().psrc).split('.')
    ip = str(computer[0])+'.'+str(computer[1])+'.'+str(computer[2])+'.0/24'

    if str(computer[0]) != '0':
        pass
    else:
        print '\n\n\t\t\t! ! ERROR- Connection Issue ! ! \n\t\t\t  Pleas Connect To LAN Network'
        exit(0)

    if os.getuid() != 0:
        os.system('clear')
        print '\n\n\t\t ! ! ERROR- Permission Issue ! ! \n\t\t Run This Program As Administrator\n\n'
        exit(0)

    return ip
    

def arp_scanner(lan):

    print '\n\n\t\t\tThe Program Started\n\t\tAt The End LOG File Will Be Opene \n'
    live,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff" )/ARP(pdst=str(lan)),timeout=1, verbose=0)
    for s,r in live :
        lan_file = open('lan_log.txt','a+')
        lan_file.write ('\n[*]\t'+r.sprintf('IP: %ARP.psrc%\tMAC: %ARP.hwsrc%\n'))
        print r.sprintf ("%ARP.psrc%"),'Beeing scanned for open ports'
        for port in range (1,200):
            banner=port_scanner((r.sprintf ("%ARP.psrc%")),port)
            if banner != False:
                if len(banner) >= 1:
                    lan_file.write ('\t\t* PORT: '+str(port)+' Service: '+str(banner)+'\n')
                else:
                    lan_file.write ('\t\t* PORT: '+str(port)+' Is opened, but have no registered service\n')         


def port_scanner(ip,port):

    socket.setdefaulttimeout(2)
    com = socket.socket()
    try:
        com.connect((str(ip),port))
        banner = (str(com.recv(1024))).strip()
        return banner.strip(' ')
    except:
        com.close()
        return False
                                

os.system('clear')

try:   
    from scapy.all import * 
except:
    print '\n\n\t\t! ! ERROR- Missing Package ! !\n\t\t You Have To Install \'scapy\'\n\t      Try \'sudo apt-get install scapy\''
    exit()

main()
