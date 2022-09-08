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
    [start_string_id, start_int, start_string,do_nothing,do_nothing,do_nothing,do_nothing,	start_real,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing],
    [add_string_id, add_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id],
    [save_int,	add_int,	save_int, save_int,	save_int, save_int,	save_int, start_real, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int],
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
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing, add_real, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
]

print(process_table[2][2])