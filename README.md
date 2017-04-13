# Example code for Enflux

## Requirements
python3.4+

## Usage
`python3 list_diffs.py`

`python3 analyze.py`

`python3 big.py` (to generate a big csv)

The social network approach involves pushing accumulated values up the tree, since that's the way the referential links actually point. Doing so has the need to process all children of a node before the node itself, hence the sorting. Walking down the tree isn't straightforward since it's inverted, but there are a million ways to do it. Performance could be improved if the csv were guaranteed to be in the desired order.

Given the relative simplicity of the problems, python oop isn't directly demonstrated, but I'd be happy to provide an approach that does so. 

I was interested in the performance of my approach to the network problem so I wrote a script to populate a csv with a million values (which isn't BIG big, but big enough.) 

Some results on the 16M csv:

`$ time python3 analyze.py`

```
real	0m6.126s
user	0m4.640s
sys	0m0.280s
```