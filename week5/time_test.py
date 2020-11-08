import pytest
from times import compute_overlap_time, time_range
import yaml
import os


with open(os.path.join(os.path.dirname(__file__),'fixture.yaml'), 'r') as e:
    fixture = yaml.safe_load(e)
    print(fixture)


@pytest.mark.parametrize("test_name", fixture)
# fixture is a list of dictionaries [{'generic':...}, {'no_overlap':...}, ...]
def test_time_range_overlap(test_name):
    # test_name will be a dictionary, e.g. for the first case: {'generic': {'time_range_1':..., 'time_range2':..., 'expected':...}
    properties = list(test_name.values())[0]
    first_range = time_range(*properties['time_range_1'])
    second_range = time_range(*properties['time_range_2'])
    expected_overlap = [(start, stop) for start, stop in properties['expected']]
    assert compute_overlap_time(first_range, second_range) == expected_overlap

def test_negative_time_range():
    with pytest.raises(ValueError) as e:
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
        assert e.match('The end of the time range has to come strictly after its start.')
