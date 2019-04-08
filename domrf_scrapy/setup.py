

from setuptools import setup, find_packages

setup(
    name =          'domrf_scrapy',
    version =       '0.1',
    packages =      find_packages(exclude=("apply",)),
    # packages = ["dataslap_jobs", "credentials"],
    # package_dir = {
    #                 "credentials" : "credentials",
    #                 "news" : "news"},
    # package_data = {"credenitals" : ["credenitals/passwords.json"]},
    # zip_safe = False,
    zip_safe = True,
    # package_data = {"credenitals" : ["credenitals/passwords.json"]},
    # package_data = {("credenitals", ["credenitals/passwords.json"])},

    include_package_data=True,
    entry_points =  {'scrapy': ['settings = domrf_scrapy.settings']}
)
