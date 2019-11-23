import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': ['Chicago', 'chicago.csv'],
              'n' : ['new york city', 'new_york_city.csv'],
              'w': ['Washington', 'washington.csv']}

MONTH_DICT = {'january' : 1,
               'february' : 2,
                'march' :3,
                 'april' : 4,
                  'may' : 5,
                   'june' : 6,
                    'july' : 7,
                     'august' : 8,
                      'september' : 9,
                       'october' : 10,
                        'november' : 11,
                         'december' : 12}

DAY_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Set up default configuration:
    city = []
    month = 0
    day = 'all'
    
    citykey = ''
    while citykey not in CITY_DATA.keys():
        # apply lower() to input to avoid case sensitivity
        citykey =  input("""\nThe data for which city would you like to explore? Chicago (c), New york City (n) or Washington (w)
Type 'c', 'n' or 'w'\n""").lower()
    city = CITY_DATA[citykey]
    print("You chose " + city[0] + ".\n")
    
    filterinput = ''
    while (filterinput not in ['m', 'd','n']):
        filterinput = input("\nWould you like to filter the data by month(m), day(d), or not at all(n)?\nType 'm', 'd' or 'n'\n")

    if filterinput == 'm':
        monthinput = ''
        while monthinput not in (list(MONTH_DICT.keys()) + [str(i) for i in range(1,13)]):
            monthinput = input("\nWhich month would you like to explore?\nType month name (january, ..., december) or number 1-12.\n").lower()
            print(monthinput)
        if (monthinput in MONTH_DICT.keys()):
            month = MONTH_DICT[monthinput]
        else:
            month = int(monthinput)
        print("You chose month " + str(month) + ".\n")
    elif filterinput == 'd':
        dayinput = ''
        while dayinput not in DAY_LIST:
            dayinput = input('\nWhich day of the week would you like to explore? (monday, tuesday, ..., sunday)\n').lower()
        day = dayinput.capitalize()
        print("You chose " + day + ".\n")   
    
    
   
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        List city - city[0] name of the city to analyze, city[1] name of the csv file
        int month - number of the month to filter by, or 0 to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day, None if dataframe is empty
    """
    cityfile = city[1]

    df = pd.read_csv(cityfile)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
    
    if (day != 'all'):
        df = df[df['day_of_week'] == day]
    
    if (month != 0):
        df = df[df['month'] == month]

    if df.shape[0] == 0:
        df = None

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    monthmode = df['month'].mode()[0]
    print("The most common month is: " + str(monthmode))

    


    # TO DO: display the most common day of week
    dowmode = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + dowmode)

    # TO DO: display the most common start hour
    hourmode = df['hour'].mode()[0]
    print("The most common start hour is: " + str(hourmode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstationmode = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + startstationmode)


    # TO DO: display most commonly used end station
    endstationmode = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + endstationmode)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " - " + df['End Station']
    combinationmode = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is: " + combinationmode)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttl_traveltime = df['Trip Duration'].sum()
    print("The total travel time was " + str(ttl_traveltime) + " seconds (" + str(round(ttl_traveltime/3600.0,2)) + " hours).")

    # TO DO: display mean travel time
    avg_traveltime = df['Trip Duration'].mean()
    print("The mean travel time was " + str(avg_traveltime) + " seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nCounts of user types:")
    print(str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if ('Gender' in df.columns):
        print("\nCounts of gender:")
        print(str(df['Gender'].value_counts()))
    else:
        print("No Gender data")


    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df.columns):
        print("\nEarliest year of birth: " + str(int(df['Birth Year'].min())))
        print("Most recent year of birth: " + str(int(df['Birth Year'].max())))
        print("Most common year of birth: " + str(int(df['Birth Year'].mode()[0])))
    else:
        print("No Birth Year data.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_rawdata(df):
    """Displays raw data."""
    print('\nDo you want to see any raw data?')
    response =''
    while (response not in ['yes', 'no']):
        response = input("Type 'yes' or 'no'\n").lower()
    if (response == 'yes'):
        i = 0
        
        print("showing raw data rows " + str(i + 1) + " - " + str(i+5) + ":\n")
        print(df.iloc[i:i+5])
        response = ''
        while (response != 'no'):
            print("Do you want to see more data?")
            response = input("'yes' or 'no':\n").lower()
            if (response == 'yes'):
                i = i + 5
                if (i <= df.shape[0]):
                    print("showing raw data rows " + str(i + 1) + " - " + str(i+5) + ":")
                    print(df.iloc[i:i+5])
                else:
                    print("No more data!")
                    break
            
        



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if (df is not None):
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_rawdata(df)
        else: 
            print("No data to display!")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
