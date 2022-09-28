
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMA COMP_DISTINTO COMP_IGUAL COMP_MAYOR COMP_MAYOR_IGUAL COMP_MENOR COMP_MENOR_IGUAL CONDICION_TERNARIA CTE_NUMERICA CTE_REAL CTE_STRING DOS_PUNTOS ID LLAVE_ABRE LLAVE_CIERRA OP_AND OP_ASIGNACION OP_CONCAT OP_DIVISION OP_MULTIPLICACION OP_NOT OP_OR OP_RESTA OP_SUMA PARENTESIS_ABRE PARENTESIS_CIERRA PUNTO_COMA between bool else false if in int out real string true var while\n    expression : expression OP_SUMA term\n                | expression OP_RESTA term\n                | term\n    \n    term : term OP_MULTIPLICACION factor\n        | term OP_DIVISION factor \n        | factor\n    \n    factor : CTE_NUMERICA\n        | CTE_REAL\n        | ID\n    '
    
_lr_action_items = {'CTE_NUMERICA':([0,7,8,9,10,],[4,4,4,4,4,]),'CTE_REAL':([0,7,8,9,10,],[5,5,5,5,5,]),'ID':([0,7,8,9,10,],[6,6,6,6,6,]),'$end':([1,2,3,4,5,6,11,12,13,14,],[0,-3,-6,-7,-8,-9,-1,-2,-4,-5,]),'OP_SUMA':([1,2,3,4,5,6,11,12,13,14,],[7,-3,-6,-7,-8,-9,-1,-2,-4,-5,]),'OP_RESTA':([1,2,3,4,5,6,11,12,13,14,],[8,-3,-6,-7,-8,-9,-1,-2,-4,-5,]),'OP_MULTIPLICACION':([2,3,4,5,6,11,12,13,14,],[9,-6,-7,-8,-9,9,9,-4,-5,]),'OP_DIVISION':([2,3,4,5,6,11,12,13,14,],[10,-6,-7,-8,-9,10,10,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'term':([0,7,8,],[2,11,12,]),'factor':([0,7,8,9,10,],[3,3,3,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression OP_SUMA term','expression',3,'p_expression','sintactico.py',17),
  ('expression -> expression OP_RESTA term','expression',3,'p_expression','sintactico.py',18),
  ('expression -> term','expression',1,'p_expression','sintactico.py',19),
  ('term -> term OP_MULTIPLICACION factor','term',3,'p_term','sintactico.py',30),
  ('term -> term OP_DIVISION factor','term',3,'p_term','sintactico.py',31),
  ('term -> factor','term',1,'p_term','sintactico.py',32),
  ('factor -> CTE_NUMERICA','factor',1,'p_factor','sintactico.py',43),
  ('factor -> CTE_REAL','factor',1,'p_factor','sintactico.py',44),
  ('factor -> ID','factor',1,'p_factor','sintactico.py',45),
]
