import sublime
import sublime_plugin
import re


class RegexEscapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            substr = self.view.substr(sel)
            self.view.replace(edit, sel, re.escape(substr))
