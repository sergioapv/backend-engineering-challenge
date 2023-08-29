from moving_average import get_moving_average
import pytest
import json
import os 

TEST_INPUT_FOLDER = 'inputs'
TEST_OUTPUT_FOLDER = 'outputs'

def base_test(input_file:str, window_size:int, expected_output_file:str):
    input_file_path = os.path.join(TEST_INPUT_FOLDER, input_file)
    output_file_path = os.path.join(TEST_OUTPUT_FOLDER, expected_output_file)

    result = get_moving_average(input_file_path, window_size)

    with(open(output_file_path)) as f:
        expected_result = json.load(f)

    assert result == expected_result
    
def test_provided_example():
    base_test('test1_input.json', 10, 'test1_output.json')

def test_repeating_elements():
    base_test('test2_input.json', 10, 'test2_output.json')