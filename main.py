from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
from flask import Flask

app = Flask("JobScrapper")
app.run("0.0.0.0")



'''
keyword = input('what do you want to search for?')

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)
'''
