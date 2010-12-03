class Lattice:
    def __init__(self, Uelements,join_func,meet_func):
        '''Create a lattice:

        Keyword arguments:
        Uelements -- list. The lattice set.
        join_func  -- join function that operates to elements and returns the greatest element.
        meet_func  -- meet function that operates to elements and returns the least element.

        Returns a lattice instance.
        '''
        self.Uelements = Uelements
        self.join=join_func
        self.meet=meet_func

    def wrap(self,object):
        '''Wraps an object as a lattice element:

        Keyword argument:
        object -- any item from the lattice set.
        '''
        return LatticeElement(self,object)

    def WElementByIndex(self,ElementIndex):
        return LatticeElement(self,self.Uelements[ElementIndex])

    @property
    def TopElement(self):
        top=self.wrap(self.Uelements[0])
        for element in self.Uelements[1:]:
            top |= self.wrap(element)
        return top

    @property
    def BottonElement(self):
        botton=self.wrap(self.Uelements[0])
        for element in self.Uelements[1:]:
            botton &= self.wrap(element)
        return botton

    def Hasse(self):
        graph=dict()
        for indexS,elementS in enumerate(self.Uelements):
            graph[indexS]=[]
            for indexD,elementD in enumerate(self.Uelements):
                if self.wrap(elementS) <= self.wrap(elementD):
                    if not bool( sum([ int(self.WElementByIndex(x) <= self.wrap(elementD)) for x in graph[indexS]])) and not elementS==elementD:
                        graph[indexS]+=[indexD]
        dotcode='digraph G {\nsplines="line"\nrankdir=BT\n'
        dotcode+='\"'+str(self.TopElement.unwrap)+'\" [shape=box];\n'
        dotcode+='\"'+str(self.BottonElement.unwrap)+'\" [shape=box];\n'
        for s, ds in graph.iteritems():
            for d in ds:
                dotcode += "\""+str(self.WElementByIndex(s))+"\""
                dotcode += " -> "
                dotcode += "\""+str(self.WElementByIndex(d))+"\""
                dotcode += ";\n"
        dotcode += "}"
        try:
            from scapy.all import do_graph
            do_graph(dotcode)
        except:
            pass
        return dotcode

    def __repr__(self):
        """Represents the lattice as an instance of Lattice."""
        return 'Lattice(%s,%s,%s)' % (self.Uelements,self.join,self.meet)

class LatticeElement:
    def __init__(self, lattice, Uelement):
        if Uelement not in lattice.Uelements: raise ValueError('The given value is not a lattice element')
        self.lattice=lattice
        self.ElementIndex=lattice.Uelements.index(Uelement)

    @property
    def unwrap(self):
        return self.lattice.Uelements[self.ElementIndex]

    def __str__(self):
        return str(self.unwrap)

    def __repr__(self):
        """Represents the lattice element as an instance of LatticeElement."""
        return "LatticeElement(L, %s)" % str(self)

    def __and__(self,b):
        # a.__and__(b) <=> a & b <=> meet(a,b)
        return LatticeElement(self.lattice,self.lattice.meet(self.unwrap,b.unwrap))

    def __or__(self,b):
        # a.__or__(b) <=> a | b <=> join(a,b)
        return LatticeElement(self.lattice,self.lattice.join(self.unwrap,b.unwrap))

    def __eq__(self,b):
        # a.__eq__(b) <=> a = b <=> join(a,b)
        return self.unwrap==b.unwrap

    def __le__(self,b):
        # a <= b if and only if a = a & b,
        # or
        # a <= b if and only if b = a | b,
        a=self
        return ( a == a & b ) or ( b == a | b )
