# transative_pref

This programme takes a set of options and gets the user to choose their preferred option out of all pairs. 
The programme looks to see if there are any strongly connected components which would indicate a preference cycle. 

The output is a directed graph and for each set of strongly connected components one of the cycles that links them
will be displayed in a different colour.

Issues:
Basically the idea was to have a similar output to https://demonstrations.wolfram.com/EnumeratingCyclesOfADirectedGraph/

Verifying if a directed graph is cyclic is very efficient but finding a labeled path is less easy. The best way I have found 
is using Johnson's algorithm but I have not been able to code it yet. 

Instead what I use works fine for small sets of preferences as I use a very inefficient permutation of edge combinations. Once 
you start having preference cycles with > 6 nodes it can take a long time to complete.


