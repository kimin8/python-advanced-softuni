def gather_credits(number_of_credits_needed, *args):
    already_enrolled = []
    total_credits = 0

    for tokens in args:
        course_name, credits = tokens

        if total_credits < number_of_credits_needed:
            if not course_name in already_enrolled:
                already_enrolled.append(course_name)
                total_credits += credits
        else:
            break
    
    if total_credits >= number_of_credits_needed:
        return f'Enrollment finished! Maximum credits: {total_credits}.\nCourses: {", ".join(sorted(already_enrolled))}'            
    else:
        return f"You need to enroll in more courses! You have to gather {number_of_credits_needed - total_credits} credits more."