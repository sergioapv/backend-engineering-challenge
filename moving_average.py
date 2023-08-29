from datetime import datetime, timedelta
import argparse
import json 
import os

parser = argparse.ArgumentParser(description='Moving average delivery times')
parser.add_argument('-i', '--input_file', type=str, required=True, help='Path for the input JSON file')
parser.add_argument('-w', '--window_size', type=int, default=10, help='Moving average window size in minutes')

def get_average_delivery_time(current_date, parsed_data, window_size):
    end_date = current_date
    start_date = current_date - timedelta(minutes=window_size)
    durations = []
    for event_date, duration in parsed_data.items():
        if event_date >= start_date and event_date < end_date:
            durations.append(duration)
    if len(durations) == 0:
        return 0
    else:
        return sum(durations) / len(durations)


def moving_average(input_file, window_size):
    if os.path.exists(input_file):
        with(open(input_file)) as f:
            result = []
            parsed_data = {}
            data = json.load(f)

            for event in data:
                event_date = datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                parsed_data[event_date] = event['duration']

            #get first and last event dates in datetime format without factoring in seconds    
            first_event_date = list(parsed_data.keys())[0]
            last_event_date = list(parsed_data.keys())[-1]

            interval = timedelta(minutes=1)
            current_date = first_event_date
            while current_date < last_event_date:
                formatted_date = current_date.strftime("%Y-%m-%d %H:%M:00")
                result.append({
                    'date': formatted_date,
                    'average_delivery_time': get_average_delivery_time(current_date, parsed_data, window_size)
                })
                current_date += interval

            #get the average for the last window
            formatted_date = current_date.strftime("%Y-%m-%d %H:%M:00")
            result.append({
                'date': formatted_date,
                'average_delivery_time': get_average_delivery_time(current_date, parsed_data, window_size)
            })
            print(result)
    else:
        raise Exception('Input file not found')





def main():
    args = parser.parse_args()
    moving_average(args.input_file, args.window_size)

if __name__ == '__main__':
    main()