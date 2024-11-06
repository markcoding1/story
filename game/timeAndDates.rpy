default day = 1
default month = 8
default year = 1
default weekday_index = 4  # 0 = Monday, 1 = Tuesday, etc.
default time_period = "Early Morning"

# List of months with number of days (no leap year for February)
define month_days = {8: 31, 9: 30, 10: 31, 11: 30, 12: 31, 1: 31, 2: 28, 3: 31, 4: 30, 5: 31}
define month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}



# Weekdays and weekend days have different time periods
define weekday_periods = ["Early Morning", "Morning", "Early Afternoon", "Afternoon", "Evening", "Night"]
define weekend_periods = ["Morning", "Afternoon", "Evening", "Night"]
define weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Use an init python block to define the functions
init python:
    # Function to advance to the next time period
    def next_time_period():
        global time_period, weekday_index, day, month, year

        # Determine if it's a weekday or weekend and get the right time periods
        if weekdays[weekday_index] in ["Saturday", "Sunday"]:
            periods = weekend_periods
        else:
            periods = weekday_periods

        # Find the current index in the list of periods
        period_index = periods.index(time_period)

        # If we are at the last time period of the day, move to the next day
        if period_index == len(periods) - 1:
            next_day()
            # After moving to the next day, re-evaluate if it's a weekend or weekday
            if weekdays[weekday_index] in ["Saturday", "Sunday"]:
                time_period = weekend_periods[0]  # Set to "Morning" for weekends
            else:
                time_period = weekday_periods[0]  # Set to "Early Morning" for weekdays
        else:
            time_period = periods[period_index + 1]  # Move to the next period

    # Function to advance to the next day
    def next_day():
        global day, month, year, weekday_index

        # Advance the weekday (Monday -> Tuesday -> etc., looping back after Sunday)
        weekday_index = (weekday_index + 1) % 7

        # Advance the day
        day += 1

        # Check if the day exceeds the number of days in the current month
        if day > month_days[month]:
            day = 1  # Reset to the first day of the new month
            month += 1  # Advance to the next month

            # Check if the month exceeds December (month 12)
            if month > 12:
                month = 1  # Reset to January
                year += 1  # Increment the year if desired

    # Function to add suffix to day
    
    def day_with_suffix(day):
        if 10 <= day % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        return f"{day}{suffix}"




