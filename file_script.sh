if [[ $1 == "make" ]]
then
    file_list=`ls -R | grep -P "^challenge(\d{2})\.py$"`

    for variable in $file_list
    do
        cp $variable ${variable%.*}
    done
elif [[ $1 == "fclean" ]]
then
    file_list=`ls -R | grep -P "challenge(\d{2})$"`

    for variable in $file_list
    do
        rm -rf $variable
    done
elif [[ $1 == "test" ]]
then
    export PYTHONPATH="$PWD"
    cd test
    file_list=`ls -R | grep -P "t_challenge(\d{2})\.py$"`

    for variable in $file_list
    do
        python3 -m unittest $variable
    done
    echo $index
    cd ..
else
    echo "Bad command enter."
fi