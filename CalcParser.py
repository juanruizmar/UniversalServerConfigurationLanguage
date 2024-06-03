from sly import Parser
from CalcLexer import CalcLexer


class CalcParser(Parser):
    tokens = CalcLexer.tokens

    @_('Statement_List')
    def program(self, p):
        return ('program', p.Statement_List)

    @_('Statement Statement_List')
    def Statement_List(self, p):
        return [p.Statement] + p.Statement_List

    @_('Statement')
    def Statement_List(self, p):
        return [p.Statement]

    # Define las reglas para diferentes tipos de declaraciones
    @_('Directive')
    def Statement(self, p):
        return p.Directive

    @_('Expires')
    def Statement(self, p):
        return p.Expires

    @_('Sobreescritura')
    def Statement(self, p):
        return p.Sobreescritura

    @_('Directiva_Bloque')
    def Statement(self, p):
        return p.Directiva_Bloque

    @_('Virtualhost')
    def Statement(self, p):
        return p.Virtualhost

    # Reglas para directivas
    @_('DirectiveName STRING')
    def Directive(self, p):
        return ('Directive', p.DirectiveName, p.STRING)
    
    @_('"Multiprocesamiento" MULTIPROC_OPTIONS')
    def Directive(self, p):
        return p.multiprocessing

    # Reglas para módulo Expires
    @_('"ExpiresByType" FILE_TYPE "/" ENCODING Expires_Body')
    def Expires(self, p):
        return ('Expires', p.ExpiresByType, p.FileType, p.Dash, p.ENCODING, p.Expires_Body)

    @_('"ExpiresDefault" Expires_Body')
    def Expires(self, p):
        return ('Expires', p.ExpiresDefault, p.Expires_Body)

    @_('"\"" Base "\""')
    def Expires_Body(self, p):
        return ('Expires_body', p.Base)

    @_('BASE_NOW')
    def Base(self, p):
        return ('base_now', p.BASE_NOW)

    @_('BASE_OTHER Time_Period')
    def Base(self, p):
        return ('base_other', p.BASE_OTHER, p.Time_Period)

    @_('INT TIME_UNIT')
    def Time_Period(self, p):
        return ('Time_Period', p.INT, p.TIME_UNIT)

    @_('INT TIME_UNIT Time_Period')
    def Time_Period(self, p):
        return ('Time_Period', p.INT, p.TIME_UNIT, p.Time_Period)

    # Reglas para módulo Sobreescritura
    @_('Rewrite_Cond Sobreescritura')
    def Sobreescritura(self, p):
        return ('Sobreescritura', p.Rewrite_Cond, p.Sobreescritura)

    @_('Rewrite_Cond')
    def Sobreescritura(self, p):
        return ('Sobreescritura', p.Rewrite_Cond)

    @_('"RewriteCond" TEST_STRING PATTERN Rewrite_Cond')
    def Rewrite_Cond(self, p):
        return ('Rewrite_Cond', p.TEST_STRING, p.PATTERN, p.Rewrite_Cond)

    @_('"RewriteCond" TEST_STRING PATTERN Rewrite_Rule')
    def Rewrite_Cond(self, p):
        return ('Rewrite_Cond', p.TEST_STRING, p.PATTERN, p.Rewrite_Rule)

    @_('"RewriteRule" PATTERN SUBSTITUTION')
    def Rewrite_Rule(self, p):
        return ('Rewrite_Rule', p.PATTERN, p.SUBSTITUTION)

    @_('"RewriteRule" PATTERN SUBSTITUTION Rewrite_Rule')
    def Rewrite_Rule(self, p):
        return ('Rewrite_Rule', p.PATTERN, p.SUBSTITUTION, p.Rewrite_Rule)

    # Reglas para directiva de bloques
    @_('"<Directory" Pathfolder ">" Statement_List "</Directory>"')
    def Directiva_Bloque(self, p):
        return ('Directiva_Bloque_directory', p.Pathfolder, p.Statement_List)

    @_('"<Files" Pathfile ">" Statement_List "</Files>"')
    def Directiva_Bloque(self, p):
        return ('Directiva_Bloque_files', p.Pathfile, p.Statement_List)

    @_('"<Location" Web_Address ">" Statement_List "</Location>"')
    def Directiva_Bloque(self, p):
        return ('Directiva_Bloque_location', p.Web_Address, p.Statement_List)

    # Reglas para Virtualhost
    @_('"<Virtualhost" IP ">" Statement_List "</Virtualhost>"')
    def Virtualhost(self, p):
        return ('Virtualhost', p.IP, p.Statement_List)
    
    #Reglas Auxiliares
    @_('"/"')
    def Pathfolder(self,p):
        return
    
    @_('"/" STRING Pathfolder')
    def Pathfolder(self,p):
        return
    
    @_('Pathfolder File')
    def Pathfile(self,p):
        return
    
    @_('File')
    def Pathfile(self,p):
        return
    
    @_('STRING "@" Domain "." EXTENSION')
    def Email_Address(self,p):
        return
    
    @_('"www." STRING "." EXTENSION')
    def Web_Address(self,p):
        return
    
    @_('STRING "." EXTENSION')
    def File(self,p):
        return
    
    @_('INT "." INT "." INT "." INT Port')
    def IP(self,p):
        return
    
    @_('":" INT')
    def Port(self,p):
        return
    
    @_('')
    def Port(self,p):
        return
    


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