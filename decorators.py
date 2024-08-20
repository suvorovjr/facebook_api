from functools import wraps


def paginator(max_page=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_items = []
            page_count = 0
            while max_page is None or max_page < page_count:
                items = func(*args, **kwargs)
                all_items.extend(items.data)
                page_count += 1
                if items.paging.next is None:
                    break
                next_url = items.paging.get('next')
                kwargs['url'] = next_url

            return all_items

        return wrapper

    return decorator
