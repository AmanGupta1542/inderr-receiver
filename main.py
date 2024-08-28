
from reciever_mod import receiver, tk_window
import datetime
from decimal import Decimal
import os

DATA = {
    'train': {'name': 'Rajya Rani Express', 'number': 22161, 'from_station': 'Bhopal Junction', 'to_station': 'Damoh'}, 
    'stations': [
            {'name': 'Bhopal Junction', 'abbr': 'BPL', 'distance': None, 'order': 1, 'estimate_time': None, 'depart_time': datetime.time(17, 55), 'lat': Decimal('23.266717'), 'lon': Decimal('77.412920'), 'halt_time': None}, 
            {'name': 'Vidisha', 'abbr': 'BHS', 'distance': None, 'order': 2, 'estimate_time': datetime.time(18, 32), 'depart_time': datetime.time(18, 34), 'lat': Decimal('23.522687'), 'lon': Decimal('77.815174'), 'halt_time': 2}, 
            {'name': 'Ganj Basoda', 'abbr': 'BAQ', 'distance': None, 'order': 3, 'estimate_time': datetime.time(19, 2), 'depart_time': datetime.time(19, 3), 'lat': Decimal('23.846135'), 'lon': Decimal('77.944559'), 'halt_time': 2}, 
            {'name': 'Mandi Bamora', 'abbr': 'MABA', 'distance': None, 'order': 4, 'estimate_time': datetime.time(19, 27), 'depart_time': datetime.time(19, 28), 'lat': Decimal('24.053588'), 'lon': Decimal('78.082580'), 'halt_time': 2}, 
            {'name': 'Bina', 'abbr': 'BINA', 'distance': None, 'order': 5, 'estimate_time': datetime.time(19, 55), 'depart_time': datetime.time(20, 0), 'lat': Decimal('24.172716'), 'lon': Decimal('78.184876'), 'halt_time': 2}, 
            {'name': 'Khurai', 'abbr': 'KYE', 'distance': None, 'order': 6, 'estimate_time': datetime.time(20, 30), 'depart_time': datetime.time(20, 32), 'lat': Decimal('24.053327'), 'lon': Decimal('78.330431'), 'halt_time': 2}, 
            {'name': 'Saugor', 'abbr': 'SGO', 'distance': None, 'order': 7, 'estimate_time': datetime.time(21, 22), 'depart_time': datetime.time(21, 25), 'lat': Decimal('23.847723'), 'lon': Decimal('78.744192'), 'halt_time': 2}, 
            {'name': 'Makronia', 'abbr': 'MKRN', 'distance': None, 'order': 8, 'estimate_time': datetime.time(21, 36), 'depart_time': datetime.time(21, 38), 'lat': Decimal('23.866749'), 'lon': Decimal('78.809547'), 'halt_time': 2}, 
            {'name': 'Ganeshganj', 'abbr': 'GAJ', 'distance': None, 'order': 9, 'estimate_time': datetime.time(22, 3), 'depart_time': datetime.time(22, 5), 'lat': Decimal('23.895494'), 'lon': Decimal('79.073202'), 'halt_time': 2}, 
            {'name': 'Patharia', 'abbr': 'PHA', 'distance': None, 'order': 10, 'estimate_time': datetime.time(22, 18), 'depart_time': datetime.time(22, 20), 'lat': Decimal('23.905831'), 'lon': Decimal('79.192505'), 'halt_time': 2}, 
            {'name': 'Damoh', 'abbr': 'DMO', 'distance': None, 'order': 11, 'estimate_time': datetime.time(22, 45), 'depart_time': None, 'lat': Decimal('23.835631'), 'lon': Decimal('79.431790'), 'halt_time': 2}
        ], 
    # 'next_station': {'name': 'Vidisha', 'lat': Decimal('23.522687'), 'lon': Decimal('77.815174'), 'order': 2, 'distance': 49.70376998384893}, 
    'next_station': {'name': 'Sagar', 'lat': Decimal('23.847723'), 'lon': Decimal('78.744192'), 'order': 7, 'distance': 52.8}, 
    'curr_location': {'lat': Decimal('23.847723'), 'lon': Decimal('78.744192')}, 
    'speed': 0, 
    'late_by': 0
}

DATA = {
    'train': {'name': 'Rajya Rani Express', 'number': 22161, 'from_station': 'Bhopal Junction', 'to_station': 'Damoh'}, 
    'stations': [
            {'name': 'Bhopal Junction', 'abbr': 'BPL', 'distance': None, 'order': 1, 'estimate_time': None, 'depart_time': '17:55', 'lat': '23.266717', 'lon': '77.412920', 'halt_time': None}, 
            {'name': 'Vidisha', 'abbr': 'BHS', 'distance': 53.4, 'order': 2, 'estimate_time': '18:32', 'depart_time': '18:34', 'lat': '23.522687', 'lon': '77.815174', 'halt_time': 2}, 
            {'name': 'Ganj Basoda', 'abbr': 'BAQ', 'distance': 39.5, 'order': 3, 'estimate_time': '19:02', 'depart_time': '19:03', 'lat': '23.846135', 'lon': '77.944559', 'halt_time': 2}, 
            {'name': 'Mandi Bamora', 'abbr': 'MABA', 'distance': None, 'order': 4, 'estimate_time': '19:27', 'depart_time': '19:28', 'lat': '24.053588', 'lon': '78.082580', 'halt_time': 2}, 
            {'name': 'Bina', 'abbr': 'BINA', 'distance': None, 'order': 5, 'estimate_time': '19:55', 'depart_time': '20:00', 'lat': '24.172716', 'lon': '78.184876', 'halt_time': 2}, 
            {'name': 'Khurai', 'abbr': 'KYE', 'distance': None, 'order': 6, 'estimate_time': '20:30', 'depart_time': '20:32', 'lat': '24.053327', 'lon': '78.330431', 'halt_time': 2}, 
            {'name': 'Saugor', 'abbr': 'SGO', 'distance': None, 'order': 7, 'estimate_time': '21:22', 'depart_time': '21:25', 'lat': '23.847723', 'lon': '78.744192', 'halt_time': 2}, 
            {'name': 'Makronia', 'abbr': 'MKRN', 'distance': None, 'order': 8, 'estimate_time': '21:36', 'depart_time': '21:38', 'lat': '23.866749', 'lon': '78.809547', 'halt_time': 2}, 
            {'name': 'Ganeshganj', 'abbr': 'GAJ', 'distance': None, 'order': 9, 'estimate_time': '22:03', 'depart_time': '22:05', 'lat': '23.895494', 'lon': '79.073202', 'halt_time': 2}, 
            {'name': 'Patharia', 'abbr': 'PHA', 'distance': None, 'order': 10, 'estimate_time': '22:18', 'depart_time': '22:20', 'lat': '23.905831', 'lon': '79.192505', 'halt_time': 2}, 
            {'name': 'Sagar', 'abbr': 'DMO', 'distance': None, 'order': 11, 'estimate_time': '22:45', 'depart_time': None, 'lat': '23.835631', 'lon': '79.431790', 'halt_time': 2}
        ], 
    'next_station': {'name': 'Sagar', 'lat': Decimal('23.847723'), 'lon': Decimal('78.744192'), 'order': 7, 'distance': 52.8}, 
    'curr_location': {'lat': Decimal('23.847723'), 'lon': Decimal('78.744192')}, 
    'speed': 0, 
    'late_by': 30
}

DATA = {'train': {'name': 'Rajya Rani Express', 'number': 22161, 'from_station': 'Bhopal Junction', 'to_station': 'Damoh'}, 'stations': [{'name': 'Bhopal Junction', 'lat': '23.266717', 'lon': '77.412920', 'curr_lat': '23.528112', 'curr_lon': '77.822980', 'order': 1, 'remaining_distance': 50.95106671196291, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'BPL', 'distance': None, 'total_distance': 0, 'estimate_time': None, 'depart_time': '17:55', 'halt_time': None}, {'name': 'Vidisha', 'lat': '23.522687', 'lon': '77.815174', 'curr_lat': '23.528112', 'curr_lon': '77.822980', 'order': 2, 'remaining_distance': 0.9986270153232826, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'BHS', 'distance': 53.4, 'total_distance': 53.4, 'estimate_time': '18:32', 'depart_time': '18:34', 'halt_time': 2, 'total_time_to_reach': '2024-06-01T11:04:39.596061', 'instant_distance': 0, 'instant_speed': 43, 'late_by': 'Train is early by 7 hours 27 minutes'}, {'name': 'Ganj Basoda', 'lat': '23.846135', 'lon': '77.944559', 'curr_lat': '23.528112', 'curr_lon': '77.822980', 'order': 3, 'remaining_distance': 37.46697406355163, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'BAQ', 'distance': 39.5, 'total_distance': 92.9, 'estimate_time': '19:02', 'depart_time': '19:03', 'halt_time': 2}, {'name': 'Mandi Bamora', 'lat': '24.053588', 'lon': '78.082580', 'curr_lat': '23.528112', 'curr_lon': '77.822980', 'order': 4, 'remaining_distance': 64.12292001587963, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'MABA', 'distance': 28.4, 'total_distance': 121.30000000000001, 'estimate_time': '19:27', 'depart_time': '19:28', 'halt_time': 2}, {'name': 'Bina', 'lat': '24.172716', 'lon': '78.184876', 'curr_lat': '23.528112', 'curr_lon': '77.822980', 'order': 5, 'remaining_distance': 80.5735866037869, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'BINA', 'distance': 17.4, 'total_distance': 138.70000000000002, 'estimate_time': '19:55', 'depart_time': '20:00', 'halt_time': 2}, {'name': 'Khurai', 'lat': '24.052270', 'lon': '78.331110', 'curr_lat': 
'23.528112', 'curr_lon': '77.822980', 'order': 6, 'remaining_distance': 77.90954875478027, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'KYE', 'distance': 21.7, 'total_distance': 160.4, 'estimate_time': '20:30', 'depart_time': '20:32', 'halt_time': 2}, {'name': 'Saugor', 'lat': '23.847723', 'lon': '78.744192', 'curr_lat': '23.528112', 'curr_lon': '77.822980', 'order': 7, 'remaining_distance': 100.31005435542784, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'SGO', 'distance': 52.8, 'total_distance': 213.2, 'estimate_time': '21:22', 'depart_time': '21:25', 'halt_time': 2}], 'get_ack': '', 'next_station': {'name': 'Bina', 'lat': '24.172716', 'lon': '78.184876', 'curr_lat': '24.171163', 'curr_lon': '78.183109', 'order': 5, 'remaining_distance': 0.24890236706655017, 'is_crossed': True, 'actual_arrival_time': '2024-06-03T18:35:49.537473', 'actual_departure_time': False, 'abbr': 'BINA', 'distance': 17.4, 'total_distance': 138.70000000000002, 'estimate_time': '19:55', 'depart_time': '20:00', 'halt_time': 2, 'total_time_to_reach': '2024-06-03T18:36:09.018789', 'instant_distance': 9.51, 'instant_speed': 46, 'late_by': 'Train is early by 1 hour 18 minutes'}, 'speed': 0, 'late_by': 0}
update_data = {'next_station': {'name': 'Khurai', 'lat': '24.052270', 'lon': '78.331110', 'curr_lat': '24.065403', 'curr_lon': '78.322474', 'order': 6, 'remaining_distance': 
1.7033560828139973, 'is_crossed': False, 'actual_arrival_time': False, 'actual_departure_time': False, 'abbr': 'KYE', 'distance': 21.7, 'total_distance': 160.4, 'estimate_time': '20:30', 'depart_time': '20:32', 'halt_time': 2, 'total_time_to_reach': '2024-06-03T18:44:58.049142', 'instant_distance': 2.26, 'instant_speed': 32, 'late_by': 'Train is early by 1 hour 45 minutes'}}

if __name__ == '__main__':
    # if os.environ.get('DISPLAY', '') == '':
    #     print("No display found. Using dummy display.")
    #     os.environ['DISPLAY'] = ':0'
    
    dd = tk_window.DisplayDesign()
    dd.run(DATA)
    dd.update_data(update_data)

    # listen = receiver.Receiver()
    # listen.main()

