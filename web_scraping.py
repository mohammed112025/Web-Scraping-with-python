"""
    This module for scrap subpage of wuzzaf.com and know some
    information about the latest jobs for a specific possition
"""
import csv
from itertools import zip_longest
import requests
from bs4 import BeautifulSoup

titles = []
skills = []
names = []
locations = []

# Access the page of data analysis job of wuzzuf website
open1 = requests.get("https://wuzzuf.net/search/jobs/?q=Data+analysis&a=hpb")

# Save the content of the page
Jobs = BeautifulSoup(open1.content, "lxml")

# Scrip pages
job_title = Jobs.find_all("h2", {"class": "css-m604qf"})
job_skills = Jobs.find_all("div", {"class": "css-y4udm8"})
company_name = Jobs.find_all("a", {"class": "css-17s97q8"})
company_location = Jobs.find_all("span", {"class": "css-5wys0k"})
num_jobs = len(job_title)

# save the important info in lists
for i in range(num_jobs):
    titles.append(job_title[i].text)
    skills.append(job_skills[i].text)
    names.append(company_name[i].text)
    locations.append(company_location[i].text)

# Creat a csv file include the important info
job_info = [titles, names, locations, skills]
combineLists = zip_longest(*job_info)

with open(r"D:\Data Science\Python\Projects\Web-Scraping\New-Jobs.csv", "w", encoding="utf-8") as jobs:
    writer = csv.writer(jobs)
    writer.writerow(["Job Title", "Company Location",
                     "Company Name", "Job Skills"])
    writer.writerows(combineLists)
jobs.close()
