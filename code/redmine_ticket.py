from redmine import Redmine
# python-redmine.readthedocs.io/configuration.html
redmine = Redmine('url')
redmine.issue.create()
