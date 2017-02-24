def jobs_schedule(jobs, i):
    '''
    INPUT: List, Int
    OUTPUT: Int

    If the given integer is 0, then return the jobs schedule as ordered by the
    difference between the job's weight and length. Otherwise, return the jobs
    schedule as ordered by the ratio between the job's weight and its length.
    '''
    if i == 0:
        return jobs_schedule_difference(jobs)
    return jobs_schedule_ratio(jobs)


def jobs_schedule_difference(jobs):
    '''
    INPUT: List
    OUTPUT: Int

    Sort the jobs by the difference between a job's weight (the first number in
    the job's tuple) and its length (the second number in the job's tuple). If
    the difference is the same, then order by the job's weight. Lastly, return
    the weighted completion time of all of the jobs, given the sorted order.
    '''
    jobs = sorted(jobs, key=lambda j: ((j[0] - j[1]), j[0]), reverse=True)
    return sum_weighted_completion_times(jobs)


def jobs_schedule_ratio(jobs):
    '''
    INPUT: List
    OUTPUT: Int

    Sort the jobs by the ratio between a job's weight (the first number in the
    job's tuple) and its length (the second number in the job's tuple). Return
    the weighted completion time of all of the jobs, given the sorted order.
    '''
    jobs = sorted(jobs, key=lambda j: (j[0] / j[1]), reverse=True)
    return sum_weighted_completion_times(jobs)


def sum_weighted_completion_times(jobs):
    '''
    INPUT: List
    OUTPUT: Int

    Calculate the total completion time of a list of jobs, given their weights.
    '''
    sum_total = 0
    sum_length = 0
    for job in jobs:
        sum_length += job[1]
        sum_total += job[0] * sum_length
    return sum_total


if __name__ == '__main__':
    with open('jobs.txt') as f:
        # The first line of the file contains the number of jobs; keep or skip.
        num_jobs = int(f.readline())
        # Each subsequent line corresponds to a job, with a weight and length.
        jobs = [tuple(map(int, line.split())) for line in f]

    print('Difference:\t{}'.format(jobs_schedule(jobs, 0)))
    # Answer = 69119377652
    print('Ratio:\t{}'.format(jobs_schedule(jobs, 1)))
    # Answer = 67311454237
