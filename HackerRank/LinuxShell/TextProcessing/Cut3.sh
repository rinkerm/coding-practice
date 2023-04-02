while read -r line;
do
x=$( echo $line | cut -c 2,3,4,5,6,7 )
echo "$x"
done
