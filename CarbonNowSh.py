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

        settings = sublime.load_settings("Carbon.sublime-settings")

        # Build config
        config = {
            't': settings.get('theme'),
            'code': text
        }

        # Build URL
        url = "https://carbon.now.sh/?" + urllib.parse.urlencode(config)

        # Open browser
        webbrowser.open_new_tab(url)
