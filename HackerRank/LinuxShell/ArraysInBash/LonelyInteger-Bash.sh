x= read x
arr= read arr 
(echo ${arr[@]}) | tr ' ' '\n' | sort | uniq -u
