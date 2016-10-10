########## input ########
declare -a Ns=(278 138) #number of files in each folder
declare -a starts=(1 1)
threads=2
#########################

function work_item {
    name=$1
    i=$2
    fast  -n 3 -o ${name} ${name}.nii
    gzip -d ${name}_pve_*.gz
    mv ${name}_pve_0.nii spinal_fluid/${name}.nii
    mv ${name}_pve_1.nii grey_matter/${name}.nii
    mv ${name}_pve_2.nii white_matter/${name}.nii
    echo ${type}_${i} > ../last_done.txt
    echo ${type}_${i}
}


# name of folder
iter=0
for type in train test; do
    cd set_$type
    N=${Ns[${iter}]}
    start=${starts[${iter}]}
    echo "start: ${start}"
    mkdir grey_matter
    mkdir white_matter
    mkdir spinal_fluid
    for (( i=$start; i<=$N; i++ ))
    do
	name=${type}_$i
	work_item $name $i &
	id=$[ ($i-$start+1) % $threads ]
	if [ $id -eq 0 ]; then
	    wait
	    rm *.gz
 	fi
    done
    iter=$[$iter+1]
    cd ../
done
