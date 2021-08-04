from mininet.topo import Topo

class Red1(Topo):
  def build( self ):
    h1 = self.addHost("h1", mac="00:00:00:00:00:01")
    h2 = self.addHost("h2", mac="00:00:00:00:00:02")
    h3 = self.addHost("h3", mac="00:00:00:00:00:03")
    h4 = self.addHost("h4", mac="00:00:00:00:00:04")
    h5 = self.addHost("h5", mac="00:00:00:00:00:05")
    h6 = self.addHost("h6", mac="00:00:00:00:00:06")
    h7 = self.addHost("h7", mac="00:00:00:00:00:07")
    h8 = self.addHost("h8", mac="00:00:00:00:00:08")

    s1 = self.addSwitch("s1")
    s2 = self.addSwitch("s2")
    s3 = self.addSwitch("s3")
    s4 = self.addSwitch("s4")

    self.addLink(h1, s1, 10, 1)
    self.addLink(h2, s1, 10, 2)

    self.addLink(h3, s2, 10, 3)
    self.addLink(h4, s2, 10, 4)

    self.addLink(h5, s3, 10, 5)
    self.addLink(h6, s3, 10, 6)

    self.addLink(h7, s4, 10, 7)
    self.addLink(h8, s4, 10, 8)

    self.addLink(s1, s4, 9, 14)
    self.addLink(s4, s3, 9, 13)
    self.addLink(s3, s2, 9, 12)
    self.addLink(s2, s1, 9, 11)

<<<<<<< HEAD
topos = { "red1": (lambda: Red1()), "red2": (lambda: Red2())}
=======
topos = { "red1": (lambda: Red1())}

>>>>>>> 78b5c424cb30eed8fc53582044a61e054dbf3db3
