from sly import Lexer

class CalcLexer(Lexer):
	tokens = {
		OPEN_BRACKET, CLOSE_BRACKET, SEMICOLON, EXTENSION, AT, DOT, INT, CADENA, BOOL, QUOTES, DOMAIN,
		OPTIONS_VAR, ERRORS, MULTIPROC_OPTIONS, 
		BASE_NOW, BASE_OTHER, TIME_UNIT, FILE_TYPE, ENCODING, 
		TEST_STRING, PATTERN, SUBSTITUTION, CP_BASIC_AUX, CP_CIERRES, CP_CHAR
	}

	ignore = r' |\t'

	@_('{')
	def OPEN_BRACKET(self,t):
		print("Regla aplicada: OPEN_BRACKET = '{'")

	@_('}')
	def CLOSE_BRACKET(self,t):
		print("Regla aplicada: CLOSE_BRACKET = '}'")

	@_(';')
	def SEMICOLON(self,t):
		print("Regla aplicada: SEMICOLON = ';'")

	@_(r'html|com')
	def EXTENSION(self,t):
		print("Regla aplicada: EXTENSION = r'html|com'")

	@_('@')
	def AT(self,t):
		print("Regla aplicada: AT = '@'")

	@_(r'\d+')
	def INT(self,t):
		print("Regla aplicada: INT = r'\\d+'")

	@_(r'\w+')
	def CADENA(self,t):
		print("Regla aplicada: CADENA = r'\\w+'")

	@_(r'On|Off')
	def BOOL(self,t):
		print("Regla aplicada: BOOL = r'On|Off'")

	@_('"')
	def QUOTES(self,t):
		print("Regla aplicada: QUOTES = '\"'")

	@_('gmail')
	def DOMAIN(self,t):
		print("Regla aplicada: DOMAIN = 'gmail'")

	@_(r'none|all|indexes|followsymlinks|execcgi')
	def OPTIONS_VAR(self,t):
		print("Regla aplicada: OPTIONS_VAR = r'none|all|indexes|followsymlinks|execcgi'")

	@_(r'400|401|403|404|500|503')
	def ERRORS(self,t):
		print("Regla aplicada: ERRORS = r'400|401|403|404|500|503'")

	@_(r'prefork|worker|event')
	def MULTIPROC_OPTIONS(self,t):
		print("Regla aplicada: MULTIPROC_OPTIONS = r'prefork|worker|event'")

	@_('now')
	def BASE_NOW(self,t):
		print("Regla aplicada: BASE_NOW = 'now'")
		
	@_(r'access|remote')
	def BASE_OTHER(self,t):
		print("Regla aplicada: BASE_OTHER = r'access|remote'")
		
	@_(r'Year|Month|Day|Hour|Minute|Second')
	def TIME_UNIT(self,t):
		print("Regla aplicada: TIME_UNIT = r'Year|Month|Day|Hour|Minute|Second'")
		
	@_(r'text|image|video')
	def FILE_TYPE(self,t):
		print("Regla aplicada: FILE_TYPE = r'text|image|video'")
		
	@_(r'html|gif|H.264')
	def ENCODING(self,t):
		print("Regla aplicada: ENCODING = r'html|gif|H.264'")
		
	@_(r'REQUEST_URI|REQUEST_FILENAME|QUERY_STRING|REMOTE_ADDR')
	def TEST_STRING(self,t):
		print("Regla aplicada: TEST_STRING = r'REQUEST_URI|REQUEST_FILENAME|QUERY_STRING|REMOTE_ADDR'")
		
	@_('.\'(\'.\')\'.*')
	def PATTERN(self,t):
		print("Regla aplicada: PATTERN = '.\\'(\\'.\\')\\'.*'")
		
	@_('$1')
	def SUBSTITUTION(self,t):
		print("Regla aplicada: SUBSTITUTION = '$1'")
	
	@_(r'\.')
	def CP_BASIC_AUX(self,t):
		print("Regla Aplicada: CP_BASIC_AUX = r'\\.'")

	@_(r'\*|\+')
	def CP_CIERRES(self,t):
		print("Regla Aplicada: CP_CIERRES = r'\\*|\\+'")

	@_(r'\^|\$|\.|\\|\!|\*|\+')
	def CP_CHAR(self,t):
		print("Regla Aplicada: CP_CHAR = r'\\^|\\$\|\.|\\\\|\\!|\\*|\\+'")
		

lexer = CalcLexer()