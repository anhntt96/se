## NETWORKING

1. Read the concept of TCP in [this wiki page](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) and try to understand all the concepts of it (deeply):
    - How TCP open a connection? what does it need to open a connection?
        + Why there are 3 way handshakes but not 2 way? 
        + What is syn, ack mean?
        + Why they have to send 2 "random" sequence numbers? The purpose of this sequence number?
        + What if the 3rd handshake fail? How the server can detect it and what does it do in this case?
    - How TCP handles the connection?
        + What happens if some bits are wrong due to connection errors? How to detect them and fix them?
        + How the timeout is handled? what if the timeout is expired?
        + What will happen if some "packet" is missing on the way?
        + How to detect the appropriate number of packets to send (speed of sending packet)?
    - How TCP close the connection?
        + What if the internet is dropped in the middle of the connection? Or in case one peer is crash?
    - How long you can keep a TCP connection alive?

2. What are the differences between TCP and UDP? And in which case we use which?

3. How Ping command works? What is TTL?? How does TTL will be changed?? 

4. How HTTP works?
    - Why did people say that HTTP is stateless? The reason they make it stateless?
    - Can we make a persistent HTTP connection? pros and cons of this way?
    - Why HTTP require cookie each time we send the request?
    - Can someone use your cookie and log in your Facebook account? How to migrate this?
    - What is HTTP session? How does authentication work in HTTP? What is JWT?
    - Which type of "data" HTTP can help us to get or push? (binary file? image? text file? video file? music file?)
    - REST/RESTful?
    - AJAX technique? 
    - How HTTPs work?
    - Learn about some useful headers.

5. When you type "google.com" into your browser, that will happen when you type enter till everything is displayed on your screen?
    - DNS lookup (in case you already access google.com before and also in case you do not know the IP of google.com)
        + Which protocol DNS use and why?
        + The other of place to look up DNS.
    - TCP or UDP will be used in this case? why?
    - How to know "google.com" require HTTP or https? how browser can know and redirect from HTTP to HTTps?
    - After you get the `HTML content` for "google.com" how to get the `*.js` and `image` files?
    - When getting `*.js` or `image` files do why use another `TCP connection` or use the same one as in the get `HTML content`? How DNS lookup work in this case?
    - After your browser display "google.com" fully, is there any connection open?
    - Caching can apply to which steps? How caching applied?

6. What is the connection pool? It's advantages and disadvantages? How to implement connection pool in your programing language?

7. What is socket?
    - Why do we need socket? Why socket is a "file" in linux?
    - What is `src port` when you create a connection to a "server"?
    - What one server can handle multiple connections to the same port? [Good answers here but read all answers](https://stackoverflow.com/questions/3329641/how-do-multiple-clients-connect-simultaneously-to-one-port-say-80-on-a-server)
    - What is the maximum number of connections a server can handle? (if it has unlimited resource) (in case of the same client and in case of multiple clients)
    - When you open multiple tabs on your chrome, how OS knows which packet (both sending and receiving) correspond to which tab? (how about in case you open many tabs to the same page "for eg: google.com")
    - What are the maximum numbers of connection your machine can connect to "google.com" (if you have unlimited resource)
    - Can two processes listen to the same port on your machine? Why? How?
    - What is `buffer`? why we always need buffer when working with "file"?
    - What is `unix socket`? When to use it?

8. What is `TCP proxy`? `reverse proxy`? and `VPN`?
    - How your router at your home works?
        + Inside LAN network, it uses IP or MAC address? Why?
        + How does it know which packet comes from (or arrive at) which machine?
        + What is the difference between Hub and Switch inside LAN?
        + How src IP/PORT and dst IP/PORT change on the way to the server?
    - How `load-balancer` works? (this one is a tough question) // hint: it opposite to how to router work. 
        + When we send a packet to a `load-balancer` how does it forward to the desired server? (Does it keep any data on its memory?)
        + When the server wants to send data back to the client, does the connection need to go through the `load-balancer`? 
        + What is different between `reverse proxy` and `load-balancer`?
        + Can `load-balancer` be a bottleneck? (Because it is the end-point of too many requests) (bottleneck about RAM or CPU or Network?)
        + Try to understand everything in [this page](https://softwareengineering.stackexchange.com/questions/312956/what-does-a-load-balancer-return) (all the answers)