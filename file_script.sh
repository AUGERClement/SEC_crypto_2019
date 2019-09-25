if [[ $1 == "make" ]]
then
    file_list=`find . * | grep -P "^challenge(\d{2})\.py$"`

    for variable in $file_list
    do
        cp $variable ${variable%.*}
    done
elif [[ $1 == "fclean" ]]
then
    file_list=`find . * | grep -P "challenge(\d{2})$"`

    for variable in $file_list
    do
        rm -rf $variable
    done
elif [[ $1 == "test" ]]
then
    file_list=`find . * | grep -P "t_challenge(\d{2})\.py$"`

    for variable in $file_list
    do
         python3 -m unittest $variable
    done
else
    echo "Bad command enter."
fi