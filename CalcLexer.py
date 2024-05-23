from sly import Lexer
from sly import Parser

import sys

class CalcLexer(Lexer):
	tokens = {
		OpenBracket, CloseBracket, Semicolon, Extension, At, Dot, Int, Cadena, Bool, Quotes, Domain,

		BaseNow, BaseOther, TimeUnit, FileType, Encoding, TestString, CP, Pattern, Substitution,
	}

	ignore = r' |\t'

	OpenBracket = '{'
	CloseBracket = '}'

	Semicolon = ';'
	Extension = r'html|com'	# Todas las extensiones válidas 

	At = '@'
	Dot = '.'
	Int = r'\d+'
	Cadena = r'\w+'
	Bool = r'On|Off'
	Quotes = '"'
	Domain = 'LoL xD'	# Una lista de dominios válidos
	BaseNow = 'now'
	BaseOther = r'access|remote'
	TimeUnit = r'Year|Month|Day|Hour|Minute|Second'
	FileType = r'text|image|video'
	Encoding = r'html|gif|H.264'
	TestString = r'REQUEST_URI|REQUEST_FILENAME|QUERY_STRING|REMOTE_ADDR'

#	Una gramática para el CP
	CondPattern = r'CPInner|CPInner\$|\^CPInner|\^CPInner\$'
	CPInner = r'CPInnerAux | CPInner CPInnerAux'
	CPInnerAux = r'CPBasic|\! CPBasic|CPBasic CPCierres|\! CPBasic CPCierres'	# Añadir capa
	CPBasic = r'CPBasicAux|CPBasic CPBasicAux'
	CPBasicAux = r'\.|\\ CPChar'												# Añadir capa

	CPCierres = r'\*|\+'
	CPChar = r'\^|\$|\.|\\|\!|\*|\+'

