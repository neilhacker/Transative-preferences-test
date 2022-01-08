# Transative preference tester

One of the main axioms of traditional economics is that people have transative preferences. If you prefer A to B and B to C then we can infer you should prefer A to C. If this is not the case then it can lead to lots of strange behaviour and some apparent paradoxes. It turns out that unless you have really strong feelings about a group of things it can actually be pretty hard to have a self consistent set of transative preferences. 

This is a little program to let you test you/friends to see if you can be consistent. You can feed in a list of options into the options array (https://github.com/neilhacker/transative_pref/blob/79e2d9d2a233d9e0714d0f9a52fbdf0864830409/transitive_pref.py#L14). 

You will then be presented with every pairwise comparison, this grows in proportion to number_options² so will get long quickly. For each comparison you can then enter:
* 1: you prefer the first option
* 2: you prefer the second option
* 0: you are indifferent

Once you have done this up to 3 graphs will be outputted. Each graph shows a certain type of violation of transative preferences. Each graph will only display one violation even if there are more of that type of violation as otherwise things get a bit cluttered. 

Graph 1: shows if there are any preference cycles based on strict preference orderings. 
i.e A > B > C > A
<img src="https://github.com/neilhacker/transative_pref/blob/master/ExampleGraphs/Graph1.png" alt="drawing" width="400"/>

Graph 2: shows if there are any strict preference orderings between nodes that are in the same indifference set
i.e A∼B∼C but A > C

<img src="https://github.com/neilhacker/transative_pref/blob/master/ExampleGraphs/Graph2.png" alt="drawing" width="400"/>

Graph 3: shows if there are any preference cycles between indifference sets
i.e A∼B and C∼D but A>C and D>B
<img src="https://github.com/neilhacker/transative_pref/blob/master/ExampleGraphs/Graph3.png" alt="drawing" width="400"/>



