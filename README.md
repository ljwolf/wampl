**W**es **A**nderson **M**at**P**lot**L**ib Palettes
====================================================================
aka `wes`
----------

[![Build Status](https://travis-ci.org/ljwolf/wampl.svg?branch=master)](https://travis-ci.org/ljwolf/wampl)

This is another [Wes Anderson Palettes](http://wesandersonpalettes.tumblr.com/)
implementation. Currnetly, if you set your default pallete, it just modifies the
default color cycle to the one provided by the blog. I don't make any
classification or useage inferences, unlike jiffyclub's fantastic 
[palettable](https://github.com/jiffyclub/palettable). 

Check out the [demo notebook](http://nbviewer.ipython.org/github/ljwolf/wampl/blob/master/demo.ipynb) for more information.

Usage
-----

It's about as easy as:
```
import wes
wes.set_palette('Rushmore')
```
and then your future plots will use the `Rushmore` palette. If you'd like to
reset your palette, use 

```
import matplotlib
matplotlib.rcdefaults()
```
Otherwise, you can show all palettes available using `wes.available()` and can
plot two palettes against each other using `wes.plot_palettes(*args)`. 

You can also use this with
[seaborn](http://stanford.edu/~mwaskom/software/seaborn/). Just remember to set
your palette **after** importing seaborn, as seaborn overwrites matplotlib's
[`rcdefaults`](http://matplotlib.org/users/customizing.html)

License
--------

This is licensed in the Creative Commons for Attribution and ShareAlike
purposes. 
CC-BY-SA
