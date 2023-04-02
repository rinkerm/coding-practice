i=0
while read line || [ -n "$line" ]
do
    countries[$i]=$line
    i=$i+1
done
countries1=( "${countries[@]}" "${countries[@]}" "${countries[@]}" )
echo ${countries1[@]}
