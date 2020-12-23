- Two distinct transport-layer protocols available to the application layer: TCP, UDP
  - TCP: Transmission Control Protocol
    - which provide a reliable, connection-oriented service to the invoking application.
  - UDP: User Datagram Protocol
    - which provides an unreliable, connectionless service to the invoking application.

- Internet Protocol provides logical communication between hosts, *but it makes not guarantees (unreliable service)*. 
  - It does not guarantee segment delivery.
  - It does not guarantee orderly delivery of segments.
  - It does not guarantee the integrity of the data in segments.

- The most fundamental responsibility of UDP and TCP is to extend IP's delivery service between two end systems to a delivery service between two processes running on the end systems.
- UDP and TCP also provide integrity checking by including error-detection fields in their segments headers.

- UDP provides two minimal transport-layer services: 
  - process-to-process data delivery
  - error checking

- TCP offers several additional services to applications:
  - First and foremost: reliable data transfer - using flow control, sequence numbers, acknowledgments, and timers, TCP ensures that data is delivered from sending process to receiving process correctly and in order.
(Page 228)