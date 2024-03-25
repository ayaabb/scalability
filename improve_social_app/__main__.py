from calculations.calculate_results import (calculate_results_register, calculate_results_follow,
                                            calculate_results_post)
from calculations.calculate_runtime import calculate_runtime
from social_media import SocialMediaPlatform
from user import User
from improved_social import *


def main():
    sizes = [1000,]
    res = []
    rs = []
    r = []
    user1 = User("aya")
    social_m = SocialMediaPlatform()
    for s in sizes:
        res.append(calculate_runtime(calculate_results_register, s, social_m))
        rs.append(calculate_runtime(calculate_results_follow, s, user1))
        # r.append(calculate_runtime(calculate_results_post, social_m.users[0:s]))
    print(res)
    print(rs)
    print(r)


if __name__ == '__main__':
    main()
