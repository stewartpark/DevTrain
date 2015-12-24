from git import Repo
import json
import control
import time

repos = json.load(open("./repos.json"))

while True:
    run_train = False
    for i, repo in enumerate(repos):
        path = repo['path']
        print path
        last_commit = repo['last_commit']
        branch = repo['branch']
        
        lc = Repo(path).commit(branch).hexsha
        if lc != last_commit:
            run_train = True
            repos[i]['last_commit'] = lc

    if run_train:
        print 'Chu chu~~~'
        control.go(control.FORWARD_SLOW)
        time.sleep(5)
        control.stop()
        print 'Stopped.'
    time.sleep(5)
    json.dump(repos, open("./repos.json", "w"))    
