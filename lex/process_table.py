# Global Variables
#Counter
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
cte_entera = ''

# CTE Real
cte_real = ''


def do_nothing(_):
    return

def start_string_id(char):
    global id, counter
    id = char
    counter = 1
    return

def add_string_id(char):
    global counter
    global id
    if counter <= string_id_limit:
        id += char
        counter += 1
    return

def save_string_id(_):
    global id
    return id

def start_int(char):
    global cte_entera, counter
    cte_entera = char
    counter = 1
    return

def add_int(char):
    global cte_entera, counter
    if counter <= int_limit:
        cte_entera += char
        counter += 1
    return

def save_int(_):
    global cte_entera
    return cte_entera

def start_real(char):
    global cte_real, counter
    if counter <= int_limit:
        cte_real += char
        counter += 1
    return

def add_real(char):
    global cte_real, counter
    if counter <= int_limit:
        cte_real += char
        counter += 1
    return

def save_real(_):
    global cte_real
    return cte_real

def start_string(char):
    global id, counter
    id = char
    counter = 1
    return

def add_string(char):
    global counter
    global id
    if counter <= string_limit:
        id += char
        counter += 1
    return

def save_string(_):
    global id
    return id

process_table=[
    [start_string_id, start_int, start_string,do_nothing,do_nothing,do_nothing,do_nothing,	start_real,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing,	do_nothing],
    [add_string_id, add_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id, save_string_id],
    [save_int,	add_int,	save_int, save_int,	save_int, save_int,	save_int, start_real, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int, save_int],
    [save_real,add_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real,save_real],
    [add_string,add_string,save_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,add_string,do_nothing],
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
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
    [do_nothing, add_real, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing, do_nothing],
    [do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing,do_nothing],
]