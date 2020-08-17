# transative_pref

Takes a set of options and presents user with every pair of options. The user then says which option they prefer or if they are indifferent.

The output is three graphs:

Graph 1: shows if there are any preference cycles based on strict preference orderings. 
i.e A > B > C > A
<img src="https://github.com/neilhacker/transative_pref/blob/master/ExampleGraphs/Graph1.png" alt="drawing" width="400"/>

Graph 2: shows if there are any strict preference orderings between nodes that are in the same indifference set
i.e A∼B∼C but A > C

<img src="https://github.com/neilhacker/transative_pref/blob/master/ExampleGraphs/Graph2.png" alt="drawing" width="400"/>

Graph 3: shows if there are any preference cycles between indifference sets
i.e A∼B and C∼D but A>C and D>B
<img src="https://github.com/neilhacker/transative_pref/blob/master/ExampleGraphs/Graph3.png" alt="drawing" width="400"/>



