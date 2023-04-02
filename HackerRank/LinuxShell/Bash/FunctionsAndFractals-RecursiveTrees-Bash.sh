read n
let start_pos=49
let freespace=63
let  j=0
while ((j<n)); 
do
    exp=$((2**$j))
    space=$((32/$exp))
    freespace=$(($freespace-$space))
    let j++
done
line="____________________________________________________________________________________________________"
while ((freespace>0));
do
    echo $line
    let freespace--
done
let t=$n
while ((t>0));
do
    let noBranches=2**t
    let noTrunks=noBranches/2
    let height=32/noBranches
    let spacing=(2*height)-1
    let width=(-1*spacing+noBranches*spacing)+noBranches
    let branch_row=height
    let trunk_space=spacing
    while((branch_row>0))
    do
    
          
         thisline="____________________________________________________________________________________________________"
        let b=1
        let leftwidth=width-1
        let leftwidth=leftwidth/2
        let pos=50-leftwidth
        while((b<=noBranches/2))
        do
            thisline=$(echo $thisline | sed "s/./1/$pos")
            let pos=$pos+$spacing+1
            let b++
            thisline=$(echo $thisline | sed "s/./1/$pos")
            let pos=$pos+$trunk_space+1
        done   
        echo $thisline
        let branch_row--
        let width=width-2
        let spacing=spacing-2
        let trunk_space=trunk_space+2
    done
    let trunk_row=height
    let spacing=spacing+2
    
    while((trunk_row>0))  
    do  
    let nt=1
    let pos=50-leftwidth+1
    thisline="____________________________________________________________________________________________________"
        while((nt<=noTrunks))
        do
            thisline=$(echo $thisline | sed "s/./1/$pos")
            let nt++
            let pos=pos+trunk_space+1
        done   
        
        echo $thisline
        let trunk_row--
    done
    let t--
done
