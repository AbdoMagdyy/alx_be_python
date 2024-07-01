task = input('Enter your task: ')
priority = input('Priority (high/medium/low):')
time_bound = input('Is it time-bound? (yes/no):')
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f'Reminder: {task} is a high priority task that requires immediate attention today!')
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a high priority task that should be completed as soon as possible.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a medium priority task that is due soon. Please complete it by the end of the day.")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a medium priority task that needs to be addressed in a timely manner.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a low priority task that has a deadline. Please review it by the end of the week.")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a low priority task. Please complete it when you have some free time.")
