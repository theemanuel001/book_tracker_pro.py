import ui

class MainScreen(ui.View):
    def __init__(self):
        self.background_color = 'white'
        self.name = 'Book Tracker Pro'
        self.add_buttons()

    def add_buttons(self):
        add_button = ui.Button(frame=(50, 50, 200, 40))
        add_button.title = 'Add Book'
        add_button.action = self.open_add_book
        self.add_subview(add_button)

        view_button = ui.Button(frame=(50, 120, 200, 40))
        view_button.title = 'View Collection'
        view_button.action = self.open_view_collection
        self.add_subview(view_button)

        stats_button = ui.Button(frame=(50, 190, 200, 40))
        stats_button.title = 'View Statistics'
        stats_button.action = self.open_statistics
        self.add_subview(stats_button)

        exit_button = ui.Button(frame=(50, 260, 200, 40))
        exit_button.title = 'Exit'
        exit_button.action = self.close_app
        self.add_subview(exit_button)

    def open_add_book(self, sender):
        add_screen = AddBookScreen()
        add_screen.present('sheet')

    def open_view_collection(self, sender):
        collection_screen = ViewCollectionScreen()
        collection_screen.present('sheet')

    def open_statistics(self, sender):
        stats_screen = StatisticsScreen()
        stats_screen.present('sheet')

    def close_app(self, sender):
        self.close()

class AddBookScreen(ui.View):
    def __init__(self):
        self.background_color = 'lightgrey'
        self.name = 'Add a New Book'
        self.create_form()

    def create_form(self):
        self.title_field = ui.TextField(frame=(50, 50, 200, 40), placeholder='Book Title')
        self.add_subview(self.title_field)

        self.author_field = ui.TextField(frame=(50, 110, 200, 40), placeholder='Author')
        self.add_subview(self.author_field)

        submit_button = ui.Button(frame=(50, 170, 200, 40))
        submit_button.title = 'Submit'
        submit_button.action = self.submit_book
        self.add_subview(submit_button)

        cancel_button = ui.Button(frame=(50, 230, 200, 40))
        cancel_button.title = 'Cancel'
        cancel_button.action = self.close_screen
        self.add_subview(cancel_button)

    def submit_book(self, sender):
        title = self.title_field.text
        author = self.author_field.text
        if not title or not author:
            ui.alert('Error', 'Both fields are required!', 'OK')
        else:
            # Here, save the book details (can be extended with file/database storage)
            ui.alert('Success', f'Book "{title}" by {author} added!', 'OK')
            self.close()

    def close_screen(self, sender):
        self.close()

class ViewCollectionScreen(ui.View):
    def __init__(self):
        self.background_color = 'white'
        self.name = 'View Collection'
        self.create_collection_view()

    def create_collection_view(self):
        # Placeholder for collection data (can be replaced with actual data storage)
        books = ["Book 1 by Author A", "Book 2 by Author B"]

        list_view = ui.TableView(frame=(0, 0, self.width, self.height), flex='WH')
        data_source = ui.ListDataSource(items=books)
        list_view.data_source = data_source
        list_view.delegate = data_source
        self.add_subview(list_view)

class StatisticsScreen(ui.View):
    def __init__(self):
        self.background_color = 'lightblue'
        self.name = 'View Statistics'
        self.create_stats_view()

    def create_stats_view(self):
        stats_label = ui.Label(frame=(50, 50, 300, 40))
        stats_label.text = 'Total Books: 2 (Placeholder)'
        stats_label.alignment = ui.ALIGN_CENTER
        self.add_subview(stats_label)

# Run the application
main = MainScreen()
main.present('sheet')
 
