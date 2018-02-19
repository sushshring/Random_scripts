#!/bin/bash
echo "" > data.csv
echo "benchnum, branchnum, inst_execution, CPI, b_misses, n_inst" >> data.csv
BENUM=0
BRNUM=0
INEXC="inorder"
for i in $(ls); do
	if [[ $i == *.simout ]]
	then
		if [[ $i == *.inorder.simout ]]
		then
			INEXC="inorder"
		else
			INEXC="outorder"
		fi
		CPI=$(cat $i | grep sim_CPI | awk '{print $2}')
		BMISS=$(cat $i | grep bpred_comb.misses)
		if [[ $? -eq 1 ]]
		then
			BMISS=0
		else
			BMISS=$(echo $BMISS | awk '{print $2}')
		fi
		NINST=$(cat $i | grep sim_num_insn | awk '{print $2}')
		echo "$BENUM,$BRNUM,$INEXC,$CPI,$BMISS,$NINST" >> data.csv
		if [[ $BRNUM -eq 5 && $i == *.outorder.simout ]]
		then
			BRNUM=0
			((BENUM+=1))
		elif [[ $i == *.outorder.simout ]]
		then
			((BRNUM+=1))
		fi
	fi
done
