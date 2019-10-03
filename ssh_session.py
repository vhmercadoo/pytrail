#!/usr/bin/etc python
from netmiko import ConnectHandler

nxos_device_1= {
    "host":'nxos1.lasthop.io',
    "username": 'pyclass',
    "password":'88newclass',
    "device_type":'cisco_nxos',
    #session_log='my_ssh_log.txt',
}
nxos_device_2= {
    "host":'nxos2.lasthop.io',
    "username": 'pyclass',
    "password":'88newclass',
    "device_type":'cisco_nxos',
     #session_log='my_ssh_log.txt',
}

my_nxos_1=ConnectHandler(**nxos_device_1)
my_nxos_2=ConnectHandler(**nxos_device_2)
print (my_nxos_1.find_prompt())
print (my_nxos_2.find_prompt())

