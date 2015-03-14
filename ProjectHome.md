A finite lattice is an algebraic structure in which any two elements have a unique supremum and an infimum. More info at <a href='http://en.wikipedia.org/wiki/Lattice_(order)'>the wikipedia page</a>.
There is no limitation in the element class (supports unhashable types) and a Hasse diagram can be created.
Comments of any kind are welcome.

## Usage and Example 1 ##
Given the power set of { x, y, z } partially ordered by inclusion.
![http://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Hasse_diagram_of_powerset_of_3.svg/429px-Hasse_diagram_of_powerset_of_3.svg.png](http://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Hasse_diagram_of_powerset_of_3.svg/429px-Hasse_diagram_of_powerset_of_3.svg.png)

In this case, the join and meet operation is the union and intersection between sets, respectively.
```
>>> powerset=[set(),set(['x']),set(['y']),set(['z']),set(['x','y']),set(['x','z']),set(['y','z']),set(['x','y','z'])]
>>> def intersection(a,b): return a&b 
... 
>>> def union(a,b): return a|b 
... 
```
The lattice may be defined as following.
```
>>> from lattice import Lattice
>>> L=Lattice(powerset,union,intersection)
>>> L
Lattice([set([]), set(['x']), set(['y']), set(['z']), set(['y', 'x']), set(['x', 'z']), set(['y', 'z']), set(['y', 'x', 'z'])],<function union at 0x7f41e3d4ede8>,<function intersection at 0x7f41e3d4ec08>)
```
The elements can be created by referencing the original object or by indexing in `Lattice.Uelements`. The lattice's top and bottom can be access by `Lattice.TopElement` and `Lattice.BottonElement`:
```
>>> set_with_x=L.wrap(set(['x']))
>>> set_with_x
LatticeElement(L, set(['x']))
>>> set_with_x.unwrap
set(['x'])
>>> emptyset=L.wrap(set([]))
>>> emptyset == L.BottonElement
True 
>>> L.TopElement
LatticeElement(L, set(['y', 'x', 'z']))
>>> set_with_y=L.wrap(set(['y']))
>>> set_with_yz=L.wrap(set(['y','z']))
```
The lattice elements supports the following operations:
```
>>> set_with_x | set_with_yz # join
LatticeElement(L, set(['y', 'x', 'z']))
>>> set_with_y & set_with_yz # meet
LatticeElement(L, set(['y']))
>>> set_with_x & set_with_yz == emptyset # equal 
True
>>> set_with_y <= set_with_yz #partial order relation
True
>>> set_with_x <= set_with_yz #partial order relation
False
```
To graph a Hasse diagram based on the created lattice run `Lattice.Hasse()`. This will return [graphviz code](http://www.graphviz.org/). If [scapy](http://www.secdev.org/projects/scapy/) is installed (this condition will be removed in the future), it will appear the graph.
```
>>> print L.Hasse()
digraph G {
splines="line"
rankdir=BT
"set(['y', 'x', 'z'])" [shape=box];
"set([])" [shape=box];
"set([])" -> "set(['x'])";
"set([])" -> "set(['y'])";
"set([])" -> "set(['z'])";
"set(['x'])" -> "set(['y', 'x'])";
"set(['x'])" -> "set(['x', 'z'])";
"set(['y'])" -> "set(['y', 'x'])";
"set(['y'])" -> "set(['y', 'z'])";
"set(['z'])" -> "set(['x', 'z'])";
"set(['z'])" -> "set(['y', 'z'])";
"set(['y', 'x'])" -> "set(['y', 'x', 'z'])";
"set(['x', 'z'])" -> "set(['y', 'x', 'z'])";
"set(['y', 'z'])" -> "set(['y', 'x', 'z'])";
}
```
![http://www.lucianobello.com.ar/blog/partition_lattice.png](http://www.lucianobello.com.ar/blog/partition_lattice.png)

## Example 2 ##
```
>>> from lattice import Lattice
>>> def gcd(a,b):
...     while b > 0: a,b = b, a%b 
...     return a
... 
>>> def lcm(a, b): 
...     return a*b/gcd(a,b)
... 
>>> L=Lattice([ 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 ],lcm,gcd)
>>> L.Hasse()
digraph G {
splines="line"
rankdir=BT
"60" [shape=box];
"1" [shape=box];
"1" -> "2";
"1" -> "3";
"1" -> "5";
"2" -> "4";
"2" -> "6";
"2" -> "10";
"3" -> "6";
"3" -> "15";
"4" -> "12";
"4" -> "20";
"5" -> "10";
"5" -> "15";
"6" -> "12";
"6" -> "30";
"10" -> "20";
"10" -> "30";
"12" -> "60";
"15" -> "30";
"20" -> "60";
"30" -> "60";
}
```
![http://www.lucianobello.com.ar/blog/lcm_gcd_lattice.png](http://www.lucianobello.com.ar/blog/lcm_gcd_lattice.png)