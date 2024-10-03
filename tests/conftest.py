import logging
import pytest
from concurrent_log_handler import ConcurrentRotatingFileHandler
import pytest

# usage for fixture based data driven testing
from utils.data_utils import DataUtils
from utils.db_utils import DBUtils

@pytest.fixture
def get_csv_data():
    return DataUtils.read_csv('data/test_data.csv')

@pytest.fixture
def get_db_data():
    query = "SELECT * FROM test_table"
    return DBUtils.fetch_data(query)



# logging for parallel testexecutions
@pytest.fixture(autouse=True)
def test_case_logging(request):
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        # Use ConcurrentRotatingFileHandler to prevent race conditions
        handler = ConcurrentRotatingFileHandler('logs/test_logs.log', backupCount=10)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.info(f"Start of test case: {request.node.name}")

    yield logger

    logger.info(f"End of test case: {request.node.name}")

# failure screenshots configurations
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        page = item.funcargs.get("page")
        screenshot_path = f"screenshots/failure_screenshots/{item.name}.png"
        page.screenshot(path=screenshot_path)
