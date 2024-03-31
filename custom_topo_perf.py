WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # hosts and switches
        leftHost1 = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        rightHost1 = self.addHost( 'h3' )
        rightHost2 = self.addHost( 'h4' )
        rightSwitch = self.addSwitch( 's2' )

        # links
        self.addLink( leftHost1, leftSwitch, bw = 50, cls=TCLink )
        self.addLink( leftHost2, leftSwitch, delay = '10ms', cls=TCLink )
        self.addLink( leftSwitch, rightSwitch, cls=TCLink )
        self.addLink( rightSwitch, rightHost1, delay = '10ms', cls=TCLink )
        self.addLink( rightSwitch, rightHost2, cls=TCLink )


topos = { 'mytopo': ( lambda: MyTopo() ) }
