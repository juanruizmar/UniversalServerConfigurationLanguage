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
  - STATEMENT_LIST-> Statement StamentList | Statement
  
  - STATEMENT-> Directiva | DirectivaBloque | VirtualHost | Modulo
  
  - DIRECTIVAS-> "Listen" int | "KeepAlive" bool | "Timeout" int | "ServerName" webAddress | "ServerAdmin" emailAddress | "DocumentRoot" Dash cadena Dash cadena dash | "DirectoryIndex" index.html | "DirectoryIndex" cadena extensions
    
  - PATH -> Dash cadena | Path Dash cadena
  - EMAIL_ADDRESS -> CadenaCompleta At Domain Extension
  - WEB_ADDRESS -> "www" Dot cadena Dot Extensions


### **Directivas no obligatorias:**

- Léxico:

  - OptionsVar -> "none" | "all" | "indexes" | "followsymlinks" | "execcgi"
  - Errors -> 400 | 401 | 403 | 404 | 500 | 503

  

- Sintáctico:

  - OPTIONS-> "Options" OptionsVar
  - ERROR_DOCUMENT-> Path ErrorDocument

  

### **Directivas Optativas:**

- Léxico:

  - MultiprocOptions -> "prefork" | "worker" | "event"

  

- Sintácticos:
  - MULTIPROCESAMIENTO-> "Multiprocesamiento" MultiprocOptions

### **Módulo Expires:**

- Léxico:

  - BaseNow -> “now”
  - BaseOther -> “access” | “modified”
  - TimeUnit -> “Year” | “Month” | “Day” | “Hours” | “Minutes” | “Seconds”
  - FileType -> “text” | “image” | “video”
  - Encoding -> “html” | “gif” | “H.264”

  

- Sintáctico:

  - TIME_PERIOD-> int TimeUnit | TimePeriod Time Unit
  - FILE_TYPE_OR_ENCODING-> FileType | Encoding
  - BASE-> BaseNow | BaseOther TimePeriod
  - EXPIRES_BODY-> Quotes Base Quote
  - EXPIRES-> “ExpiresDefault” ExpiresBody | “ExpiresByType” FileTypeOrEncoding ExpiresBody
  
  

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
  - RE_WRITE_RULE-> “RewriteCond” TestString CondPattern | “RewriteRule” Pattern Substitution
  - COND_PATTERN -> CP_INNER | CP_INNER \$ | \^ CP_INNER | \^ CP_INNER \$

- Sintáctico auxiliar para COND_PATTERN
  - CP_INNER -> CP_INNER_AUX | CP_INNER CP_INNER_AUX
  - CP_INNER_AUX -> CP_BASIC | \! CP_BASIC | CP_BASIC CPCierres | \! CP_BASIC CPCierres
  - CP_BASIC -> CP_BASIC_AUX | CP_BASIC CP_BASIC_AUX
  - CP_BASIC_AUX -> \epsilon | \\ CPChar

###  

### **Directiva de bloques:**

- Sintácticos: 
  - DIRECTIVA_BLOQUES-> “<Directory” cadena “>” StatementList “</Directory>” | 
  
    “<Files” cadena “>” StatementList“</Files>” | “<Location” cadena “>” StatementList“</Location>”
  
    

### **VirtualHost:**

- Sintácticos:
  - VIRTUAL_HOST-> “<VirtualHost” cadena “>” StatementList “</VirtualHost>”
  
  

### **Diseñar el analizador léxico**

para la gramática del lenguaje, implementarlo en SLY

### **Diseñar el analizador sintáctico**

para la gramática, implementarlo en SLY

- Importante: En caso de ambigüedad resolverla a nivel de gramática. NO se puede utilizar las precedencias de SLY

- Entrega: detallado en la diapositiva 3
