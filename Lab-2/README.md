Hi,

I just started with mininet and have doubts in how mininet actually work ,
the statement written and wireshark capture is contrasting with my
understanding.

Below is URL I am referring and I run command <h1 ping -c 1 h2> , I want to
understand how exactly it is working
http://mininet.org/walkthrough/


*mininet> h1 ping –c 1 h2*
This commands sends a single ping packet from h1 to h2.
The first host (h1) ARPs for the MAC address of the second (h2) causes a
packet_in message to go to the OpenFlow controller.
The controller then sends a packet_out message to flood the broadcast
packet to other ports on the switch (in this example, the only other data
port). The second host observes the ARP request and sends a broadcast
reply. This reply goes to the controller, which sends it to the first host
and pushes down a flow entry to the flow table of s1 (OpenFlow switch).

*Capture from wireshark*
 No   Time                 Source                         Destination Protocol
length   info
"223","13.873972000","fe:92:02:80:f4:38" ,"Broadcast" ,"OF 1.0" ,"126"
,"of_packet_in"
"224","13.875076000","127.0.0.1" ,"127.0.0.1" ,"OF 1.0" ,"90"
,"of_packet_out"
"225","13.875098000","127.0.0.1" ,"127.0.0.1" ,"TCP" ,"66" ,"51188 >
openflow [ACK] Seq=85 Ack=49 Win=86 Len=0 TSval=1129345 TSecr=1129345"
"226","13.875666000","b6:b1:90:42:e0:2c" ,"fe:92:02:80:f4:38","OF 1.0"
,"126" ,"of_packet_in"
"227","13.876417000","127.0.0.1" ,"127.0.0.1" ,"OF 1.0" ,"146"
,"of_flow_add"
"228","13.877426000","10.0.0.1" ,"10.0.0.2" ,"OF 1.0" ,"182" ,"of_packet_in"
"229","13.878206000","127.0.0.1" ,"127.0.0.1" ,"OF 1.0" ,"146"
,"of_flow_add"
"230","13.879014000","10.0.0.2" ,"10.0.0.1" ,"OF 1.0" ,"182" ,"of_packet_in"
"231","13.879655000","127.0.0.1" ,"127.0.0.1" ,"OF 1.0" ,"146"
,"of_flow_add"


*mininet> h1 ifconfig*
h1-eth0   Link encap:Ethernet  HWaddr fe:92:02:80:f4:38
          inet addr:10.0.0.1  Bcast:10.255.255.255  Mask:255.0.0.0

*mininet> h2 ifconfig*
h2-eth0   Link encap:Ethernet  HWaddr b6:b1:90:42:e0:2c
          inet addr:10.0.0.2  Bcast:10.255.255.255  Mask:255.0.0.0


*My Questions/Doubts*
*Packet 223 - *who does this switch or host? if switch does why the source
address is of host1 physical address and why brodcast require as only
controller understand "of_packet_in".  If host does then how host can
directly broadcast and host cannot send of_packet_in as it does not
understand anything related to openflow stuff?
*Packet 224 - *This should be from controller to switch
*Packet 226 - *how packet wit info "of_packet_in" can go from host2
physical address to host1 physical address

No clue what is going on. Can someone explain with step by step what is the
exact sequence and how communicates with whom and why?


Thanks,
Archit
-------------- next part --------------
An HTML attachment was scrubbed...
URL: <http://mailman.stanford.edu/pipermail/mininet-discuss/attachments/20170826/51f599b8/attachment.html>
