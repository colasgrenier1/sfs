/**
 * Parser code file.
 */

/*
 * Parse tokens are individual elements.
 *
 */

enum parse_token_type {
	NEWLINE   = 0,
	SPACE     = 1,
	ATSIGN    = 2,
	SEMICOLON = 3,
	LBRACK    = 4,
	RBRACK    = 5,
	CHARACTER = 6
};

struct parse_token {
	enum token_type type;
	char value;
};

struct parse_token * parse_token_new(enum parse_token_type type, char * value) {
	struct parse_token * pt = malloc(sizeof(struct parse_token));
	pt->type = type;
	pt->value = value;
	return pt;
}

struct parse_token * parse_token_read(int fd) {
	char c;
	if (read(fd, &c, 1) != EOF) {
		switch(c) {
			case '\n':
				return parse_token_new(NEWLINE, c);
			case '\r':
				return parse_token_new(NEWLINE, c);
			case '\t':
				return parse_token_new(SPACE, c);
			case ' ':
				return parse_token_new(SPACE, c);
			case '@':
				return parse_token_new(ATSIGN, c);
			case ';':
				return parse_token_new(SEMICOLON, c);
			case '<':
				return parse_token_new(LBRACK, c);
			case '>':
				return parse_token_new(RBRACK, c);
			default:
				return parse_token_new(CHARACTER, c);
		}
	} else {
		return null;
	}
};


/*
 * Tokens are actual wholes
 *
 */

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
	char * value;
};

struct token_stack_elem {
	struct token * token;
	struct token * bottom;
}

struct token_stack {
	struct token_stack_elem * top;
}

void token_stack_push (struct token_stack * stack, struct token * tok) {
	struct token_stack_elem * tse = malloc(sizeof(struct token_stack_elem));
	tse->token = tok;
	tse->bottom = stack->bottom;
}

struct token * token_stack_peek (struct token_stack * stack) {
	if (stack->top != NULL) {
		return stack->top->token;
	} else {
		return null;
	}
}

struct token * token_stack_pop (struct token_stack * stack) {
	struct token * t = token_stack_peek(stack);
	if (stack->top != null) {
		struct token_stack_elem * curtop = stack->top;
		stack->top = stack->top->bottom;
		free(curtop);
	}
	return t;
}

/**
 * Reads a whole file and returns a list of tokens.
 */
struct token * token_read(FILE * f) {

}
