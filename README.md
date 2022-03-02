# Ansible Role: Proxmox KVM Management

Create and manage Proxmox KVM virtual machines.

## Requirements
See *requirements.txt*.

Use this command to install all requirements:
```
python3 -m pip install --user -r requirements.txt
```

Setup credentials in ENV with:
```
source extras/proxmox-variables.sh
```

The script will add automatically @pem to the username.

If you prefer, you can setup the credentials in a secure vault file, using these parameters:
    
    credentials:
      username: root@pem
      password: yourpassword

## Role Variables
See defaults/globals.yml for the complete list of variables.
See also [proxmox_kvm] module page.

## Dependencies
Module community.general.proxmox_kvm that can be found in collection community.general.

## Usage
Define a inventory of virtual machines in this format:

```
kvm_guests:
  hosts:
   vm1:
     net: {"net0":"virtio=32:5F:B4:35:16:0F,bridge=vmbr0"}
     scsi: {"scsi0":"local-lvm:8,ssd=1"}
     bootdisk: 'scsi0'
     cores: 1
     memory: 1024
     balloon: 512
     vga: vmware
   vm2:
     net: {"net0":"virtio=32:5F:B4:37:16:0F,bridge=vmbr1"}
     scsi: {"scsi0":"local-lvm:16,ssd=1"}
     bootdisk: 'scsi0'
     cores: 4
     memory: 4096
     protection: yes
```

Execute playbook:
```
ansible-playbook ansible-proxmox-kvm-mgmt.yml --tags "OPERATION"
```

Tag **OPERATION**:
  * Create VMs
    * **present**
    * **create**
  * Start VMs
    * **started**
    * **start**
  * Delete VMs
    * **absent**
    * **delete**
  * Stop VMs
    * **stopped**
    * **stop**
  * Restart VMs
    * **restarted**
    * **restart**
  * List VMs
    * **current**
    * **list**
  * Update VMs
    * **update** 

## Example Playbook
```
---
- hosts: localhost  
  roles:
    - ansible-proxmox-kvm-mgmt
  vars:
    - global_api_host: NODE_IP or NODE_DNS_NAME
    - global_node: "NODENAME"
    - vm_list:
        - name: example-vm1
          net: {"net0":"virtio=32:5F:B4:35:16:0F,bridge=vmbr0"}
          scsi: {"scsi0":"local-lvm:8,ssd=1"}
          bootdisk: 'scsi0'
```
**And other variables from defaults/main/globals.yml**

## License

GPL-3.0

[proxmox_kvm]: <https://docs.ansible.com/ansible/latest/modules/proxmox_kvm_module.html>
