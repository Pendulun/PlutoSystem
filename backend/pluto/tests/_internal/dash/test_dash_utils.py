import pytest

from tests._internal.mocks import DashCallbacksUtilMock
from pluto._internal.domain.model.expense import Expense

class TestDashCallbacksUtil:

    def test_can_generate_last_twelve_months_list(self):
        month_year_fmt = DashCallbacksUtilMock.month_year_fmt
        expected_list = ['5/2023', '4/2023', '3/2023',
                         '2/2023', '1/2023', '12/2022',
                         '11/2022', '10/2022', '9/2022',
                         '8/2022', '7/2022', '6/2022']
        expected_list.reverse()
        assert expected_list == DashCallbacksUtilMock.get_last_twelve_months_str_list(month_year_fmt)
    
    def test_can_get_total_of_expenses_per_month(self):
        last_twelve_months = ['5/2023', '4/2023', '3/2023',
                         '2/2023', '1/2023', '12/2022',
                         '11/2022', '10/2022', '9/2022',
                         '8/2022', '7/2022', '6/2022']
        last_twelve_months.reverse()
        exp1_dict = {
            'id': '1',
            'user_id': '1',
            'src': 'EPA',
            'amount': 10,
            'exp_date': '01/01/2023'
        }
        exp2_dict = {
            'id': '2',
            'user_id': '1',
            'src': 'Padaria 24 horas',
            'amount': 15,
            'exp_date': '01/02/2023'
        }
        exp3_dict = {
            'id': '3',
            'user_id': '1',
            'src': 'Farmácia',
            'amount': 5,
            'exp_date': '01/03/2023'
        }
        exp1 = Expense.from_complete_dict(exp1_dict)
        exp2 = Expense.from_complete_dict(exp2_dict)
        exp3 = Expense.from_complete_dict(exp3_dict)
        exp_list = [exp1, exp2, exp3]
        expected_expenses_per_month = {
            '5/2023':0, '4/2023':0, '3/2023':5,
            '2/2023':15, '1/2023':10, '12/2022':0,
            '11/2022':0, '10/2022':0, '9/2022':0,
            '8/2022':0, '7/2022':0, '6/2022':0
        }
        total_per_month = DashCallbacksUtilMock.total_amount_in_months(exp_list, 
                                                                       last_twelve_months
                                                                       )
        
        print(total_per_month)
        print(expected_expenses_per_month)
        assert total_per_month == expected_expenses_per_month
    
    def test_invalid_url(self):
        invalid_url = "/dash_entries".split('/')
        assert DashCallbacksUtilMock.invalid_url(invalid_url)

        invalid_url = '/dash_entries/'.split('/')
        assert DashCallbacksUtilMock.invalid_url(invalid_url)
    
    def test_not_invalid_url(self):
        valid_url = '/dash_entries/daniel'.split('/')
        assert not DashCallbacksUtilMock.invalid_url(valid_url)

        