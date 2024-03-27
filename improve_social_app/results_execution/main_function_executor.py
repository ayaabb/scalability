def run_register_follow(n, func_, info):
    if func_.__name__ == 'register_user':
        func_(info + '0')
    for i in range(1, n):
        func_(info + str(i))


def run_post_before(n, users):
    for user in users:
        user.post_message(user.username + "msg")
    for i in range(n):
        users[0].post_message(users[0].username + "msg" + str(i))


def run_post_after(n, users):
    for username, user in users.items():
        user.post_message(username + "msg")
    for i in range(n):
        users['user0'].post_message(users['user0'].username + "msg" + str(i))


def run_generate_timeline(social, username):
    social.generate_timeline(username)
