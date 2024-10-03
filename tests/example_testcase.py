# this is example of how the logging will be performed in testcases

def test_login(test_case_logging):
    logger = test_case_logging
    logger.info("Attempting to log in")

    # Test actions go here
    assert 1 == 1

    logger.info("Login test completed")


# usage of data_utils to perform datadriven testing
from utils.data_utils import DataUtils

def test_data_driven_with_csv():
    data = DataUtils.read_csv('data/test_data.csv')
    for row in data:
        # Use the data in the test
        assert len(row) > 0


from utils.db_utils import DBUtils

def test_data_driven_with_db():
    query = "SELECT * FROM test_table"
    data = DBUtils.fetch_data(query)
    for row in data:
        # Use the data in the test
        assert row is not None
