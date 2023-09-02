# Solution for task: https://www.codewars.com/kata/56c22c5ae8b139416c00175d/

def job_matching(candidate: dict, job: dict) -> bool:
    return candidate['min_salary'] - (candidate['min_salary'] * 0.1) <= job['max_salary'] 
