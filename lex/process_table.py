# Aun resta ver el tema de las variables globales. Por lo que veo en cada funcion las vuelve a crear con lo que no toman el sentido que quiero darles. A revisar manana. Deje la logica, solo a modo de ejemplo

# Counter
counter = 0

# Limits
string_limit = 144
string_id_limit = 32
int_limit = 6
real_int_limit = 6
real_decimal_limit = 4

# ID
id = ''

# CTE Entera
cte_Entera = ''

# CTE Real
cte_real = ''


def do_nothing():
    return

def state_error():
    return

def start_string_id(char):
    # id = ''
    # id += char
    # counter += 1
    return

def add_string_id(char):
    # if counter <= string_id_limit:
    #     id += char
    #     counter += 1
    return

def save_string_id(char):
    return id

def start_int(char):
    return

def add_int(char):
    return

def save_int():
    # Persist Int
    return

def start_real(char):
    return

def add_real(char):
    return

def save_real():
    # Persist Real
    return

def start_string(char):
    # id = ''
    # id += char
    # counter += 1
    return

def add_string(string, char):
    # if counter <= string_id_limit:
    #     id += char
    #     counter += 1
    return

def save_string():
    # Persist String
    return
process_table=[
    [start_string_id, start_int, start_string,	9,	10,	11,	12,	start_real(),	29,	30,	15,	13,	6,	16,	17,	19,	25,	27,	21,	23,	31,	33,	0,	-1],
    [add_string_id, add_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id],
    [save_int,	add_int,	save_int, save_int,	save_int, save_int,	save_int, start_real(int), save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int],
    [save_real,add_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real],
    [add_string,add_string,save_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,state_error],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,state_error],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,state_error],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	14,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	18,	-1,	-1,	-1,	-1],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	20,	-1,	-1,	-1,	-1],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	22,	-1,	-1,	-1,	-1],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	24,	-1,	-1,	-1,	-1],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	26,	-2,	-2,	-2,	-2,	-2,	-2,	-2],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	-2,	28,	-2,	-2,	-2,	-2,	-2,	-2],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing, add_real, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
]

