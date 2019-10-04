#!usr/bin/env python
from netmiko import ConnectHandler

cisco_list =  ['cisco3.lasthop.io','cisco4.lasthop.io']

for cisco in cisco_list :
    print ("ssh to :",cisco) 
    cisco_device = {
        "host": cisco,
        "username": 'pyclass',
        "password":'88newclass',
        "device_type":'cisco_ios',
        #session_log='my_ssh_log.txt',
        }
    ssh_session = ConnectHandler(**cisco_device)
    print (ssh_session.find_prompt())
    show_ver = ssh_session.send_command('show version')
    print (show_ver)




