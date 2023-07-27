# Network Architecture with NAT

This README.md document describes a network architecture with Network Address Translation (NAT). The architecture comprises two virtual machines (VM1 and VM2) connected to a NAT network. The NAT network is connected to a physical network interface, which is in turn connected to a router. The router is connected to a firewall, which is connected to the Internet.

## Overview

This network architecture is designed to provide internet connectivity to two virtual machines (VM1 and VM2) using Network Address Translation (NAT). NAT is a technique that allows multiple devices with private IP addresses to share a single public IP address when accessing the internet. The architecture ensures security through a firewall and allows the VMs to communicate with the external network while keeping their internal IP addresses hidden.

## Components

1. **VM1 and VM2 (Virtual Machines):** These are two virtual machines that run on a host system and serve as clients or servers in the network.

2. **NAT Network:** The NAT network acts as an internal network where VM1 and VM2 reside. It allows them to communicate with each other and share a single public IP address when accessing the internet.

3. **Physical Network Interface:** This is the physical network interface of the host system to which the NAT network is connected. It facilitates communication between the virtual machines and the external network.

4. **Router:** The router is a network device responsible for routing data between the NAT network and the external network, which is the internet in this case.

5. **Firewall:** The firewall is a security device that filters incoming and outgoing network traffic, providing an additional layer of protection for the internal network.

6. **Internet:** The internet represents the external network to which the router is connected. It provides access to various resources and services.

## Network Configuration

The network configuration for this architecture is as follows:

1. VM1 and VM2 are configured with private IP addresses within the same network segment, for example, 192.168.1.10 and 192.168.1.20, respectively.

2. The NAT network is configured to assign private IP addresses to VM1 and VM2, such as in the 192.168.1.0/24 range.

3. The physical network interface of the host system is configured with a public IP address, provided by the Internet Service Provider (ISP).

4. The router is configured to perform Network Address Translation (NAT) for outgoing traffic from VM1 and VM2. It maps the private IP addresses of VM1 and VM2 to the public IP address of the physical network interface.

5. The firewall is configured to filter and allow/deny incoming and outgoing traffic based on predefined rules. It protects the internal network from unauthorized access.

6. VM1 and VM2 are able to access the internet through the NAT network, router, firewall, and the physical network interface. Outgoing traffic from VM1 and VM2 is translated to use the public IP address of the network interface.



## Conclusion

The described network architecture with Network Address Translation (NAT) allows VM1 and VM2 to communicate with each other within the internal NAT network and access the internet using a shared public IP address. The use of a firewall enhances security by filtering network traffic, ensuring the safe transfer of data between the internal network and the internet. This setup is suitable for scenarios where multiple virtual machines need internet connectivity without requiring dedicated public IP addresses for each VM.