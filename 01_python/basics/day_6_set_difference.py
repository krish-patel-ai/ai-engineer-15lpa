all_users = {"u1", "u2", "u3"}
blocked_users = {"u2"}

active_users = all_users - blocked_users

print(active_users) # elements in A but no in B
