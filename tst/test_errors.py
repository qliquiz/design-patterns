from src.error_proxy import error_proxy
from src.argument_exception import argument_exception
from src.operation_exception import operation_exception
import unittest


class test_errors(unittest.TestCase):
    def test_argument_exception(self):
        try:
            raise argument_exception('Test')
        except argument_exception as e:
            assert e.error.is_error == True
            return

        assert 1 != 1


    def test_operation_exception(self):
        try:
            raise operation_exception('Test')
        except operation_exception as e:
            assert e.error.is_error == True
            return

        assert 1 != 1


    def test_check_set_exception(self):
        error = error_proxy()

        try:
            result = 1 / 0
        except Exception as e:
            error.set_error(e)

        assert error.is_error == True
        

    def test_check_error_test(self):
        error = error_proxy('Test', 'Test')

        assert error.is_error == True