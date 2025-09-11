from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, DataTable
import lang
import load_config
import colorama
import weather

Lang = load_config.Load_lang()

weatherq = weather.weather_temp_desc()

def create_logo(langt):
    if langt == "EN":
        with open('logo-en', 'r', encoding='utf-8') as file:
            ascll_logo = file.read()
            
    elif langt == "RU":
        with open('logo-ru', 'r', encoding='utf-8') as file:
            ascll_logo = file.read()
    
    return ascll_logo
        

ascll_logo = create_logo(Lang)

class SimpleTileApp(App):
    CSS = """
    #sidebar { 
        width: 30%; 
        border: solid grey; 
    }
    #content { 
        height: 70%; 
        border: solid grey; 
    }
    #footer { 
        height: 30%; 
        border: solid grey; 
    }
    DataTable {
        height: 100%;
        background: black;
    }
    DataTable > .datatable--header {
        background: #333;
        color: white;
    }
    DataTable > .datatable--hover {
        background: #222;
    }
    DataTable > .datatable--cursor {
        background: #444;
    }
    """

    def compose(self) -> ComposeResult:
        
        command = lang.Lang_create(Lang, "command")
        description = lang.Lang_create(Lang, "desc")
        weather_ = lang.Lang_create(Lang, "weather")
        weatherCH = lang.Lang_create(Lang, "weatherCH")
        langO = lang.Lang_create(Lang, "out")
        
        self.content_widget = Static("", classes="header")
        self.footer_widget = Static(ascll_logo, classes="header")
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Static(langO, classes="header")
                table = DataTable()
                table.cursor_type = "row"
                table.show_cursor = True
                table.add_columns(command, description)
                table.add_rows([
                    [weather_, weatherCH],
                    ["f", "f"]
                ])
                yield table
            with Vertical():
                with Vertical(id="content"):
                    yield self.content_widget
                with Vertical(id="footer"):
                    yield self.footer_widget

    def update_content(self, weather_temp):
        content = self.query_one("#content")
        content.remove_children()
        from weather_ascll import OutAscll
        content.mount(Static(weather_temp, classes="header"))
        content.mount(OutAscll())

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        row = event.data_table.get_row(event.row_key)
        if row and row[0] == lang.Lang_create(Lang, "weather"):
            weather_temp = weatherq["temp"]
            self.update_content(weather_temp)
        self.notify(f"Выбрана команда: {row[0]} - {row[1]}")

if __name__ == "__main__":
    app = SimpleTileApp()
    app.run()
