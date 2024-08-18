from .main import get_hours_minutes_seconds


class TestMain:
    def test_get_houts_minutes_seconds_0_seconds(self):
        elapsed_time = 0.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 0
        assert int(seconds) == 0

    def test_get_houts_minutes_seconds_1_seconds(self):
        elapsed_time = 1.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 0
        assert int(seconds) == 1

    def test_get_houts_minutes_seconds_59_seconds(self):
        elapsed_time = 59.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 0
        assert int(seconds) == 59

    def test_get_houts_minutes_seconds_60_seconds(self):
        elapsed_time = 60.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 1
        assert int(seconds) == 0

    def test_get_houts_minutes_seconds_61_seconds(self):
        elapsed_time = 61.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 1
        assert int(seconds) == 1

    def test_get_houts_minutes_seconds_121_seconds(self):
        elapsed_time = 121.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 2
        assert int(seconds) == 1

    def test_get_houts_minutes_seconds_3599_seconds(self):
        elapsed_time = 3599.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 0
        assert int(minute) == 59
        assert int(seconds) == 59

    def test_get_houts_minutes_seconds_3600_seconds(self):
        elapsed_time = 3600.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 1
        assert int(minute) == 0
        assert int(seconds) == 0

    def test_get_houts_minutes_seconds_3601_seconds(self):
        elapsed_time = 3601.0
        hours, minute, seconds = get_hours_minutes_seconds(elapsed_time)
        assert int(hours) == 1
        assert int(minute) == 0
        assert int(seconds) == 1
