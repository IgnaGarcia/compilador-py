include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_num1 		DD 		0 
	_v1 		DD 		0 
	$10 		DD 		10 
	$3 		DD 		3 
	$6 		DD 		6 
	_TRUE 		DB 		1 
	_FALSE 		DB 		0 
	@logicalAux 		DB 		0 


.CODE ; bloque de definicion de codigo

START:
mov AX,@DATA ; carga variables
mov DS,AX
mov es,ax

	FLD _num1
	FLD $10
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNBE #tag10
	FLD _TRUE
	FSTP @logicalAux
	FFREE
	JMP #tag13
#tag10: 
	FLD _FALSE
	FSTP @logicalAux
	FFREE
#tag13: 
	FLD _TRUE
	FLD @logicalAux
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNE #tag23
	FLD $3
	FSTP _v1
	FFREE
	JMP #tag26
#tag23: 
	FLD $6
	FSTP _v1
	FFREE
#tag26: 
	FLD _v1
	DisplayInteger _v1
 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
