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
    try:
        return int(stats[1].split()[0]) + int(stats[2].split()[0])
    except:
        try:
            return int(stats[1].split()[0])
        except:
            return 0


def time_to_run(num_changes, min_run_time, max_run_time, changes_at_midpoint):
    """
    Exponentially interpolate the number of seconds the train should run based on the number of changes, between min_run_time and max_run_time.
    Tuned by setting changes_at_midpoint, which is the number of changes required for the train to run for the average of the min and max run times.
    """
    exponent = num_changes * math.log(0.5) / changes_at_midpoint
    return min_run_time + (max_run_time - min_run_time) * (1 - math.exp(exponent))


if __name__ == '__main__':
    while True:
        changes = 0
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
                    changes += git_diff_changes(r, r.commit(lc), r.commit(last_commit))
                    repos[i]['last_commit'] = lc
            except Exception, e:
                print 'Oops.', e

        if changes:
            print 'Choo~~~'
            control.choo()
            control.go(control.FORWARD_SLOW)
            time.sleep(time_to_run(changes, 5, 60, 100))
            print 'Stopped.'
            control.stop()
        time.sleep(5)
        json.dump(repos, open("./repos.json", "w"))
