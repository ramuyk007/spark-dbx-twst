import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from app import pyspark_demo
import pytest
import logging
import pyspark
from pyspark.sql import SparkSession

def quiet_py4j():
    """Suppress spark logging for the test context."""
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)
    
@pytest.fixture(scope="session")
def spark_session(request):
    """Fixture for creating a spark context."""

    spark = (SparkSession
             .builder
             .master("local")
             .getOrCreate())
    request.addfinalizer(lambda: spark.stop())

    quiet_py4j()
    return spark

def test_create_df():
    result = pyspark_demo.create_df()
    assert result == 3
