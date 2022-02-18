run.py search in calculation only closer to `pi pi*pi or pi**1/2` values.
run.py only polished enough.
Later , using html generator is possible to test matrices with best result indices, using maxima runme.wxm file and batchStuff.txt , generated using html miniapp. Generated numbers of html matrices same as matrices numbers in python code.

not use this, not polished finally.
runfull.py print each group of results of matrices calculation in files.

Trying to make python checker and printer fail, code very muddy, and just trunscoded from javascript html generator to be similar/comparable with wxmaxima stuff.

2x2 completed

3x3 completed

now added 60 sec limit per matrix, because at last of 4x4, very long calc, more than 10 hours not enough, for some matrices

2022-2-12
4x4 in process
run4.py executed using amazon EC2 with filtering "bad" matrix, which calculation can't be completed per two minutes. 14000+ matrices collected as bad. rf4.zip include result of EC2 calculations with filtering "bad"matrices.

2022-2-18
4x4 Next recalculation (from last correct point "globalCounter.txt -> 1564500") without filtering "bad" matrices will be executed later.
4x4 Founded some potential hole in code. Code fixed, will be first executed 5x5 flow using aws

5x5 in process using aws without filtering by calculation time, because 4x4 was completed correct.
Matrices number is 3162510.
Used script `run.py` on aws

`run4.py` `run3.py` `run2.py` code changed to
`run.py` `mp.py` `ms.py` `mg.py` new flow
