.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	_cte1 		DD 		0 
	_num 		DD 		0 
	_num2 		DD 		0.0 
	$5 		DD 		5 
	$25 		DD 		25 
	$3 		DD 		3 
	$5.6 		DD 		5.6 
	$1.0 		DD 		1.0 


.CODE ; bloque de definicion de codigo
mov AX,@DATA : carga variables
mov DS,AX
mov es,ax

<<<<<<< HEAD
	FLD $5
	FLD _cte1
	FLD $25
	FLD $3
=======
	FLD 5
	FLD _cte1
	FLD 25
	FLD 3
>>>>>>> f4f461f4a6c7aa6bf9c7dc7c5621c4db979c032c
	FADD
	FMUL
	FADD
	FSTP _num
	FFREE

<<<<<<< HEAD
	FLD $5.6
	FLD $1.0
=======
	FLD 5.6
	FLD 1.0
>>>>>>> f4f461f4a6c7aa6bf9c7dc7c5621c4db979c032c
	FADD
	FSTP _num2
	FFREE

 
mov ax,4c00h
int 21h ; interrupcion del programca
END ; fin del programa
