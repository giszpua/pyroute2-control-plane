import os
import socket
import time

NODE_NAME = os.getenv("NODE_NAME", "node")

router_id = socket.gethostbyname(socket.gethostname())

config = f"""
frr version 8.4
frr defaults traditional
hostname {NODE_NAME}
service integrated-vtysh-config
!
router bgp 65000
 bgp router-id {router_id}
 no bgp ebgp-requires-policy
 neighbor FABRIC peer-group
 neighbor FABRIC remote-as internal
 !
 address-family l2vpn evpn
  advertise-all-vni
 exit-address-family
!
line vty
"""

while True:
    with open("/etc/frr/frr.conf", "w") as f:
        f.write(config)

    os.system("pkill bgpd")
    time.sleep(2)
    os.system("/usr/lib/frr/bgpd -d")

    print("FRR config applied")
    time.sleep(60)