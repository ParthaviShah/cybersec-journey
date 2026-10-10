
# Nmap Flags- What I learned

## -sV( Service Version  Detection)
Command: nmap -sv -p 22,80,110 scanme.nmap.org

Found exact software versions:
-Port 22: OpenSSH 6.6.1p1(Ubuntu) - an old version
-Port 80: Apache httpd 2.4.7(Ubuntu)- also old
-Port 110: pop3, version unclear, service gave an error response

Why this matters:
Knowing the exact version lets us check if that specific version has known security vulnerabilities.This scan was fast and gave confident, specific answers

## -O (OS Detection)
Command: sudo nmap -O -p 22,80,110 scanme.nmap.org
Result was NOT confident- nmap gave several gusses with percentages( VirtualBox 92%, QEMU 90%)

## Key takeaway
-sV gave reliable, specific answers. -O gave uncertain, percentage based gusses on this target. Version detection seems more dependable than OS detection, at least under these conditions.


 
