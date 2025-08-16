from netmiko import BaseConnection
import textfsm


class RunConfig:
    def __init__(self, ssh: BaseConnection):
        self.ssh = ssh
        self.resources = self.get_resources()
        # self.ipintf = self.get_ipintf()
        self.routes = self.get_routes()

    def get_resources(self):
        output = self.ssh.send_command('/system resource print without-paging')
        with open('templates/mikrotik_routeros_system_resource_print.textfsm') as tpl:
            fsm = textfsm.TextFSM(tpl)
            result = fsm.ParseText(output)
            return dict(zip(fsm.header, *result))

    # def get_ipintf(self):
    #     output = self.ssh.send_command('/ip address print where disabled=no')
    #     with open('templates/mikrotik_routeros_ip_address_print.textfsm') as tpl:
    #         fsm = textfsm.TextFSM(tpl)
    #         result = fsm.ParseText(output)
    #         return result

    def get_routes(self):
        output = self.ssh.send_command('/ip route print terse without-paging')
        print(output)
        ros_major_version = int(self.resources['VERSION'].split('.')[0])
        if ros_major_version <= 6:
            with open('templates/mikrotik_routeros_ip_route_print_terse_without-paging.textfsm') as tpl:
                fsm = textfsm.TextFSM(tpl)
                result = fsm.ParseText(output)
                result.insert(0, fsm.header)
                return result
        elif ros_major_version == 7:
            with open('templates/mikrotik_routeros7_ip_route_print_terse_without-paging.textfsm') as tpl:
                fsm = textfsm.TextFSM(tpl)
                result = fsm.ParseText(output)
                result.insert(0, fsm.header)
                return result


class RawConfig:
    def __init__(self, ssh: BaseConnection):
        self.ssh = ssh
        self.resources = self.get_resources()
        self.routes = self.get_routes()

    def get_resources(self):
        return self.ssh.send_command('/system resource print without-paging')

    def get_routes(self):
        return self.ssh.send_command('/ip route print terse without-paging')
