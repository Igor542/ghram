import json
import requests

def get_status(branch):
    gh_repo = 'https://api.github.com/repos/evatux/snakex'
    gh_commit = gh_repo + '/commits' + '/' + branch + '/' + 'check-runs'
    print('request: %s', gh_commit)
    gh_answer = requests.get(gh_commit)
    gh_runs = gh_answer.json()['check_runs']
    run_status = ''
    for run in gh_runs:
        run_status += run['conclusion'] + '\n'
    return run_status
