from sly import Lexer

class CalcLexer(Lexer):
	tokens = {
	    DIRECTIVE_INT, DIRECTIVE_BOOL, DIRECTIVE_WA, DIRECTIVE_EA,
	    DIRECTIVE_PFD, DIRECTIVE_PF, DIRECTORY_B, FILES_B,
		LOCATION_B, VIRTUALHOST_B, RWCOND, RWRULE, EXPIRESBYTYPE,
	    EXPIRESDEFAULT, OPTIONS, ERRORDOCUMENT,
		EXTENSION, INT, STRING, BOOL, DOMAIN, SUBDOMAIN,
		OPTIONS_VAR, ERRORS, MULTIPROC_OPTIONS, MULTIPROCESS,
		BASE_NOW, BASE_OTHER, TIME_UNIT, FILE_TYPE, ENCODING, 
		TEST_STRING, SUBSTITUTION
	}
	ignore = r' |\t'
	literals = {'{', '}', ';', '/', '@', '.', '\"', '=', '<', '>', ':'}

	def error(self,t):
		self.index += 1

	OPTIONS = r'Options'
	ERRORDOCUMENT = r'ErrorDocument'
	DIRECTIVE_INT = r'Listen|Timeout'
	DIRECTIVE_BOOL = r'KeepAlive'
	DIRECTIVE_WA = r'ServerName'
	DIRECTIVE_EA = r'ServerAdmin'
	DIRECTIVE_PFD = r'DocumentRoot'
	DIRECTIVE_PF = r'DirectoryIndex|ErrorLog'
	DIRECTORY_B = r'Directory'
	FILES_B = r'Files'
	LOCATION_B = r'Location'
	VIRTUALHOST_B = r'Virtualhost'

	RWCOND = r'RewriteCond'
	RWRULE = r'RewriteRule'
	EXPIRESBYTYPE = r'ExpiresByType'
	EXPIRESDEFAULT = r'ExpiresDefault'
	MULTIPROCESS = r'Multiprocesar'
	TEST_STRING = r'REQUEST_URI|REQUEST_FILENAME|QUERY_STRING|REMOTE_ADDR'
	OPTIONS_VAR = r'none|all|indexes|followsymlinks|execcgi'
	ERRORS = r'400|401|403|404|500|503'
	SUBSTITUTION = r'\$1'

	MULTIPROC_OPTIONS = r'prefork|worker|event'

	BASE_NOW = r'now'
	BASE_OTHER = r'access|remote'
	TIME_UNIT = r'Year|Month|Day|Hour|Minute|Second'
	FILE_TYPE = r'text|image|video'
	ENCODING = r'gif|H.264'

	BOOL = r'On|Off'
	DOMAIN = r'gmail'	# Una lista de dominios válidos (por lo pronto sólo uno)
	SUBDOMAIN = r'www'
	EXTENSION = r'html|com'
	INT = r'\d+'
	STRING = r'\w+'

# Prueba Lexer
#lexer = CalcLexer()
#text = "REQUEST_URI/REQUEST_FILENAME/QUERY_STRING/REMOTE_ADDR"
#text += "none.all}indexes{followsymlinks@execcgi"
#text += "400|401|403|404|500|503 $1"
#text += "prefork|worker|event now access|remote"
#text += "Year|Month|Day|Hour|Minute|Second"
#text += "text|image|video html|gif|H.264"
#text += "On|Off gmail html|com 1010 Final"
#if text:
#   	for token in lexer.tokenize(text):
#    		print('type=%r, value=%r' % (token.type, token.value))
