import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

        
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
    
    
    while True:
      city=input('enter city between these cities: Chicago, New York City, or Washington\n')
      if city.lower() not in ['chicago','new york city','washington']:
             
             print('try again')
     
      else: 
            
         city=city.lower()   
         break
            
      
    print('You chose {}'.format(city.title()))
         

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month=input('enter month between these months: january,february,march,april,may,june,all\n')
      if month.lower() not in ['january','february','march','april','may','june','all']:
           
           print('try again')
        
      else:
        
         month=month.lower()
         break
        
    print('You chose {}'.format(month.title()))
             

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day=input('enter a day between these days: monday,tuesday,wednesday,thursday,friday,saturday,sunday,all\n')
      if day.lower() not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
           
           print('try again')
        
      else:
        
         day=day.lower()
         break
        
    print('You chose {}'.format(day.title()))

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
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    df['month']=df['Start Time'].dt.month
    df['dayofweek']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
    
    months=['january','february','march','april','may','june']
    
    if month!='all':
        month=months.index(month)+1
        df=df[df['month']==month]
    
    if day!='all':
        df=df[df['dayofweek']==day.title()]
    
    
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month: {} '.format(df['month'].mode()))

    # TO DO: display the most common day of week
    print('the most common day: {} '.format(df['dayofweek'].mode()))

    # TO DO: display the most common start hour
    print('the most common hour: {} '.format(df['hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()
    print('the most commonly used start station: {}'.format(start_station))

    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()
    print('the most commonly used end station: {}'.format(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + 'to' + df['End Station']
    combination=df['start_end'].mode()
    print('the most frequent combination start-end station: {}'.format(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel=df['Trip Duration'].sum()
    print('the total of travel time is : {}'.format(total_travel))

    # TO DO: display mean travel time
    
    mean_travel=df['Trip Duration'].mean()
    print('the mean of travel time is : {}'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types=df['User Type'].value_counts()
    print('counts of user type is: \n{}'.format(user_types))

    # TO DO: Display counts of gender
    
    
    if 'Gender' in df.columns:
        user_gender=df['Gender'].value_counts()
        print('\nthe counts of gender is: \n{}'.format(user_gender))
    else:
        print ('nothing')
        
    

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        
        earliest_year=df['Birth Year'].min()
        print('\nthe earliest birth is:  {} '.format(earliest_year))
        most_recent=df['Birth Year'].max()
        print('the most recent birth is: {}'.format(most_recent))
        most_common=df['Birth Year'].mode()[0]
        print('the most common year of birth is: {}'.format(most_common))
        
    else:
        print('nothing')
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    print('\n you want to see raw data ?')
    
    start=0
    end=5
    
    while True:
        user_input = input('write "yes" if you want and "no" if you do not: \n')
        if user_input == 'yes':
            print(df.iloc[start:end])
            print('do you want to see more rows?\n')
        else:
            break
    
        start += start
        end += end
    
    print('will see more statistics')
    
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)                 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
