import plotly.express as px  # type: ignore
from dash.dependencies import Input, Output  # type: ignore

from pluto._internal.adapters.expense_service import ExpenseServiceImpl
from pluto._internal.adapters.income_service import IncomeServiceImpl
from pluto._internal.dash.utils import DashCallbacksUtil
from pluto._internal.server.server import Server


def register_callbacks(dashapp):
    @dashapp.callback(
        Output("graph", "figure"),
        Input(component_id="url", component_property="pathname"),
    )
    def update_exp_and_inc_bar_graph(url_path: str):
        url_by_bar = url_path.split("/")

        if DashCallbacksUtil.invalid_url(url_by_bar):
            return ""

        user_id = url_by_bar[2]

        exp_service = ExpenseServiceImpl(Server.DB_IMP)
        expenses = exp_service.expenses_from_user_id(user_id)

        inc_service = IncomeServiceImpl(Server.DB_IMP)
        incomes = inc_service.incomes_from_user_id(user_id)

        last_twelve_months = DashCallbacksUtil.get_last_twelve_months_str_list(
            DashCallbacksUtil.month_year_fmt
        )

        total_expenses_by_month_dict = DashCallbacksUtil.total_amount_in_months(
            expenses, last_twelve_months
        )

        total_incomes_by_month_dict = DashCallbacksUtil.total_amount_in_months(
            incomes, last_twelve_months
        )

        df = DashCallbacksUtil.get_total_inc_and_exp_by_month_df(
            last_twelve_months,
            total_expenses_by_month_dict,
            total_incomes_by_month_dict,
        )
        title = "Gastos e Receitas nos últimos doze meses"
        return px.bar(
            df, x="Data", y="Total", color="Tipo", title=title, barmode="group"
        )
