'''Custom ansible filters for proxmox'''


class FilterModule(object):

    def filters(self):
        return {
            'inventory_to_vm_list': self.inventory_to_vm_list
        }

    def inventory_to_vm_list(self, hostvars, hostnames):
        '''adds group membership information to users'''
        vm_list = []
        for host in hostnames:
            if host not in hostvars:
                continue
            vm_list_entry = {"name": host}
            vm_list_entry.update(hostvars[host])
            vm_list.append(vm_list_entry)
        return vm_list
