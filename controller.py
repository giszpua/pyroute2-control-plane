import os
import socket
import time

NODE_NAME = os.getenv("NODE_NAME", "node")

router_id = socket.gethostbyname(socket.gethostname())

config = f"""
!
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
end
"""

while True:
    with open("/etc/frr/frr.conf", "w") as f:
        f.write(config)

    print("FRR config rendered")

    time.sleep(60)