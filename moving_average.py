from datetime import datetime, timedelta
import argparse
import json
import os

parser = argparse.ArgumentParser(description='Moving average delivery times')
parser.add_argument('-i', '--input_file', type=str, required=True,
                    help='Path for the input JSON file')
parser.add_argument('-w', '--window_size', type=int, default=10,
                    help='Moving average window size in minutes')

def get_average_delivery_time(end_date: datetime, parsed_data: dict, window_size: int) -> float:
    start_date: datetime = end_date - timedelta(minutes=window_size)
    durations: list = []
    copy_parsed_data: dict = parsed_data.copy()

    for event_date, duration in parsed_data.items():
        if start_date <= event_date < end_date:
            durations.append(duration)
        #stops searching if the event date if greater than the window end date
        if event_date >= end_date:
            break
        #removes events that are outside of the window start date
        if event_date < start_date:
            del copy_parsed_data[event_date]

    parsed_data = copy_parsed_data

    if len(durations) == 0:
        return 0

    return sum(durations) / len(durations)


def get_moving_average(input_file:str, window_size:int) -> list:

    if not os.path.exists(input_file):
        raise FileNotFoundError('Input file not found')

    with(open(input_file, encoding="utf-8")) as file:
        data = json.load(file)

    result: list = []
    parsed_data: dict = {}

    #parse data into a list of events with datetime as key and duration as value
    for event in data:
        event_date = datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        parsed_data[event_date] = event['duration']

    #get first and last event dates
    first_event_date: datetime = list(parsed_data.keys())[0]
    last_event_date: datetime = list(parsed_data.keys())[-1]

    #get the average for the indicated window size for each minute and add to result
    interval: timedelta = timedelta(minutes=1)
    current_date: timedelta = first_event_date
    while current_date < last_event_date + interval:
        formatted_date: timedelta = current_date.strftime("%Y-%m-%d %H:%M:00")
        result.append({
            'date': formatted_date,
            'average_delivery_time': get_average_delivery_time(current_date, parsed_data, window_size)
        })
        current_date += interval

    return result

def main():
    args = parser.parse_args()
    print(get_moving_average(args.input_file, args.window_size))

if __name__ == '__main__':
    main()
