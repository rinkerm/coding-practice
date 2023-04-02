while read -r line;
do
x=$( echo $line | cut -c 1,2,3,4 )
echo "$x"
done
