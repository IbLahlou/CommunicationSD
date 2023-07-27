# Socket Programming in Python

## Overview

Socket programming in Python allows communication between processes over a network. It provides a low-level networking interface that enables data exchange between different devices, either locally or over the internet. This README provides an overview of socket programming in Python, covering connected and unconnected modes, as well as its relevance to parallel programming.

## Connected Mode

In connected mode, socket programming follows the client-server architecture, where one socket acts as the server, waiting for incoming connections, and the other socket acts as the client, initiating the connection. The server listens for client requests and responds to them.


## Unconnected Mode (Datagram Sockets)

In unconnected mode, socket programming uses datagram sockets, which operate on the UDP (User Datagram Protocol). Unlike connected mode, it does not require a persistent connection between the client and server.



## Socket Programming and Parallel Programming

Socket programming plays a vital role in parallel programming, enabling communication between multiple processes or threads running concurrently on different devices or on the same machine.

Parallel programming in Python can be achieved using threads or processes. Sockets allow these threads or processes to exchange data and coordinate their activities. By using socket-based communication, parallel programs can be designed to distribute tasks, share data, and achieve better performance through parallelism.

In conclusion, socket programming in Python provides a powerful mechanism for communication between processes over a network. Whether in connected or unconnected mode, sockets facilitate the exchange of data, enabling distributed systems and parallel programming to efficiently work together.

