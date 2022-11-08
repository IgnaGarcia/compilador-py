.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
_mensaje 		DB 		"", '$', 120 dup (?); 
_valor 		DD 		0 ; 
_flag 		DB 		1 ; 
$Ejemplo_Print_ 		DB 		"Ejemplo Print ", '$', 106 dup (?); 
_valior 		DD 		None ; 
$3 		DD 		3 ; 
$de_Variable 		DB 		"de Variable", '$', 109 dup (?); 
$de_Constante 		DB 		"de Constante", '$', 108 dup (?); 


.CODE ; bloque de definicion de codigo
mov AX,@DATA : carga variables
mov DS,AX
mov es,ax ;

mov ax,4c00h
int 21h ; interrupcion del programca
END ; fin del programa
