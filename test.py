import netmiko
from netmiko import ConnectHandler
from classes import RunConfig
import tomllib
from pprint import pprint


# Load creds
with open('config.toml', 'rb') as conf:
    router = tomllib.load(conf)

ssh = ConnectHandler(**router)

runconf = RunConfig(ssh)

print(runconf.resources)

for i in runconf.routes:
    print(i)