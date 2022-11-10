.MODEL LARGE ; tipo del modelo de memoria usado.
.386
.STACK 200h ; bytes en el stack


.DATA ; bloque de definicion de variables
MAXTEXTSIZE equ 120
	$hola_mundo 		DB 		"hola mundo", '$', 110 dup (?) 


.CODE ; bloque de definicion de codigo
mov AX,@DATA : carga variables
mov DS,AX
mov es,ax

	FLD $hola_mundo
	MOV dx, OFFSET ESP | $hola_mundo
	MOV ah,9
	int 21h
 
mov ax,4c00h
int 21h ; interrupcion del programca
END ; fin del programa
