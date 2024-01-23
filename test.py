import os
import sys
import pytest
import logging
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from SmartCalender import free_time,meeting_time
from main import main
from datetime import datetime

@pytest.mark.parametrize("schedule, bounds, meeting_duration, expected_result", [
    ( # Test Case 1: Normal case
        [["08:00", "09:30"], ["10:00", "12:00"], ["13:00", "14:30"]],
        ["08:00", "17:00"],
        60,
        [["12:00", "13:00"], ["14:30", "17:00"]]
    ),
    ( # Test Case 2: No free time
        [["09:00", "10:30"], ["11:00", "12:30"]],
        ["09:00", "13:00"],
        60,
        []
    ),
    ( # Test Case 3: Edge case with minimum meeting duration
        [["08:00", "09:00"], ["10:00", "11:00"], ["12:00", "13:00"]],
        ["08:00", "17:00"],
        1,
        [["09:00", "10:00"], ["11:00", "12:00"], ["13:00", "17:00"]]
    ),
    ( # Test Case 4: Edge case with empty schedule
        [],
        ["08:00", "17:00"],
        60,
        None
    ),
],
ids=["NormalCase","NoFreeTime","MinimumMeetingDuration","EmptySchedule"])
def test_free_time(schedule, bounds, meeting_duration, expected_result):
    ''''Test free_time function'''
    if len(schedule)!=0:
        result = free_time(schedule, bounds, meeting_duration)
        assert result == expected_result
    else:
        with pytest.raises(Exception):
            free_time(schedule, bounds, meeting_duration)


@pytest.mark.parametrize("calendar1, calendar2, meeting_duration, expected_result", [
    (
        [["08:00", "09:30"], ["10:00", "12:00"]],
        [["09:00", "10:30"], ["11:00", "12:30"]],
        60,
        [["11:00", "12:00"]]
    )
],
ids=["NormalCase"])
def test_meeting_time_additional(calendar1, calendar2, meeting_duration, expected_result):

    result = meeting_time(calendar1, calendar2, meeting_duration)
    assert result == expected_result

def test_main(caplog):
    '''Test main Function'''
    caplog.set_level(logging.INFO)
    main()
    #assertions to check if the log messages are as expected
    assert "1. possible time for the meeting is" in caplog.text  
