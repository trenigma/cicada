from pathlib import Path
import json

from job import Job

class AppContext:
    jobs = {}

    def __init__(self):
        # as of yet, we make a lot of assumptions about permissions
        self.data_dir = Path("/var/lib/cicada")
        self.jobs_dir = self.data_dir / "jobs"
        self.workspaces_dir = self.data_dir / "workspaces"

        # setup our working dirs
        for path in [ self.jobs_dir, self.workspaces_dir ]:
            if not path.exists():
                path.mkdir(parents=True)

        # import all jobs
        jobs_dir_listing = list(self.jobs_dir.glob("*.json"))
        for job_file in jobs_dir_listing:
            job = Job(job_file=str(job_file), context=self)
            self.jobs[job.config["name"]] = job

    def get_job_by_name(self, job_name):
       return self.jobs[job_name]
