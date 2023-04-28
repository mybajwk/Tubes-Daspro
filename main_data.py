
is_login = False
stop_program = False
current_user = None
current_role = None
# data from csv
data_csv_user = None  # 1
user_len = 0
data_csv_bahan = None  # 2
bahan_len = 0
data_csv_candi = None  # 3
candi_len = 0
folder = None


# for data
user_data = [None for k in range(3)]
bahan_data = [None for k in range(3)]
candi_data = [None for k in range(5)]


# fitur bonus
undo_stack = []
len_undo = 0
