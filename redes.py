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

		self.addLink(h1, s1, 9, 1)
		self.addLink(h2, s1, 9, 2)

		self.addLink(h3, s2, 9, 3)
		self.addLink(h4, s2, 9, 4)

		self.addLink(h5, s3, 9, 5)
		self.addLink(h6, s3, 9, 6)

		self.addLink(h7, s4, 9, 7)
		self.addLink(h8, s4, 9, 8)

		self.addLink(s1, s2, 10, 14)
		self.addLink(s2, s3, 11, 15)
		self.addLink(s3, s4, 12, 16)
		self.addLink(s4, s1, 13, 17)

class Red2(Topo):

	def build( self ):
		h1 = self.addHost("h1", mac="00:00:00:00:00:01")
		h2 = self.addHost("h2", mac="00:00:00:00:00:02")
		h3 = self.addHost("h3", mac="00:00:00:00:00:03")
		h4 = self.addHost("h4", mac="00:00:00:00:00:04")
		h5 = self.addHost("h5", mac="00:00:00:00:00:05")
		h6 = self.addHost("h6", mac="00:00:00:00:00:06")

		s1 = self.addSwitch("s1")
		s2 = self.addSwitch("s2")
		s3 = self.addSwitch("s3")
		s4 = self.addSwitch("s4")
		s5 = self.addSwitch("s5")

		self.addLink(h1, s1, 9, 1)
		self.addLink(h2, s1, 9, 2)

		self.addLink(h3, s2, 9, 3)
		self.addLink(h4, s2, 9, 4)

		self.addLink(h5, s5, 9, 5)
		self.addLink(h6, s5, 9, 6)

		self.addLink(s1, s2, 12, 21)
		self.addLink(s2, s4, 24, 42)
		self.addLink(s3, s4, 34, 43)
		self.addLink(s1, s3, 13, 31)

		self.addLink(s3, s5, 35, 53)
		self.addLink(s1, s5, 15, 51)

topos = { "red1": (lambda: Red1()), "red2": (lambda: Red2())}

