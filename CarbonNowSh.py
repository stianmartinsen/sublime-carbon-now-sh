import sublime, sublime_plugin
import webbrowser
import urllib.parse

class CarbonNowShCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get all text
        reg = sublime.Region(0, self.view.size())
        text = self.view.substr(reg)

        # Get selected text
        selectedText = ''

        for selectedRegion in self.view.sel():
            if not selectedRegion.empty():
                selectedLines = self.view.lines(selectedRegion)
                for line in selectedLines:
                    selectedText += self.view.substr(line) + "\n"

        # Send only selected text if any
        if selectedText:
            text = selectedText

        # Build URL
        url = "https://carbon.now.sh/?code="
        url += urllib.parse.quote_plus(text)

        # Open browser
        webbrowser.open_new_tab(url)
