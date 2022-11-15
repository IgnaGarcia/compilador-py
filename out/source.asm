include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_a 		DD 		0.0 
	$303.123 		DD 		303.123 


.CODE ; bloque de definicion de codigo

START:
mov AX,@DATA ; carga variables
mov DS,AX
mov es,ax

	FLD $303.123
	FSTP _a
	FFREE
	FLD _a
	DisplayFloat _a 4
 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
