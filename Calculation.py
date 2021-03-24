def compute_bruto_yield(total_investment, rental_fee, exclude_month=True):
    """
    :param exclude_month: take into account 1 month rental fee for maintain expense
    :param total_investment: includes: taxes, reconstruction, mortgage advisors fee, broker fee , etc..
    :param rental_fee: monthly rental expected payment
    :return:
    """
    yearly_rental = rental_fee * 11 if exclude_month else rental_fee * 12
    yearly_yield = (yearly_rental / total_investment) * 100
    return yearly_yield


def compute_net_yield(total_investment, my_investment, mortgage_interest_rate, rental_fee, exclude_month=True):
    """
    :param total_investment:
    :param my_investment:
    :param mortgage_interest_rate:
    :param rental_fee:
    :param exclude_month:
    :return:
    """
    mortgage = total_investment - my_investment
    yearly_mortgage_payments = mortgage_interest_rate * mortgage
    yearly_rental = rental_fee * 11 if exclude_month else rental_fee * 12
    yearly_income_net = yearly_rental - yearly_mortgage_payments
    yearly_yield_net = (yearly_income_net / my_investment) * 100
    return yearly_yield_net


def compute_n_years_profit(n, net_yield, my_investment, discount_factor):
    total_discounted_profit = 0
    yearly_profit = my_investment * (net_yield / 100)
    for i in range(0, n):
        total_discounted_profit += yearly_profit * (discount_factor ** i)

    return total_discounted_profit


if __name__ == '__main__':
    yearly_net_yield = compute_net_yield(800000, 200000, 0.03, 2500, exclude_month=True)
    print(compute_n_years_profit(5, yearly_net_yield, 200000, 0.98))
