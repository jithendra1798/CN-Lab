## Kill a Port Number (ex: Port 9999)
    sudo kill -9 `sudo lsof -t -i:9999`

Lab Assignment I

1) Create a TCP/IP client-server program in which a single client connects to the server. The server then should send a greeting to the client. Repeat the experiment using UDP.
2) Create a TCP/IP client-server program. The client should send a message asking for the current date. The server should respond with the current date that will be displayed on the client.
3) Create a TCP/IP server-client program in which both client and server can send and receive messages (Chat application). Repeat the experiment using UDP.
4) Create a chat room such that multiple clients can connect to a server. The clients must be able to both send and receive messages to each other via the server. Create chat rooms using TCP and UDP.
