def rand05(seed):
    # X(n+1) = (a*X(n) + c) % m
    # a, c, dan m dipilih 691, 4201, dan 694201 karena funni. Cycle length 57850 kalau seed awalnya 0

    seed = (691*seed + 4201) % 694201
    return seed

# kalau mau keluarin angka 0 sampai 5 tinggal seed%6
# kalau mau dipakai mungkin harus disimpan seednya??? gak tahu gimana