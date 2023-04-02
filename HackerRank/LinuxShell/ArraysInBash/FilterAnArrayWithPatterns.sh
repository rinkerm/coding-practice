i=0
while read -r line
do
    countries[$i]=$line
    i=$i+1
done
declare -a countries1=( ${countries[@]/*a*/} )
echo ${countries1[@]}
