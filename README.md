# Python-groupbyNumericSeries

This repo should help me classify a numeric series into groups.

I use syntax below to explain some of the behavior.

    # Scenario 0
    my_l = [] # Find all groups in this list
    gc_i = 44 # I want 44 groups
    
    my_d = calc_groupby(my_l, gc_i)
    
    # my_d should now be None
    
    # Scenario 1
    my_l = [0,1]
    gc_i = 1 # I want 1 group
    
    my_d = calc_groupby(my_l, gc_i)
    
    # my_d should now be {0: [0,1]}
    
    
    # Scenario 2
    my_l = [0,1]
    gc_i = 2 # I want 2 groups
    
    my_d = calc_groupby(my_l, gc_i)
    
    # my_d should now be {0: [0], 1:[1]}
    
    
    # Scenario 3
    my_l = [0,1,2,22,23,44,46,4,24]
    
    gc_i = 2 # I want 3 groups
    
    my_d = calc_groupby(my_l, gc_i)
    
    # my_d should now be {0: [0,1,2,4], 1:[22,23,24], 2:[44,46]}

