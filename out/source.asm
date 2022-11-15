include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_n 		DD 		0 
	@Ingrese_un_numero 		DB 		"Ingrese un numero", '$', 103 dup (?) 
	_TRUE 		DD 		1 
	_FALSE 		DD 		0 
	@logicalAux 		DD 		0 


.CODE ; bloque de definicion de codigo

START:
mov AX,@DATA ; carga variables
mov DS,AX
mov es,ax

	displayString @Ingrese_un_numero
	newLine 1
	FLD _n
	GetInteger _n
	FREE
 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
