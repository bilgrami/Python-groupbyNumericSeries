# Python-groupbyNumericSeries

This repo should help me classify a numeric series into groups.

---
I use syntax below to explain some of the behavior.

```python
import calc_groupby as grp_m
grp_o = grp_m.calc_groupby();
```
### Scenario 0
```python
    my_l = [] # Find all groups in this list
    gc_i = 44 # I want 44 groups
    my_d = grp_o.calc_groupby(my_l, gc_i)
```    
my_d returns an AssertionError excpetion, with following message
"Parameter [Desired Group Count] cannot be more than number of list elements"

### Scenario 1
```python
    my_l = [0,1]
    gc_i = 1 # I want 1 group
    
    my_d = grp_o.calc_groupby(my_l, gc_i)
```    
my_d should now be {0: [0,1]}

### Scenario 2
```python
    my_l = [0,1]
    gc_i = 2 # I want 2 groups
    
    my_d = grp_o.calc_groupby(my_l, gc_i)
```    
my_d should now be {0: [0], 1:[1]}
    
    
### Scenario 3
```python
    my_l = [0,1,2,22,23,44,46,4,24]
    
    gc_i = 3 # I want 3 groups
    
    my_d = grp_o.calc_groupby(my_l, gc_i)
```    
my_d should now be {0: [0,1,2,4], 1:[22,23,24], 2:[44,46]}

---
## run.py: 
Execute ./run.py to see following output
![Image of Sample run](https://raw.githubusercontent.com/bilgrami/Python-groupbyNumericSeries/master/docs/run_result.JPG)

