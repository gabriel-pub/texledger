from __future__ import annotations
from textual.app import App, ComposeResult, InvalidThemeError
from textual.widgets import Footer, Header
from texledger.config import config as cf


class LedgerApp(App):
    BINDINGS = []

    def on_mount(self) -> None:
        try:
            # WARN: `cf.get` has not been implemented
            self.theme = cf.get("theme")
        except InvalidThemeError:
            self.theme = "textual-dark"  # fallback to a sane default

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


def main():
    app = LedgerApp()
    app.run()


if __name__ == "__main__":
    main()
