## Example14: 


# List Comprehensions
log_files = ['app.log', 'error.log', 'security.log', 'access.log', 'debug.log', 'system.log']
# Get only the log files starting with a, e 
important_log = [log for log in log_files if log.startswith(('a', 'e'))]
print(f"important logs are {important_log}")

