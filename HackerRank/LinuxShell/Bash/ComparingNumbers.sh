read x
read y
if (($x > $y));
then
    echo "X is greater than Y"
else
    if (($y>$x));
    then
        echo "X is less than Y"
    else
        echo "X is equal to Y"
    fi
fi
