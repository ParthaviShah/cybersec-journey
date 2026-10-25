# Wireshark Basics

Captured and analyzed live network traffic from my own machine using
Wireshark, to understand what's actually happening under the hood
every time a browser loads a page.

## 1. DNS (Domain Name System)
DNS is the internet's "phonebook" - it translates a website name
(like play.google.com) into the actual IP address needed to reach
it, since computers only understand numbers, not names.

A "Standard query" is my computer asking "what's the IP address for
this website?" A "Standard query response" is the answer coming
back with the real address. I found a real example where my own
machine silently queried play.google.com in the background, without
me directly visiting that site - a reminder that a lot of DNS
traffic happens automatically, not just when typing a URL myself.

## 2. HTTP (Hypertext Transfer Protocol)
HTTP is the actual request for a web page or file. Looking at a
captured HTTP request, I could see headers like Host (which site is
being asked), User-Agent (my browser identifying itself - e.g.
"I'm Chrome on Linux"), and Accept-Language (my preferred language).

This is the same kind of information I saw earlier in Burp Suite -
the difference is that Burp only captures browser traffic I've
routed through it, while Wireshark captures everything on the
network, from any application, including things Burp would never
show (like the DNS query above).

## 3. TCP (the 3-way handshake)
Before any real data is exchanged, two computers go through a
3-step "hello" process:
1. SYN - my computer: "I'd like to start a connection"
2. SYN, ACK - the server: "Got it, I'm ready too"
3. ACK - my computer: "Confirmed, let's begin"

Only after this handshake completes does the actual HTTP request
and page content get sent. I observed this pattern directly in
Wireshark using the filter `tcp.flags.syn==1`.

## Why this matters beyond just this exercise
Burp Suite shows web-application-level traffic (good for VAPT/
web security work). Wireshark shows network-level traffic from
everything on the machine (useful for SOC/blue-team work, like
spotting malware quietly "phoning home" to an unknown server,
or diagnosing why a connection is failing). Having both gives
visibility into two different layers of the same system.
