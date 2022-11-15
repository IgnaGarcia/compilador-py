include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_s 		DB 		"", '$', 120 dup (?) 
	@Ingrese_un_texto 		DB 		"Ingrese un texto", '$', 104 dup (?) 
	@El_text_es_ 		DB 		"El text es ", '$', 109 dup (?) 
	_TRUE 		DD 		1 
	_FALSE 		DD 		0 
	@logicalAux 		DD 		0 
	@strAux 		DB 		"", '$', 120 dup (?) 


.CODE ; bloque de definicion de codigo

START:
mov AX,@DATA ; carga variables
mov DS,AX
mov es,ax

	displayString @Ingrese_un_texto
	newLine 1
	getString _s
	FFREE
	MOV SI, OFFSET @El_text_es_
    MOV DI, OFFSET @strAux
    STRCPY
    MOV SI, OFFSET _s
    MOV DI, OFFSET @strAux
    STRCAT
	displayString @strAux
	newLine 1
 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
