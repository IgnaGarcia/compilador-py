include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_num1 		DD 		0 
	$20 		DD 		20 
	$1 		DD 		1 
	$3 		DD 		3 
	$27 		DD 		27 
	_TRUE 		DD 		1 
	_FALSE 		DD 		0 
	@logicalAux 		DD 		0 


.CODE ; bloque de definicion de codigo

START:
mov AX,@DATA ; carga variables
mov DS,AX
mov es,ax

_tag1:
	FLD _num1
	FLD $20
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNB _tag11
	FLD _TRUE
	FSTP @logicalAux
	FFREE
	JMP _tag14
_tag11: 
	FLD _FALSE
	FSTP @logicalAux
	FFREE
_tag14: 
	FLD _TRUE
	FLD @logicalAux
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNE _tag50
	FLD _num1
	FLD $1
	FADD
	FSTP _num1
	FFREE
_tag25:
	FLD _num1
	FLD $3
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNE _tag35
	FLD _TRUE
	FSTP @logicalAux
	FFREE
	JMP _tag38
_tag35: 
	FLD _FALSE
	FSTP @logicalAux
	FFREE
_tag38: 
	FLD _TRUE
	FLD @logicalAux
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNE _tag48
	FLD $27
	FSTP _num1
	FFREE
	JMP _tag25
_tag48: 
	JMP _tag1
_tag50:
 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
