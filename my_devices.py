#!usr/bin/etc python
from netmiko import ConnectHandler

nxos_list = ["nxos1.lasthop.io","nxos2.lasthop.io"] 

for nxos_node in nxos_list :
    print ("ssh to :",nxos_node) 
    nxos_device = {
        "host": nxos_node,
        "username": 'pyclass',
        "password":'88newclass',
        "device_type":'cisco_nxos',
        #session_log='my_ssh_log.txt',
        }
    ssh_dev = ConnectHandler(**nxos_device)
    print (ssh_dev.find_prompt())



