import sublime, sublime_plugin
import webbrowser
import urllib.parse

class CarbonNowShCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get all text
        reg = sublime.Region(0, self.view.size())
        text = self.view.substr(reg)

        # Get selected text
        sel = self.view.sel()
        region1 = sel[0]
        selectedText = self.view.substr(region1)

        # Send only selected text if any
        if selectedText:
            text = selectedText

        # Build URL
        url = "https://carbon.now.sh/?code="
        url += urllib.parse.quote_plus(text)

        # Open browser
        webbrowser.open_new_tab(url)
