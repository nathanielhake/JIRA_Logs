import jira from JIRA
from datetime import *
import holidays

# put your user name and password below, don't forget to delete them after you use it
# it's recommended to save your own notebook locally --- just install jira and holidays package
auth_jira = JIRA(server="https://jira9.host.net", basic_auth=('username','password'))

# get your logging issue, if issue not existed, JiraError will be thrown
issue_name = 'your issue name' # your issue name

logging_issue = auth_jira.issue(issue_name)
print(logging_issue.fields.summary)  # check if the issue description matches

# If you need to create a new issue, use the following code

# issue_dict = {
#     'project': {'key': 'your jira project key'},
#     'summary': 'your issue description',
#     'issuetype': {'name': 'Task'},   # 'Task' or 'Story' or 'Bug' etc.
# }

# logging_issue = auth_jira.create_issue(fields=issue_dict)
# issue_name = logging_issue.key

# initialize US holiday
us_holidays = holidays.US(state='NY', years={date.today().year, date.today().year + 1})

# change your begin date and end date for bulk logging (including begin date but not end date)
begin_date = datetime(2020, 1, 17, 9)
end_date = datetime(2020, 1, 30, 9)

for i in range((end_date - begin_date).days):

    # calculate the date in between
    curr_date = begin_date + timedelta(i)

    # if not a holiday or weekend, log 1d of work on that issue, can change to '8h', '4h' if needed, don't double log!
    if curr_date.weekday() in [5, 6] or curr_date in us_holidays:
        pass
    else:
        auth_jira.add_worklog(issue_name, timeSpent='1d', started=curr_date)