import json
import math
import time

from git import Repo

import control

repos = json.load(open("./repos.json"))


def git_diff_changes(repo, commit_1, commit_2):
    """
    Description:
        Get the Number of changes that occured between two commits
    Keyword Arguments:
        repo: a GitPython repo object
        commit_1: a GitPython commit object
        commit_2: a GitPython commit object
    Return:
        returns the value of --shortstat in dictionary form
    """
    git = repo.git
    commit_1_hash = commit_1.hexsha
    commit_2_hash = commit_2.hexsha
    short_stats = git.diff("--shortstat", commit_1_hash, commit_2_hash)
    stats = short_stats.split(',')
    return {
        'files_changed': int(stats[0].split()[0]),
        'insertions': int(stats[1].split()[0]),
        'deletions': int(stats[2].split()[0]),
    }

def time_to_run(num_changes, min_run_time, max_run_time):
    """
    Description:
        Get the Number of changes that occured between two commits
    Keyword Arguments:
        num_changes: int representing the number of changes
    Return:
        number of seconds the train should run for in seconds
    """
    magic_num = 15
    fraction_of_time_to_run = 1 / (magic_num + math.exp(-num_changes))
    time_to_run = fraction_of_time_to_run * max_run_time
    if time_to_run < min_run_time:
        return min_run_time
    else:
        return time_to_run

while True:
    run_train = False
    for i, repo in enumerate(repos):
        path = repo['path']
        print path
        last_commit = repo['last_commit']
        branch = repo['branch']
        r = Repo(path)
        try:
            r.remotes.origin.pull()
            lc = r.commit(branch).hexsha
            if lc != last_commit:
                run_train = True
                repos[i]['last_commit'] = lc
        except Exception, e:
            print 'Oops.', e

    if run_train:
        print 'Choo~~~'
        control.choo()
        control.go(control.FORWARD_SLOW)
        time.sleep(7)
        print 'Stopped.'
        control.stop()
    time.sleep(5)
    json.dump(repos, open("./repos.json", "w"))
