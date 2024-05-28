from sly import Lexer

class CalcLexer(Lexer):
	tokens = {
		OPEN_BRACKET, CLOSE_BRACKET, SEMICOLON, EXTENSION, AT, DOT, INT, CADENA, BOOL, QUOTES, DOMAIN,
		OPTIONS_VAR, ERRORS, MULTIPROC_OPTIONS, 
		BASE_NOW, BASE_OTHER, TIME_UNIT, FILE_TYPE, ENCODING, 
		TEST_STRING, PATTERN, SUBSTITUTION, CP_BASIC_AUX, CP_CIERRES, CP_CHAR
	}

	ignore = r' |\t'

	OPEN_BRACKET = '{'
	CLOSE_BRACKET = '}'
	SEMICOLON = ';'
	EXTENSION = r'html|com'

	AT = '@'
	DOT = '.'
	INT = r'\d+'
	CADENA = r'\w+'
	BOOL = r'On|Off'
	QUOTES = '"'
	DOMAIN = r'gmail'	# Una lista de dominios válidos (por lo pronto sólo uno)

	OPTIONS_VAR = r'none|all|indexes|followsymlinks|execcgi'
	ERRORS = r'400|401|403|404|500|503'

	MULTIPROC_OPTIONS = r'prefork|worker|event'

	BASE_NOW = 'now'
	BASE_OTHER = r'access|remote'
	TIME_UNIT = r'Year|Month|Day|Hour|Minute|Second'
	FILE_TYPE = r'text|image|video'
	ENCODING = r'html|gif|H.264'

	TEST_STRING = r'REQUEST_URI|REQUEST_FILENAME|QUERY_STRING|REMOTE_ADDR'
	PATTERN = '.\'(\'.\')\'.*'
	SUBSTITUTION = '$1'

#	Una gramática para el CP
	CP_BASIC_AUX = r'\.'
	CP_CIERRES = r'\*|\+'
	CP_CHAR = r'\^|\$|\.|\\|\!|\*|\+'

lexer = CalcLexer()
