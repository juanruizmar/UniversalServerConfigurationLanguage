from sly import Lexer

class CalcLexer(Lexer):
	tokens = {
		EXTENSION, INT, STRING, BOOL, DOMAIN,
		OPTIONS_VAR, ERRORS, MULTIPROC_OPTIONS, 
		BASE_NOW, BASE_OTHER, TIME_UNIT, FILE_TYPE, ENCODING, 
		TEST_STRING, PATTERN, SUBSTITUTION
	}
	ignore = r' |\t'
	literals = {'{', '}', ';', '/', '@', '.', '\"', '='}

	TEST_STRING = r'REQUEST_URI|REQUEST_FILENAME|QUERY_STRING|REMOTE_ADDR'
	OPTIONS_VAR = r'none|all|indexes|followsymlinks|execcgi'
	ERRORS = r'400|401|403|404|500|503'
	SUBSTITUTION = r'\$1'

	MULTIPROC_OPTIONS = r'prefork|worker|event'

	BASE_NOW = r'now'
	BASE_OTHER = r'access|remote'
	TIME_UNIT = r'Year|Month|Day|Hour|Minute|Second'
	FILE_TYPE = r'text|image|video'
	ENCODING = r'html|gif|H.264'

	BOOL = r'On|Off'
	DOMAIN = r'gmail'	# Una lista de dominios válidos (por lo pronto sólo uno)
	EXTENSION = r'html|com'
	INT = r'\d+'
	STRING = r'\w+'

	#No funciona Pattern
	#PATTERN = '.\'(\'.\')\'.*'

lexer = CalcLexer()
text = "REQUEST_URI/REQUEST_FILENAME/QUERY_STRING/REMOTE_ADDR"
text += "none.all}indexes{followsymlinks@execcgi"
text += "400|401|403|404|500|503 $1"
text += "prefork|worker|event now access|remote"
text += "Year|Month|Day|Hour|Minute|Second"
text += "text|image|video html|gif|H.264"
text += "On|Off gmail html|com 1010 Final"
if text:
   	for token in lexer.tokenize(text):
    		print('type=%r, value=%r' % (token.type, token.value))
