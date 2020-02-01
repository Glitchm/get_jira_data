from classes import *
import pandas as pd

project_info = Jira_info('project')

data = pd.DataFrame(project_info.get_info())

print(data.name)