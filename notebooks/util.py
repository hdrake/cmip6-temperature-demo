"""This is a general purpose module containing routines
(a) that are used in multiple notebooks; or 
(b) that are complicated and would thus otherwise clutter notebook design.
"""

import re
import socket

def is_ncar_host():
    """Determine if host is an NCAR machine."""
    hostname = socket.getfqdn()
    
    return any([re.compile(ncar_host).search(hostname) 
                for ncar_host in ['cheyenne', 'casper', 'hobart']])

