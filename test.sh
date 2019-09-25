file_list=`find . * | grep -P "challenge(\d{2})\.py"`

for variable in $file_list
do
    cp $variable ${variable%.*}
done