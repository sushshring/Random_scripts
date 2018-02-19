#!/bin/bash
echo "" > data.csv
echo "filename, CPI, b_misses, n_inst" >> data.csv
for i in $(ls); do
    if [[ $i == *.simout ]]
    then
        CPI=$(cat $i | grep sim_CPI | awk '{print $2}')
        BMISS=$(cat $i | grep bpred_comb.misses)
        if [ $? -eq 1 ]
        then
            BMISS=0
        else
            BMISS=$(echo $BMISS | awk '{print $2}')
        fi
        NINST=$(cat $i | grep sim_num_insn | awk '{print $2}')
        echo "$i,$CPI,$BMISS,$NINST" >> data.csv
    fi
done

