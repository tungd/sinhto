import os

from fabric.api import cd, env, run, sudo, task
from fabric.contrib import files

PROJECT_NAME = 'sinhto'
PROJECT_ROOT = '/var/www/{}'.format(PROJECT_NAME)
VENV_DIR = os.path.join(PROJECT_ROOT, 'env')
REPO = 'git@github.com:tungd/sinhto.git'

env.hosts = []
env.use_ssh_config = True


@task
def production():
    env.hosts = ['root@172.104.54.197']
    env.environment = 'production'


@task
def bootstrap():
    files.append('~/.bash_profile', 'export PATH="$HOME/.pyenv/bin:$PATH"')
    files.append('~/.bash_profile', 'eval "$(pyenv init -)"')

    if not files.exists('~/.pyenv'):
        run('git clone --depth=1 https://github.com/pyenv/pyenv.git ~/.pyenv')

    if not files.exists('~/.pyenv/versions/3.6.2'):
        run('pyenv install 3.6.2')
        run('pyenv global 3.6.2')
        run('pip install pipenv')

    if not files.exists(PROJECT_ROOT):
        run('git clone {} {}'.format(REPO, PROJECT_ROOT))

    with cd(PROJECT_ROOT):
        run('pipenv install')
        run('pipenv run ./manage.py migrate')
        run('cp config/sinhto.service /etc/systemd/system')
        run('systemctl daemon-reload')
        run('systemctl enable sinhto')
        run('systemctl start sinhto')


@task
def deploy():
    with cd(PROJECT_ROOT):
        run('git checkout package-lock.json')
        run('git pull origin master')

        run('pipenv install')
        run('pipenv run ./manage.py migrate')
        run('npm install')
        run('npm run build')
        run('pipenv run ./manage.py collectstatic --no-input')
        sudo('systemctl restart sinhto')
