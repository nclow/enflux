# Example code for Enflux

## Requirements
python3.4+

## Usage
`python3 list_diffs.py`

`python3 analyze.py`

`python3 big.py` (to generate a big csv)

I was interested in the performance of my approach to the network problem so I wrote a script to populate a csv with a million values (which isn't BIG big, but big enough.) 

Some results on the 16M csv:

`$ time python3 analyze.py`

```
real	0m6.126s
user	0m4.640s
sys	0m0.280s
```