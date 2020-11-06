import json
import os
import string

from urllib.request import Request, urlopen
from subprocess import Popen, PIPE

from urllib.error import HTTPError

from powerline.theme import requires_segment_info


def _execute(pl, command):
    git_env = os.environ.copy()
    git_env['LC_ALL'] = 'C'
    proc = Popen(command, stdout=PIPE, stderr=PIPE, env=git_env)
    out, err = [item.decode('utf-8') for item in proc.communicate()]
    if out:
        pl.debug('Command output: %s' % out.strip(string.whitespace))
    if err:
        pl.debug('Command errors: %s' % err.strip(string.whitespace))
    return out.strip(), err.strip()


@requires_segment_info
def latest_build_state(pl, segment_info,
                       canceled_text='Canceled',
                       created_text='Created',
                       errored_text='Errored',
                       failed_text='Failed',
                       for_current_branch=False,
                       git_path='git',
                       passed_text='Passed',
                       post_state_text='',
                       pre_state_text='',
                       received_text='Received',
                       show_state_branch=False,
                       started_text='Started',
                       token=None,
                       username=None,
                       **kwargs):

    if not username or not token:
        pl.error('`username` and `token` are mandatory arguments')
        return
    states_to_text = {
        'canceled': canceled_text,
        'created': created_text,
        'errored': errored_text,
        'failed': failed_text,
        'passed': passed_text,
        'received': received_text,
        'started': started_text
    }
    cwd = segment_info['getcwd']()

    if os.path.isfile(os.path.join(cwd, '.travis.yml')):
        repo_name = os.path.basename(cwd)
        url = 'https://api.travis-ci.com/repo/{}%2F{}/builds?limit=1'.format(username, repo_name)
        if for_current_branch and os.path.isdir(os.path.join(cwd, '.git')):
            command = [git_path, '-C', cwd, 'rev-parse', '--abbrev-ref', 'HEAD']
            current_branch, error = _execute(pl, command)
            if error:
                pl.error('Error when executing {0}, {1}, {2}, {3}, {4}, {5}, {6}', *command, error)
                return
            url += '&branch.name={}'.format(current_branch)

        request = Request(url, headers={'Travis-API-Version': 3,
                                        'User-Agent': 'API Explorer',
                                        'Authorization': 'token {}'.format(token)})

        try:
            response = urlopen(request, timeout=10).read().decode('utf-8')
        except HTTPError as e:
            pl.error('Failed to get response from travis-ci API: {0}', e)
            return
        try:
            json_response = json.loads(response)
            travis_state = json_response['builds'][0]['state']
            state = states_to_text[travis_state]
            branch = json_response['builds'][0]['branch']['name']
        except (json.JSONDecodeError, LookupError, HTTPError):
            pl.error('Got unknown response from travis: {0}. Please open a github issue on https://github.com/DeepSpace2/powerline-travis-ci/issues/new',
                     response)
            return

        travis_url = 'https://travis-ci.com/{}/{}'.format(username, repo_name)
        pre_state_text = pre_state_text.replace('<travis_url>', travis_url)
        post_state_text = post_state_text.replace('<travis_url>', travis_url)
        contents = '{}{} {}{}'.format(pre_state_text, state, (branch if show_state_branch else ''), post_state_text)
        highlight_groups = ['latest_travis_build_state_{}'.format(travis_state), 'latest_travis_build_state']
        pl.debug('Creating segment with content {0} and highlight groups {1}', contents, highlight_groups)
        return [
            {
                'contents': contents,
                'highlight_groups': highlight_groups,
                'divider_highlight_group': 'background:divider'
            }
        ]
