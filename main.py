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


def close_compare(a, b, margin=0):
    if abs(a-b) <= margin:
        return 0
    if a < b:
        return -1
    else:
        return 1


##24/03/2026
def quarter_of(month):
    return (month - 1) // 3 + 1

#25/03/2026

def triple_trouble(one, two, three):
    result = ""
    for i in range(len(one)):
        result = one[i] + two[i] + three[i]
    return result

def make_upper_case(s):
  return s.upper()

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))


def duplicate_count(text):
    return sum(text.lower().count(c) > 1 for c in set(text.lower()))

##26/03/2026


a = "code"
b = "wa.rs"

name = a + b
print(name)
