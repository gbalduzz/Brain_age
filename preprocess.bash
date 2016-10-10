#number of files in each folder
declare -a Ns=(278 138)
# name of folder
for type in train test; do
    cd set_$type
    N=${Ns[i-1]}
    mkdir grey_matter
    mkdir white_matter
    mkdir spinal_fluid
    for (( i=1; i<=$N; i++ ))
    do
	name=${type}_$i
	fast  -n 3 -o ${name} ${name}.nii 
	gzip -d *_pve_*.gz
	mv ${name}_pve_0.nii spinal_fluid/${name}.nii
	mv ${name}_pve_1.nii grey_matter/${name}.nii
	mv ${name}_pve_2.nii white_matter/${name}.nii
	rm *.gz
	echo ${type}_${i} > ../last_done.txt
	echo ${type}_${i}
    done
    cd ../
done
