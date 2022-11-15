include macros.asm
include number.asm

.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_n 		DD 		0 
	@Ingrese_un_numero 		DB 		"Ingrese un numero", '$', 103 dup (?) 
	@El_numero_es_ 		DB 		"El numero es ", '$', 107 dup (?) 
	_TRUE 		DD 		1 
	_FALSE 		DD 		0 
	@logicalAux 		DD 		0 
	@strAux 		DB 		"", '$', 120 dup (?) 


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
	FLD _n
	MOV SI, OFFSET @El_numero_es_
    MOV DI, OFFSET @strAux
    STRCPY
    MOV SI, OFFSET _n
    MOV DI, OFFSET @strAux
    STRCAT
	displayString @strAux
	newLine 1
 
mov ax,4c00h
int 21h ; interrupcion del programca
END START; fin del programa
