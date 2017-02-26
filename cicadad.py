from flask import Flask
from context import AppContext
from job import Job

app = Flask(__name__)

@app.route("/job/<job_name>/build", methods=['POST'])
def build(job_name):
    job = context.get_job_by_name(job_name)
    job.build()
    return '', 204

if __name__ == "__main__":
    context = AppContext()
    app.run()
