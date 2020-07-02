# -*- coding: utf-8 -*-
import os, socket,  argparse

print('# FS2PWN v0.1 | Coded by Abdullah AlZahrani https://github.com/0xAbdullah')

parser = argparse.ArgumentParser(description="[--] First Step to pwn (FS2PWN) is script to automate some task.")
parser.add_argument('-t', required=True, default=None, help='Set target subnet\n[EX: sf2pwn.py/exe -t 10.10.100.0/24]')
args = vars(parser.parse_args())

def fs2PWN():
    subnet = args['t'].replace('/', ' ').split()
    print("[*] Let's GO.")
    hostup = []
    ports = {
        'FTP': 21,
        'SSH': 22,
        'HTTP': 80,
        'HTTPS': 443,
        'SMB': 445,
        'MSSQL': 1433,
        'MYSQL': 3306,
        'RDP': 3389,
        'PostgreSQL': 5432,
        'winRM': 5985}

    if subnet[1] == '24':
        hosts = 255
    elif subnet[1] == '25':
        hosts = 127
    elif subnet[1] == '26':
        hosts = 63
    elif subnet[1] == '27':
        hosts = 31
    elif subnet[1] == '28':
        hosts = 15
    elif subnet[1] == '29':
        hosts = 7

    for ip in range(1, hosts):
        pingSweep = os.popen('ping -n 1 -w 300 {}{}'.format(subnet[0][:-1], ip)).read()
        if 'Received = 1' in pingSweep:
            getHostname = os.popen('ping -a -n 1 -w 200 {}{}'.format(subnet[0][:-1], ip)).read().split()
            hostname = getHostname[1]
            if '{}{}'.format(subnet[0][:-1], ip) == hostname:
                if getHostname[12] == 'TTL=64':
                    hostname = 'Unknown (linux machine)'
                else:
                    hostname = 'Unknown'
            print('\n[H] IP: {}{} Hostname: {}'.format(subnet[0][:-1], ip, hostname))
            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                try:
                    con = s.connect(('{}{}'.format(subnet[0][:-1], ip), ports[port]))
                    print("[P] {} {} open.".format(port, ports[port]))
                    con.close()
                except:
                    pass
            hostup.append('{}{}'.format(subnet[0][:-1], ip))
    print('[I] I found {} hosts up!'.format(len(hostup)))
    return hostup

if __name__ == '__main__':
    fs2PWN()
