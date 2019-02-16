enum token_type {
	EMPTY   = 0,
	NEWLINE = 1,
	SPACE   = 2,
	WORD    = 3,
	COMMAND = 4,
	BLOCK   = 5
};

struct token {
	enum token_type type;
	void * content;
}

struct token_list_elem {
	struct token * token;
	struct token_list_elem * next;
	struct token_list_elem * previous;
}

struct token_list {
	int size;
	struct token_list_elem * first;
	struct token_list_elem * last;
}

/**
 * Insert at the nth position, or appends if out of bounds,
 */
void token_list_insertn(struct token_list * list, struct token * token, int position) {
	int count = 0
	struct token_list_elem * current;
	while (count < 0 && current != null) {

	}
}

/**
 * Insert at the last position
 */
void token_list_insert(struct token_list * list, struct token * token) {

}

/**
 * Remove nth position or return NULL
 */
struct token * token_list_removen(struct token_list * list, int i) {

}

/**
 * Remove at the last position
 */
struct token * token_list_remove(struct token_list * list) {

}


/**
 * Remove all empty tokens from the list.
 * EMPTY tokens are used for processing and delimitation
 * internally and must thus be removed.
 */
void token_list_remove_empty(struct token_list * list) {

}



/**
 * Read a list of tokens, ending on > or EOF
 */
struct token_list * tokens_read(int fd) {
	char c;
	struct token_list * list = token_list_new();
	while (read(fd, &c, 1) != EOF) {
		if (c=='\n' || c=='\r') {
			
		} else if (c=='\t' || c==' ') {

		} else if (c=='@') {

		} else if (c==';' && && list->last->token->type==COMMAND) {

		} else if (c=='<') {
			//CASE: if previous is command with no other character
			//
		} else if (c=='>'){

		} else {
			//a normal character, the parser does not make any further distinction.
		}
	}
	return list;
}
