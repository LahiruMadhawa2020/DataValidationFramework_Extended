import logging
from readingfiles_utility.testcsv import Testcsv
from config_validation_resultsreport.tablecreation import TbToValidate
from baseconfig_dataProfiling.dataprofiling_base import profilingBase
from validationrules.validation import Validation
from config_validation_resultsreport.testresult import TestResult
import pytest


logging.basicConfig(level='DEBUG')
# logger = log4p.GetLogger(__name__)
# log = logger.logger


@pytest.fixture
def csv_source():
    # test_source = TbToValidate(Testcsv(), utils=utility).get_table(Testcsv.test_date)
    test_source = TbToValidate(Testcsv()).get_table(Testcsv.test_date)
    # print(test_source)
    return test_source


@pytest.mark.run(order=1)
def test_source_profiling_tc01(csv_source):
    profiling_tc01 = profilingBase(csv_source)
    profiling_tc01.sourcedataprofiling()


@pytest.mark.run(order=2)
def test_source_csv_general(csv_source):
    # csv_source_selection = csv_source[(csv_source.Age > 75)]
    result = Validation().run_validation_on(csv_source).expect_column_values_to_be_unique("ID", "Test- Unique value")\
                                                       .expect_column_values_to_not_be_null("ID", "Test- Not Null")\
                                                       .expect_column_value_lengths_to_equal("Name", 4, "Length 4 ")\
                                                       .expect_column_values_to_be_of_type("Name", "object", "data type String only")\
                                                       .expect_column_values_to_be_in_set("Gender", ["M", "F"], "Values in List")\
                                                       .expect_column_values_to_match_regex("Email","(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)","email format check")\
                                                       .get_results()
    # perform PYTest Assertion
    assert TestResult().is_test_passed(result) == 'True'


@pytest.mark.run(order=3)
def test_source_csv_business_validation(csv_source):
    csv_source_selection = csv_source[(csv_source.Age > 75)]
    result = Validation().run_validation_on(csv_source_selection).expect_table_row_count(0, "business validation -1")\
                                                       .get_results()
    # perform PYTest Assertion
    assert TestResult().is_test_passed(result) == 'True'
