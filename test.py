import netmiko
from netmiko import ConnectHandler
from classes import IpInterfaces

router = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.3.129',
    'port': '22',
    'username': 'netmiko+ct',
    'password': 'netmiko'
}

ssh = ConnectHandler(**router)

out = ssh.send_command('/ip address print')

print(out)

