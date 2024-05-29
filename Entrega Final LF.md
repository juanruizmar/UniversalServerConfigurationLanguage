# Teoría de Autómatas y Lenguajes Formales.
## Trabajo Final.

**Realizado por:**

- Juan Ruiz Martos
- Pablo Pérez Santiago
- Daniel Parejo Jaramago

[TOC]

Vamos a crear un lenguaje de programación nuevo para programar servidores webs.

Ya hay muchos en el mercado, que hacen mas o menos lo mismo, pero nosotros diseñaremos uno, haremos el analizador léxico y sintáctico.

### Objetivo.
Creación de un lenguaje de programación para la configuración de servidores web.

- Objetivos Parciales:
	- Diseño del lenguaje de programación
	- Diseño de una gramática para representar el lenguaje del punto anterior
	- Diseño del analizador léxico para el lenguaje
	- Diseño del analizador sintáctico para el lenguaje

Valor: 20% de la puntuación final.

### Documentos a subir.
Todo en un zip.
- Memoria explicativa.
- Manual de usuario.
- Fichero SLY (Preferiblemente un notebook de jupyter).
	- Implementación del analizador léxico
	- Implementación del analizador sintáctico.
- Ejemplo de programa.

## Servidores Web.
### Servidores Web.
- Provisión de contenidos estáticos
- Intermediarios con servidores de aplicación

### Características.

- Host Virtuales. Varios sitios web en el mismo servidor
- Autenticación del solicitante
- Sistema de registros (logs).
- Ejecución de contenido dinámico. (Servidores de aplicación)
- Rapidez.
- Seguridad. (Http)

## Configuración de los servidores web.
### Estructura de configuración de los servidores web.

#### Virtual Hosts.
#### Directivas Obligatoras.
#### Directivas No Obligatorias

### Módulos.

#### Módulo: Multiprocesamiento.

#### Módulo: Expires.

#### Módulo de reescritura.



# Actividades a realizar

## **Diseñar la gramática**

de un lenguaje de programación que permita configurar un servidor Web utilizando todos los componentes mencionados anteriormente: Directivas, Bloques de directivas (Directory, File y Location), Virtual Hosts y módulos

### **Directivas Obligatorias** 

- Compilador léxico:

  - OpenBracket -> {
  - CloseBracket -> }
  - Semicolon -> ;
  - Dash -> /
  - Extensions -> ( html , com, es, etc) (no det)
  - At -> @
  - Dot -> .
  - Int -> \d
  - Cadena -> ^\w+$
  - Bool -> On | Off
  - Quotes -> \”
  - Domain ->  (Poner lista de dominios validos)

  

- Al sintáctico:
  - StatementList-> Statement StatementList | Statement
  - Statement -> Directiva | DirectivaBloque | VIRTUAL_HOST | MODULO
  
  - Directiva -> "Listen" int | "KeepAlive" bool | "Timeout" int | "ServerName" WebAddress | "ServerAdmin" EmailAddress | "DocumentRoot" PathFolder | "DirectoryIndex" index.html | "DirectoryIndex" PathFile | "ErrorLog" PathFile
    
  - PathFolder -> Dash | Dash Cadena PathFolder
  - PathFile -> PathFolder File | File
  - EmailAddress -> Cadena At Domain Dot Extension
  - WebAddress -> "www" Dot Cadena Dot Extension
  - File -> Cadena Dot Extension
  - IP -> int Dot int Dot int Dot int Port
  - Port -> epsilon | ":" int


### **Directivas no obligatorias:**

- Léxico:

  - OptionsVar -> "none" | "all" | "indexes" | "followsymlinks" | "execcgi"
  - Errors -> 400 | 401 | 403 | 404 | 500 | 503

  

- Sintáctico:

  - Directiva -> "Options" OptionsVar
  - Directiva -> "ErrorDocument" Errors PathFile

  

### **Directivas Optativas:**

- Léxico:

  - MultiprocOptions -> "prefork" | "worker" | "event"

  

- Sintácticos:
  - Directiva -> "Multiprocesamiento" MultiprocOptions

### **Módulo Expires:**

- Léxico:

  - BaseNow -> “now”
  - BaseOther -> “access” | “modified”
  - TimeUnit -> “Year” | “Month” | “Day” | “Hours” | “Minutes” | “Seconds”
  - FileType -> “text” | “image” | “video”
  - Encoding -> “html” | “gif” | “H.264”

  

- Sintáctico:

  - Expires -> “ExpiresByType” FileTypeEncoding ExpiresBody | “ExpiresDefault” ExpiresBody
  - FileTypeEncoding -> FileType Dash Encoding
  - ExpiresBody -> Quotes Base Quote
  - BASE -> BaseNow | BaseOther TimePeriod
  - TimePeriod -> int TimeUnit | int TimeUnit TimePeriod
  

### **Módulo Sobreescritura:**

- Léxico:
  - TestString -> “REQUEST_URI” | “REQUEST_FILENAME” | “QUERY_STRING” | “REMOTE_ADDR”
  - Pattern -> .*’(‘.*’)’.*
  - Substitution -> $1

- Léxico auxiliar para COND_PATTERN
  - CPBasicAux -> \.
  - CPCierres -> \* | \+
  - CPChar -> \^ | \$ | \. | \\ | \! | \* | \+
  
- Sintáctico:
  - Sobreescritura -> RewriteCond Sobreescritura | RewriteCond
  - RewriteCond -> “RewriteCond” TestString CondPattern RewriteCond | “RewriteCond” TestString CondPattern RewriteRule
  - RewriteRule -> “RewriteRule” Pattern Substitution | “RewriteRule” Pattern Substitution RewriteRule | “RewriteRule” Pattern Substitution RewriteCond

- Sintáctico auxiliar para COND_PATTERN
  - CP_INNER -> CP_INNER_AUX | CP_INNER CP_INNER_AUX
  - CP_INNER_AUX -> CP_BASIC | \! CP_BASIC | CP_BASIC CPCierres | \! CP_BASIC CPCierres
  - CP_BASIC -> CP_BASIC_AUX | CP_BASIC CP_BASIC_AUX
  - CP_BASIC_AUX -> \epsilon | \\ CPChar

###  

### **Directiva de bloques:**

- Sintácticos: 
  - DirectivaBloque-> “<Directory” PathFolder “>” StatementList “</Directory>” | 
  
    “<Files” PathFile “>” StatementList“</Files>” | “<Location” WebAddress “>” StatementList“</Location>”
  
    

### **VirtualHost:**

- Sintácticos:
  - VirtualHost-> “<VirtualHost” IP “>” StatementList “</VirtualHost>”
  
  

### **Diseñar el analizador léxico**

para la gramática del lenguaje, implementarlo en SLY

### **Diseñar el analizador sintáctico**

para la gramática, implementarlo en SLY

- Importante: En caso de ambigüedad resolverla a nivel de gramática. NO se puede utilizar las precedencias de SLY

- Entrega: detallado en la diapositiva 3
