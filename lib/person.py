
#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
    def __init__(self,name="unknown",job="unknown"):
        self._name=None
        self._job=None
        self.name=name
        self.job=job
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.") 
    @property
    def job(self):
        return self._job
    @job.setter
    def job(self,job):
        if job in self.approved_jobs:
            self._job=job
        else:
             print("Job must be in list of approved jobs.")
    
