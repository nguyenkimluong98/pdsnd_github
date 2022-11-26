import time
import pandas as pd
import numpy as np

# Data to be served
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Input the name of city (Chicago, New York City or Washington): ')
    while city.lower().strip() not in CITY_DATA:
        city = input('Invalid city. Please input value in city list!')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Input the month ("january", "february", "march", "april", "may", "june") or input "all" if no month specified: ')
    while month.lower().strip() not in MONTH_DATA:
        month = input('Invalid month. Please input value in month list!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Input the day ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday") or input "all" if no day specified: ')
    while day.lower().strip() not in DAY_DATA:
        day = input('Invalid day. Please input value in day list!')

    city = city.lower().strip()
    month = month.lower().strip()
    day = day.lower().strip()
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print("Loading data with city: {}, month: {}, day: {}".format(city, month, day))
    
    # I do the same Lesson 6. Practice Solution #1
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # I do the same Lesson 10. Practice Solution #3

    # TO DO: display the most common month
    # extracting month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # finding the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', MONTH_DATA[popular_month].capitalize())


    # TO DO: display the most common day of week
    # extracting dayofweek from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # finding the most popular day
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', DAY_DATA[popular_day+1].capitalize())


    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: ', df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('==> User Type:')
        print('- Counts of user types:\n', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        print('==> Gender:')
        print('- Counts of gender:\n', df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('==> Birth Year:')
        print('- Earliest year of birth:\n', df['Birth Year'].min())
        print('- Most recent year of eirth:\n', df['Birth Year'].max())
        print('- Most common year of birth:\n', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        current_iter = 0
        number_data = 5
        
        while True:
            show_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            if show_data.lower() != 'yes':
                break
            
            print(df.iloc[current_iter : current_iter + number_data])
            current_iter += number_data
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
