import logging
import math
from django.core.paginator import Paginator

# logger = logging.getLogger(__name__)


class InvalidParameterException(Exception):
    pass


class LimitedPaginator(Paginator):
    # def __init__(self, object_list, per_page, amount=5, *args, **kwargs):
    # super(LimitedPaginator, self).__init__(object_list, per_page, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        amount = kwargs.pop("amount", 5)
        if amount & 1:
            self.amount = amount
        else:
            raise InvalidParameterException("Parameter \"amount\" should be an odd integer")

        super(LimitedPaginator, self).__init__(*args, **kwargs)

    def page(self, number):
        page = super(LimitedPaginator, self).page(number)

        if len(page.object_list) == 0:
            page.main_range = []
            page.has_last = False
            page.has_first = False
            return page

        amount = min(self.amount, len(page.paginator.page_range))
        half = amount / 2

        has_last = False
        has_first = False

        if math.floor(page.number - half) <= 0:
            main_range = range(1, amount + 1)
            if amount < page.paginator.num_pages:
                has_last = True
        elif page.paginator.num_pages <= math.floor(amount / 2) + page.number:
            main_range = range(page.paginator.num_pages - math.ceil(half) - math.floor(half) + 1,
                               page.paginator.num_pages + 1)
            if amount < page.paginator.num_pages:
                has_first = True
        else:
            main_range = range(page.number - math.floor(half), page.number + math.ceil(half))
            has_last = True
            has_first = True

        page.main_range = list(main_range)
        page.has_last = has_last
        page.has_first = has_first
        return page