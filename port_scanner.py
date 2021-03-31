import socket
import common_ports

def get_open_ports(target, port_range,verbose=False):
  open_ports = []
  verbosetext=""
  target1=""
  hostname=""
  if not target.replace('.', '').isnumeric():
    #hostname
    hostname=target
    try:
      target1 = socket.gethostbyname(target)
    except socket.gaierror:
      return "Error: Invalid hostname"
  else:
    # ip
    target1=target
    try:
      hostname=socket.gethostbyaddr(target)[0]
    except socket.gaierror:
      return "Error: Invalid IP address"
    except Exception as e:
      hostname=target
      target1=target
  if target1==hostname:
    verbosetext+="Open ports for {}\n".format(hostname)
  else:
    verbosetext+="Open ports for {} ({})\n".format(hostname,target1)
  verbosetext+="PORT     SERVICE\n"
  port_range[1]=port_range[1]+1
  for x in range(port_range[0],port_range[1]):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    res = sock.connect_ex((target1,x))
    if res==0:
      open_ports.append(x)
      a=7
      if x>100:
        a=6
      verbosetext+="{}{}{}\n".format(x," "*a,common_ports.ports_and_services[x])
    sock.close()
  
  if verbose:
    return(verbosetext[:-1])
  else:
    return(open_ports)