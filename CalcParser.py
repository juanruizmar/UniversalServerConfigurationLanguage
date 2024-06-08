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
    @_('DIRECTIVE_INT INT')
    def Directive(self, p):
        return ('Directive', p.DIRECTIVE_INT, p.INT)
    
    @_('DIRECTIVE_BOOL BOOL')
    def Directive(self, p):
        return ('Directive', p.DIRECTIVE_BOOL, p.BOOL)
    
    @_('DIRECTIVE_WA Web_Address')
    def Directive(self, p):
        return ('Directive', p.DIRECTIVE_WA, p.Web_Address)
    
    @_('DIRECTIVE_EA Email_Address')
    def Directive(self, p):
        return ('Directive', p.DIRECTIVE_EA, p.Email_Address)
    
    @_('DIRECTIVE_PFD Pathfolder')
    def Directive(self, p):
        return ('Directive', p.DIRECTIVE_PFd, p.Pathfolder)
    
    @_('DIRECTIVE_PF Pathfile')
    def Directive(self, p):
        return ('Directive', p.DIRECTIVE_PF, p.Pathfile)
    
    @_('OPTIONS OPTIONS_VAR')
    def Directive(self, p):
        return ('Directive', p.OPTIONS, p.OPTIONS_VAR)
    
    @_('ERRORDOCUMENT ERRORS Pathfile')
    def Directive(self, p):
        return ('Directive', p.ERRORDOCUMENT, p.ERRORS, p.Pathfile)
    
    @_('MULTIPROCESS MULTIPROC_OPTIONS')
    def Directive(self, p):
        return (p.MULTIPROCESS, p.MULTIPROC_OPTIONS)

    # Reglas para módulo Expires
    @_('EXPIRESBYTYPE FILE_TYPE "/" ENCODING Expires_Body')
    def Expires(self, p):
        return ('Expires', p.EXPIRESBYTYPE, p.FileType, p.Dash, p.ENCODING, p.Expires_Body)

    @_('EXPIRESDEFAULT Expires_Body')
    def Expires(self, p):
        return ('Expires', p.EXPIRESDEFAULT, p.Expires_Body)

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

    @_('RWCOND TEST_STRING PATTERN Rewrite_Cond')
    def Rewrite_Cond(self, p):
        return ('Rewrite_Cond', p.TEST_STRING, p.PATTERN, p.Rewrite_Cond)

    @_('RWCOND TEST_STRING PATTERN Rewrite_Rule')
    def Rewrite_Cond(self, p):
        return ('Rewrite_Cond', p.TEST_STRING, p.PATTERN, p.Rewrite_Rule)

    @_('RWRULE PATTERN SUBSTITUTION')
    def Rewrite_Rule(self, p):
        return ('Rewrite_Rule', p.PATTERN, p.SUBSTITUTION)

    @_('RWRULE PATTERN SUBSTITUTION Rewrite_Rule')
    def Rewrite_Rule(self, p):
        return ('Rewrite_Rule', p.PATTERN, p.SUBSTITUTION, p.Rewrite_Rule)

    # Reglas para directiva de bloques
    @_('PREBLOQUE_D Pathfolder ">" Statement_List POSTBLOQUE_D')
    def Directiva_Bloque(self, p):
        return ('Directiva_Bloque_directory', p.Pathfolder, p.Statement_List)

    @_('PREBLOQUE_F Pathfile ">" Statement_List POSTBLOQUE_F')
    def Directiva_Bloque(self, p):
        return ('Directiva_Bloque_files', p.Pathfile, p.Statement_List)

    @_('PREBLOQUE_L Web_Address ">" Statement_List POSTBLOQUE_L')
    def Directiva_Bloque(self, p):
        return ('Directiva_Bloque_location', p.Web_Address, p.Statement_List)

    # Reglas para Virtualhost
    @_('PREBLOQUE_V IP ">" Statement_List POSTBLOQUE_V')
    def Virtualhost(self, p):
        return ('Virtualhost', p.IP, p.Statement_List)
    
    #Reglas Auxiliares
    @_('"/"')
    def Pathfolder(self,p):
        return "/"
    
    @_('"/" STRING Pathfolder')
    def Pathfolder(self,p):
        return "/" + p.STRING + p.Pathfolder
    
    @_('Pathfolder File')
    def Pathfile(self,p):
        return p.Pathfolder + p.File
    
    @_('File')
    def Pathfile(self,p):
        return p.File
    
    @_('STRING "@" DOMAIN "." EXTENSION')
    def Email_Address(self,p):
        return p.STRING + "@" + p.DOMAIN + "." + p.EXTENSION
    
    @_('SUBDOMAIN "." STRING "." EXTENSION')
    def Web_Address(self,p):
        return "www" + "." + p.STRING + "." + p.EXTENSION
    
    @_('STRING "." EXTENSION')
    def File(self,p):
        return p.STRING + "." + p.EXTENSION
    
    @_('INT "." INT "." INT "." INT Port')
    def IP(self,p):
        return p.INT + "." + p.INT + "." + p.INT + "." +p.INT + p.Port
    
    @_('":" INT')
    def Port(self,p):
        return ":" + p.INT
    
    @_('')
    def Port(self,p):
        pass
    


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