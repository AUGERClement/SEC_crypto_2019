##
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
## Makefile
##

# SRC=	challenge01.py	\
# 		challenge02.py

# OBJ=	($(SRC):challenge%.py=challenge%)

challenge%:challenge%.py
		cp $< $@

challenge%.o:challenge%.c
		gcc $< -o:$@

all:
	sh file_script.sh make

clean:
	rm -rf __pycache__/

fclean:	clean
	sh file_script.sh fclean

re:		fclean all

test:
	sh file_script.sh test

.PHONY:	all clean fclean re test