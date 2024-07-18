# zhanglong 2024.07.11

squares = [value**2 for value in range(1,11)]   #列表解析 - 定义1~10平方的列表
print(squares)

# for循环是一种遍历列表的有效方式，但for循环中不应该修改列表，否则将导致python难以跟踪其中元素。要在遍历列表的同时对其进行修改，可使用while循环
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:    # 一直循环，直到列表为空
    current_user = unconfirmed_users.pop()  # 从列表末尾删除未验证的用户，并使用该用户

    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())