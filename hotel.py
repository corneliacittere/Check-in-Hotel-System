"""A hotel with 3 types of accommodation"""

from datetime import date, timedelta


class Hotel:
    """The class that initiates a hotel with 3 types of accommodation"""
    def __init__(self, name, single, double, twin):
        self.hotelName = name.upper()
        self.single = single
        self.double = double
        self.twin = twin

    def rooms_available(self):
        """Displays the Hotel availability"""
        print('At the moment in Hotel {} there are {} Single Rooms, {} Double Rooms and {} Twin Rooms available '.
              format(self.hotelName, self.single, self.double, self.twin))

    def check_in_single_room(self, n, days):
        """Booking a single room in a hotel for a period for a guest"""
        term = date.today() + timedelta(days)
        if n < 1:
            print('The number of rooms should be positive!')
            return None
        elif n > self.single:
            print("Sorry, we don't have enough rooms available!")
            return None
        elif 1 <= n < self.single:
            self.single -= days
            print('You have booked {} Single Room(s) with breakfast in {} Hotel.'.format(n, self.hotelName))
            print('Your booking is available till {}.'.format(term))
            print('We hope you enjoy your stay with us at the {} Hotel!'.format(self.hotelName))

    def check_in_double_room(self, n, days):
        """Booking a double room in a hotel for a period for a guest"""
        term = date.today() + timedelta(days)
        if n < 1:
            print('The number of rooms should be positive!')
            return None
        elif n > self.double:
            print("Sorry, we don't have enough rooms available!")
            return None
        elif 1 <= n < self.double:
            self.double -= days
            print('You have booked {} Double Room(s) in {} Hotel.'.format(n, self.hotelName))
            print('Your booking is available till {}.'.format(term))
            print('We hope you enjoy your stay with us at the {} Hotel!'.format(self.hotelName))

    def check_in_twin_room(self, n, days):
        """Booking a twin room in a hotel for a period for a guest"""
        term = date.today() + timedelta(days)
        if n < 1:
            print('The number of rooms should be positive!')
            return None
        elif n > self.twin:
            print("Sorry, we don't have enough rooms available!")
            return None
        elif 1 <= n < self.twin:
            self.twin -= days
            print('You have booked {} Twin Room(s) in {} Hotel.'.format(n, self.hotelName))
            print('Your booking is available till {}.'.format(term))
            print('We hope you enjoy your stay with us at the {} Hotel!'.format(self.hotelName))

    def check_out(self, k):
        """Creating a bill"""
        room_type, num_of_rooms, date_of_check_in = k
        bill = 0

        # enter date_of_check_in in YYYY-MM-DD format
        # issue a bill only if all three parameters are not null!

        stay = date.today() - date_of_check_in

        if room_type and num_of_rooms and date_of_check_in:
            if room_type == 'single':
                self.single += num_of_rooms
                bill = stay * (num_of_rooms * 40)
            elif room_type == 'double':
                self.double += num_of_rooms
                bill = stay * (num_of_rooms * 70)
            else:
                self.twin += num_of_rooms
                bill = stay * (num_of_rooms * 60)

            #discount calculation
            if bill >= 500:
                bill -= bill * 0.15

            print('Thank you for choosing {} Hotel!'.format(self.hotelName))
            print('That would be {} $'.format(bill))
            return bill

        else:
            print('Are you sure that you are our guest?')
            return None
