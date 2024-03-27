from Improved_classes.improved_social import ImprovedSocialMediaPlatform
from classes.social_media import SocialMediaPlatform
from results_execution.main_function_executor import run_register_follow, run_post_before, run_post_after, \
    run_generate_timeline
from performance_operations.calculate_runtime import calculate_runtime
from performance_operations.write_peformance_results_to_file import write_results_to_file


def results_executor_before_improving():
    social_m = SocialMediaPlatform()
    register_result = calculate_runtime(run_register_follow, 20000, social_m.register_user, 'user')
    follow_result = calculate_runtime(run_register_follow, 20000, social_m.users[0].follow, 'user')
    post_result = calculate_runtime(run_post_before, 10000, social_m.users)
    generate_result = calculate_runtime(run_generate_timeline, social_m, 'user0')
    write_results_to_file("results.txt", "register", register_result, "before")
    write_results_to_file("results.txt", "follow", follow_result, "before")
    write_results_to_file("results.txt", "post message", post_result, "before")
    write_results_to_file("results.txt", "generate timeline", generate_result, "before")


def results_executor_after_improving():
    social_m = ImprovedSocialMediaPlatform()
    register_result = calculate_runtime(run_register_follow, 20000, social_m.register_user, 'user')
    write_results_to_file("results.txt", "register", register_result, "after")
    follow_result = calculate_runtime(run_register_follow, 20000, social_m.users['user0'].follow, 'user')
    write_results_to_file("results.txt", "follow", follow_result, "after")
    post_result = calculate_runtime(run_post_after, 10000, social_m.users)
    write_results_to_file("results.txt", "post message", post_result, "after")
    generate_result = calculate_runtime(run_generate_timeline, social_m, 'user0')
    write_results_to_file("results.txt", "generate timeline", generate_result, "after")
