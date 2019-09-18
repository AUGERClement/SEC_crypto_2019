##
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
## Makefile
##

DEBUG=yes
CC=			gcc
ifeq ($(DEBUG), yes)
	CFLAGS+=	-W -Wall -Werror -g3
	LDFLAGS+=	-lcrypto
else
	CFLAGS+=	-W -Wall -Werror
	LDFLAGS+=	-lcrypto
endif

SRC=	challenge01.c

OBJ=	$(SRC:.c=.o)

NAME=	challenge01

## ALL RULES ##

all:	$(NAME)
ifeq ($(DEBUG), yes)
	@echo "Generation en mode debug"
endif

$(NAME):	$(OBJ)
		$(CC) -o $@ $(OBJ) $(LDFLAGS)

clean:
		rm -rf $(OBJ)

fclean:	clean
		rm -rf $(NAME)

re:		fclean all

.PHONY:	all clean fclean re