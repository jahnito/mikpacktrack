from netmiko import ConnectHandler
from classes import RunConfig, RawConfig
import tomllib
from pprint import pprint


# Load creds
with open('config.toml', 'rb') as conf:
    router = tomllib.load(conf)

ssh = ConnectHandler(**router)

runconf = RunConfig(ssh)

# print(runconf.resources)
# print(runconf.routes)

for i in runconf.routes:
    print(i)

# rawconf = RawConfig(ssh)

# print(rawconf.resources)


# print(rawconf.routes)