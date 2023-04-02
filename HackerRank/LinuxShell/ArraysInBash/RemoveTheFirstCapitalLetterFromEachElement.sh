i=0
while read line || [ -n "$line" ]
do
    countries[$i]=$line
    i=$(($i+1))
done
countries1=${countries[@]/[A-Z]/.}
echo ${countries1[@]}
