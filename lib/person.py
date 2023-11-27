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
    approved_jobs = ["Engineer", "Teacher", "Doctor", "Artist", "Programmer"]

    def __init__(self, name, job):
        self._name = None  # Use a private attribute to store the name
        self._job = None  # Use a private attribute to store the job
        self.name = name  # Use the property setter for validation
        self.job = job  # Use the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
