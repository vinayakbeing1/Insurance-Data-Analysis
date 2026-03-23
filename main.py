def sum_array(a):
  return sum(a)


def feast(beast, dish):
    if beast[0].lower() == dish[0].lower() and beast[-1].lower() == dish[-1].lower():
        return True
    else:
        return False

def get_average(marks):
    return sum(marks) // len(marks)


def job_matching(candidate, job):
    'min_salary'== 120000
    'max_salary'== 140000
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Missing salary info") 
    min_salary= candidate['min_salary'] * 0.9
    return min_salary<= job['max_salary']
