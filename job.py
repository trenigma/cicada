from pathlib import Path
import json, shlex, subprocess

class Job:
    def __init__(self, job_file=None, context=None):
        if job_file:
            # open our job's configuration
            # TODO: handle misconfig/bad format json
            with open(job_file, 'r') as file:
                text = file.read()
                self.config = json.loads(text)
            self.config['job_file'] = job_file
            self.config['workspace'] = str(context.workspaces_dir / self.config['name'])

    def update_repo(self):
        # TODO: instead of deleting & re-cloning the repo, clone only if it doesn't exist,
        # and pull/update the HEAD if it does
        print("calling update_repo")

        repo_dir = self.config['workspace'] + "/" + self.config['repo']['name']

        remove_repo_cmd = shlex.split("rm -rf " + repo_dir)
        remove_repo = subprocess.Popen(remove_repo_cmd, cwd=self.config['workspace'])
        remove_repo.wait()

        clone_repo_cmd = shlex.split("git clone " + self.config['repo']['url'])
        clone_repo = subprocess.Popen(clone_repo_cmd, cwd=self.config['workspace'])
        clone_repo.wait()

        checkout_rev_cmd = shlex.split("git checkout " + self.config['repo']['ref'])
        checkout_rev = subprocess.Popen(checkout_rev_cmd, cwd=repo_dir)
        checkout_rev.wait()

    def build(self):
        # we should put a shiv here for env vars in the config
        if not Path(self.config['workspace']).exists():
            Path(self.config['workspace']).mkdir()
        self.update_repo()
        build_file = self.config['workspace'] + "/" + self.config['repo']['name'] + "/" + self.config['build_file']
        build_file_cmd = shlex.split(build_file)
        Path(build_file).chmod(0o500)
        status = subprocess.call(build_file_cmd, shell=True, cwd=self.config['workspace'])
