PathFolder -> Dash | Dash Cadena PathFolder
PathFile -> PathFolder File | File
EmailAddress -> Cadena At Domain Dot Extension
WebAddress -> "www" Dot Cadena Dot Extension
File -> Cadena Dot Extension
IP -> int Dot int Dot int Dot int Port
Port -> epsilon | ":" int

PRINCIPAL:
StatementList -> Statement StatementList | Statement
Statement -> DirectivaBloque | VirtualHost | Directiva | Modulo

BLOQUE DE DIRECTIVAS:
DirectivaBloque -> “<Directory” PathFolder “>” StatementList “</Directory>” | “<Files” PathFile “>” StatementList “</Files>” |
                   “<Location” WebAddress “>” StatementList “</Location>”

VIRTUALHOST:
VirtualHost -> “<VirtualHost” IP “>” StatementList “</VirtualHost>”

DIRECTIVAS OBLIGATORIAS:
Directiva -> "Listen" int | "KeepAlive" bool | "Timeout" int | "ServerName" WebAddress | "ServerAdmin" EmailAddress | "DocumentRoot" PathFolder |
             "DirectoryIndex" PathFile | "ErrorLog" PathFile

DIRECTIVAS NO OBLIGATORIAS:
OptionsVar -> "none" | "all" | "indexes" | "followsymlinks" | "execcgi"
Errors -> 400 | 401 | 403 | 404 | 500 | 503
Directiva -> "Options" OptionsVar
Directiva -> "ErrorDocument" Errors PathFile

MultiprocOptions -> "prefork" | "worker" | "event"
Directiva -> "Multiprocesamiento" MultiprocOptions

MODULOS:
Modulo -> Expires | Sobrescritura

BaseNow -> “now”
BaseOther -> “access” | “modified”
TimeUnit -> “Year” | “Month” | “Day” | “Hours” | “Minutes” | “Seconds”
FileType -> “text” | “image” | “video”
Encoding -> “html” | “gif” | “H.264”

Expires -> “ExpiresByType” FileTypeEncoding ExpiresBody | “ExpiresDefault” ExpiresBody
FileTypeEncoding -> FileType Dash Encoding
ExpiresBody -> Quotes Base Quote
Base -> BaseNow | BaseOther TimePeriod
TimePeriod -> int TimeUnit | int TimeUnit TimePeriod

TestString -> “REQUEST_URI” | “REQUEST_FILENAME” | “QUERY_STRING” | “REMOTE_ADDR”
Pattern -> .’(‘.’)’.*
Substitution -> $1
CPBasicAux -> .
CPCierres -> * | +
CPChar -> ^ | $ | . | \ | ! | * | +

Sobreescritura -> RewriteCond Sobreescritura | RewriteCond
RewriteCond -> “RewriteCond” TestString CondPattern RewriteCond | “RewriteCond” TestString CondPattern RewriteRule
RewriteRule -> “RewriteRule” Pattern Substitution | “RewriteRule” Pattern Substitution RewriteRule | “RewriteRule” Pattern Substitution RewriteCond

CP_INNER -> CP_INNER_AUX | CP_INNER CP_INNER_AUX
CP_INNER_AUX -> CP_BASIC | ! CP_BASIC | CP_BASIC CPCierres | ! CP_BASIC CPCierres
CP_BASIC -> CP_BASIC_AUX | CP_BASIC CP_BASIC_AUX
CP_BASIC_AUX -> \epsilon | \ CPChar
