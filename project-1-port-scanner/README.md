# Python Port Scanner

A client-side port scanner built from scratch using Python's `socket`
library, as a way to understand what tools like Nmap are actually
doing underneath their flags - specifically `-sV` (version detection).

## What it does
- Takes a target, a start port, and an end port as command-line input
- Checks each port in that range to see if it's open
- Attempts to grab a "banner" (the service's self-announcement) from
  any open port it finds

## How to run it
    python3 port_scanner.py <target> <start_port> <end_port>

Example:
    python3 port_scanner.py scanme.nmap.org 0 100

## What I learned

**Timeouts affect open/closed detection, not banner behavior.**
With a 1-second timeout, port 80 sometimes showed as closed because
the server didn't respond fast enough within that window. Increasing
the timeout to 3 seconds made the open/closed detection reliable.
However, this did NOT fix banner grabbing on port 80 - that's a
separate issue entirely (see below).

**Different services behave differently when it comes to banners.**
- Port 22 (SSH) sends a banner automatically on connection. My
  script successfully captured it: `SSH-2.0-OpenSSH_6.6.1p1
  Ubuntu-2ubuntu2.13` - this is literally the same information
  Nmap's `-sV` flag reports, which helped me understand what that
  flag is actually doing behind the scenes.
- Port 80 (HTTP) does NOT send a banner automatically - it waits
  for a request first. My script times out trying to read a banner
  here, regardless of timeout length, because nothing is ever sent
  unless I ask. A more complete version would send a basic HTTP GET
  request before trying to read a response.
- Port 110 (POP3) also returned no banner. Cross-checking against
  an earlier Nmap `-sV` scan I ran on this same target, Nmap itself
  flagged this service as returning an error ("Can not connect to
  e-mail server"), suggesting the service is misconfigured rather
  than my script being at fault.

**Command-line arguments make a script into a reusable tool.**
Originally I hardcoded the target and port range directly in the
code, meaning I had to edit the file every time I wanted to scan
something different. Using `sys.argv`, I separated the input from
the logic - now the script can scan any target/range without
touching the code, the same way `nmap <target>` works without
needing to edit Nmap's own source.

## Limitations / what I'd improve
- No GET request sent for HTTP ports, so banner grabbing fails there
- Single connection attempt per port, no retries (Nmap retries,
  which likely makes it more reliable than my script)
- Scans sequentially, one port at a time - slower than it could be
  with threading
