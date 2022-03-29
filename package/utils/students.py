def get_student_ids(number_of_students, prefix=''):
    return ['{}_{:02d}'.format(prefix, index) for index in range(1, number_of_students+1)]