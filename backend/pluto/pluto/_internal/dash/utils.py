from datetime import datetime
from typing import Dict, List, Union

import pandas as pd  # type: ignore

from pluto._internal.domain.model.expense import Expense
from pluto._internal.domain.model.income import Income


class DashCallbacksUtil:
    month_year_fmt = "{month}/{year}"

    @classmethod
    def get_last_twelve_months_str_list(cls, month_year_fmt) -> list[str]:
        today_date = cls.get_current_date()

        curr_month = today_date.month
        curr_year = today_date.year

        months_and_years = list()
        months_and_years.append(month_year_fmt.format(month=curr_month, year=curr_year))
        months_added = 1
        while months_added < 12:
            curr_month -= 1
            if curr_month < 1:
                curr_month = 12
                curr_year -= 1
            months_and_years.append(f"{curr_month}/{curr_year}")
            months_added += 1

        months_and_years.reverse()

        return months_and_years

    # useful for testing
    @classmethod
    def get_current_date(cls):
        today_date = datetime.today()
        return today_date

    @classmethod
    def total_amount_in_months(
        cls, obj_list: Union[List[Expense], List[Income]], last_twelve_months: List[str]
    ) -> Dict[str, float]:
        total_amount_last_year: Dict[str, float] = dict()
        total_amount_last_year = {month: 0 for month in last_twelve_months}
        for obj in obj_list:
            obj_date: Union[datetime, str] = (
                obj.exp_date if isinstance(obj, Expense) else obj.inc_date
            )
            if isinstance(obj_date, str):
                obj_date = datetime.strptime(obj_date, "%Y-%m-%d")

            curr_month = obj_date.month
            curr_year = obj_date.year
            formated_month_year = DashCallbacksUtil.month_year_fmt.format(
                month=curr_month, year=curr_year
            )

            if formated_month_year in last_twelve_months:
                total_amount_last_year[formated_month_year] += obj.amount

        return total_amount_last_year

    @classmethod
    def get_total_by_month_df(
        cls, last_twelve_months, total_expenses_by_month_dict
    ) -> pd.DataFrame:
        df = pd.DataFrame()
        df["Data"] = last_twelve_months
        df["Total"] = cls._total_ordered_my_months(
            total_expenses_by_month_dict, last_twelve_months
        )
        return df

    @classmethod
    def get_total_inc_and_exp_by_month_df(
        cls,
        last_twelve_months: list[str],
        total_exp_by_month_dict: dict,
        total_inc_by_month_dict: dict,
    ) -> pd.DataFrame:
        df = pd.DataFrame()
        df["Data"] = last_twelve_months * 2
        expenses_by_month = cls._total_ordered_my_months(
            total_exp_by_month_dict, last_twelve_months
        )
        incomes_by_month = cls._total_ordered_my_months(
            total_inc_by_month_dict, last_twelve_months
        )
        expenses_by_month.extend(incomes_by_month)
        df["Total"] = expenses_by_month
        df["Tipo"] = ["Gastos"] * 12 + ["Receitas"] * 12
        return df

    @staticmethod
    def _total_ordered_my_months(total_by_month: dict, months: list[str]):
        return [total_by_month.get(date, 0) for date in months]

    @staticmethod
    def invalid_url(url_by_bar):
        return len(url_by_bar) < 3 or url_by_bar[2] == ""
