# transative_pref

Programme take set of options and presents user with every pair of options. The user then says which option they prefer or if they are indifferent.

The output is three graphs:

Graph 1: shows if there are any preference cycles based on strict preference orderings. 
i.e A > B > C > A

Graph 2: shows if there are any strict preference orderings between nodes that are in the same indifference set
i.e A∼B∼C but A > C

Graph 3: shows if there are any preference cycles between indifference sets
i.e A∼B and C∼D but A>C and D>B


