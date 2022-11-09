.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_v1 		DB 		1 


.CODE ; bloque de definicion de codigo
mov AX,@DATA : carga variables
mov DS,AX
mov es,ax

	FLD 1
	FLD 0
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNE _tag13
	FLD 1
	FLD 1
	FXCH
	FCOM
	FSTSW AX
	SAHF
	JNE _tag13
	FLD 1
	JMP _tag14
_tag13: 
	FLD 0
_tag14: 
	FSTP @logicalAux
	FFREE
	FLD @logicalAux
	FSTP _v1
	FFREE
 
mov ax,4c00h
int 21h ; interrupcion del programca
END ; fin del programa
