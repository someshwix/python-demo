
class Paginator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.num_pages = (len(items) + page_size - 1) // page_size  # Calculate total number of pages
        self.current_page = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page >= self.num_pages:
            raise StopIteration
        else:
            start_index = self.current_page * self.page_size
            end_index = min((self.current_page + 1) * self.page_size, len(self.items))
            page_items = self.items[start_index:end_index]
            self.current_page += 1
            return page_items

# Example usage
items = list(range(1, 21))  # Example list of items
page_size = 5  # Number of items per page

paginator = Paginator(items, page_size)

for page in paginator:
    print(page)