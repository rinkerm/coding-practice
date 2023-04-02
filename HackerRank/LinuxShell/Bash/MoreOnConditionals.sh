read x
read y
read z

if [ $x == $y ] && [ $x == $z ];
then
    echo 'EQUILATERAL'
else
    if [ $x == $y ] || [ $y == $z ] || [ $x == $z ];
    then
        echo 'ISOSCELES'
    else
        echo 'SCALENE'
    fi
fi

