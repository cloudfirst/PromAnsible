import netifaces

def getHostNetInfo():
    hostnetinfo = {
        'exip': '',
        'ip0':  '',
        'ip1':  '',
        'ip2':  '',
        'ip3':  '',
        'mac0': '',
        'mac1': '',
        'mac2': '',
        'mac3': '',
    }
    index = 0
    list_of_nic = netifaces.interfaces()
    for nic in list_of_nic:
        if not nic.startswith('lo'):
            ipstr = 'ip' + str(index)
            macstr = 'mac' + str(index)
            addr = netifaces.ifaddresses(nic)
            if netifaces.AF_INET in addr.keys():
                hostnetinfo[ipstr]  = addr[netifaces.AF_INET][0]['addr']
            if netifaces.AF_LINK in addr.keys():
                hostnetinfo[macstr] = addr[netifaces.AF_LINK][0]['addr']
            index = index + 1

    hostnetinfo['exip'] = hostnetinfo['ip0']
    return hostnetinfo
