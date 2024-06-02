from sly import Parser
from CalcLexer import CalcLexer


class CalcParser(Parser):
    tokens = CalcLexer.tokens

    @_('statement_list')
    def program(self, p):
        return ('program', p.statement_list)

    @_('statement statement_list')
    def statement_list(self, p):
        return [p.statement] + p.statement_list

    @_('statement')
    def statement_list(self, p):
        return [p.statement]

    # Define las reglas para diferentes tipos de declaraciones
    @_('directive')
    def statement(self, p):
        return p.directive

    @_('multiprocessing')
    def statement(self, p):
        return p.multiprocessing

    @_('expires')
    def statement(self, p):
        return p.expires

    @_('sobreescritura')
    def statement(self, p):
        return p.sobreescritura

    @_('directiva_bloque')
    def statement(self, p):
        return p.directiva_bloque

    @_('virtualhost')
    def statement(self, p):
        return p.virtualhost

    # Reglas para directivas
    @_('DirectiveName EQUALS String SEMICOLON')
    def directive(self, p):
        return ('directive', p.DirectiveName, p.String)

    # Reglas para módulo de multiprocessing
    @_('OPEN_BRACKET ProcessType INT CLOSE_BRACKET')
    def multiprocessing(self, p):
        return ('multiprocessing', p.ProcessType, p.INT)

    @_('OPEN_BRACKET MaxClients INT CLOSE_BRACKET')
    def multiprocessing(self, p):
        return ('multiprocessing', p.MaxClients, p.INT)

    # Reglas para módulo expires
    @_('ExpiresByType FileType Dash Encoding ExpiresBody')
    def expires(self, p):
        return ('expires', p.ExpiresByType, p.FileType, p.Dash, p.Encoding, p.ExpiresBody)

    @_('ExpiresDefault ExpiresBody')
    def expires(self, p):
        return ('expires', p.ExpiresDefault, p.ExpiresBody)

    @_('Quotes Base Quote')
    def ExpiresBody(self, p):
        return ('expires_body', p.Base)

    @_('BaseNow')
    def Base(self, p):
        return ('base_now', p.BaseNow)

    @_('BaseOther TimePeriod')
    def Base(self, p):
        return ('base_other', p.BaseOther, p.TimePeriod)

    @_('INT TimeUnit')
    def TimePeriod(self, p):
        return ('time_period', p.INT, p.TimeUnit)

    @_('INT TimeUnit TimePeriod')
    def TimePeriod(self, p):
        return ('time_period', p.INT, p.TimeUnit, p.TimePeriod)

    # Reglas para módulo sobreescritura
    @_('RewriteCond Sobreescritura')
    def sobreescritura(self, p):
        return ('sobreescritura', p.RewriteCond, p.Sobreescritura)

    @_('RewriteCond')
    def sobreescritura(self, p):
        return ('sobreescritura', p.RewriteCond)

    @_('RewriteCond TestString CondPattern RewriteCond')
    def RewriteCond(self, p):
        return ('rewrite_cond', p.TestString, p.CondPattern, p.RewriteCond)

    @_('RewriteCond TestString CondPattern RewriteRule')
    def RewriteCond(self, p):
        return ('rewrite_cond', p.TestString, p.CondPattern, p.RewriteRule)

    @_('RewriteRule Pattern Substitution')
    def RewriteRule(self, p):
        return ('rewrite_rule', p.Pattern, p.Substitution)

    @_('RewriteRule Pattern Substitution RewriteRule')
    def RewriteRule(self, p):
        return ('rewrite_rule', p.Pattern, p.Substitution, p.RewriteRule)

    @_('RewriteRule Pattern Substitution RewriteCond')
    def RewriteRule(self, p):
        return ('rewrite_rule', p.Pattern, p.Substitution, p.RewriteCond)

    # Reglas para directiva de bloques
    @_('"<Directory" PathFolder ">" StatementList "</Directory>"')
    def directiva_bloque(self, p):
        return ('directiva_bloque_directory', p.PathFolder, p.StatementList)

    @_('"<Files" PathFile ">" StatementList "</Files>"')
    def directiva_bloque(self, p):
        return ('directiva_bloque_files', p.PathFile, p.StatementList)

    @_('"<Location" WebAddress ">" StatementList "</Location>"')
    def directiva_bloque(self, p):
        return ('directiva_bloque_location', p.WebAddress, p.StatementList)

    # Reglas para VirtualHost
    @_('"<VirtualHost" IP ">" StatementList "</VirtualHost>"')
    def virtualhost(self, p):
        return ('virtualhost', p.IP, p.StatementList)


lexer = CalcLexer()
parser = CalcParser()
while True:
    try:
        text = input('calc > ')
        if text:
            tokens = lexer.tokenize(text)
            result = parser.parse(tokens)
            print(result)
    except EOFError:
        break