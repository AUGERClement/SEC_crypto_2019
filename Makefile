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
	sh test.sh

clean:
	rm -rf __pycache__/

fclean:	clean
	rm challenge0[0-9]
	rm test/t_challenge0[09]

re:		fclean all

.PHONY:	all clean fclean re