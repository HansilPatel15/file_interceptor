<h1>file_interceptor</h1>


<h2>Description</h2>
- file interceptor script <br>
<br>This script intercepts HTTP traffic to prevent the download of executable files (.exe) by redirecting requests to a different URL. It captures and modifies packets using netfilterqueue and Scapy.<br>

<br>Features: <br>
- Packet Interception: Captures HTTP requests and responses using netfilterqueue and iptables.<br>
- Executable File Detection: Detects requests for executable files and prevents their download.<br>
- HTTP Redirect: Redirects requests for executable files to a specified URL.<br>
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 


<h2>Environments Used </h2>

- <b>Linux</b> 

<h2>Usage: </h2>
 Run the script with the required options:
<br>sudo python http_redirector.py
<br>Set up iptables rules:
<br>sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
<br>sudo iptables -I INPUT -j NFQUEUE --queue-num 0
<br>sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0

<br>Example:
<br>The script is configured to redirect requests for executable files to https://www.rarlab.com/rar/winrar-x32-611.exe. Modify the URL in the set_load function as needed.
<br>
<b>Requirements:</b><br>
- Python 3.x<br>
- Scapy library (pip install scapy)
- NetfilterQueue library (pip install NetfilterQueue)<br>
- Root or sudo privileges for packet manipulation<br>
