import sublime
import sublime_plugin
import re


class PostmanParametersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        lines = self.view.lines(self.view.sel()[0])
        offset = 0

        for original_region in lines:
            line_region = sublime.Region(
                a=original_region.a + offset,
                b=original_region.b + offset,
            )

            content = self.view.substr(line_region)

            if re.match(r'(.*):(.*)', content):
                processed = re.sub(r'(.*):(.*)',
                                   r"            '\1': '\2',",
                                   content)

                offset += len(processed) - len(content)

                self.view.replace(edit, line_region, processed)


class MakeYieldItemCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        lines = self.view.lines(self.view.sel()[0])
        offset = 0
        add_ending = False

        for original_region in lines:
            line_region = sublime.Region(
                a=original_region.a + offset,
                b=original_region.b + offset,
            )

            content = self.view.substr(line_region)
            striped_content = content.replace(' ', '')

            if re.match(r'class\w*\(scrapy\.Item\):', striped_content):
                processed = re.sub(r'class(\w*)\(scrapy\.Item\):',
                                   r"\nyield \1(",
                                   striped_content)
                if add_ending:
                    processed = ')\n' + processed
                add_ending = True

            elif re.match(r'\w*=scrapy\.Field()', striped_content):
                processed = re.sub(r'(\w*)=scrapy\.Field\(\)',
                                   r"    \1=",
                                   striped_content)
            else:
                # if the line is a blank line, or a comment,
                # we should delete it
                line_region.b += 1
                self.view.erase(edit, line_region)
                offset -= len(content) + 1
                continue

            offset += len(processed) - len(content)

            self.view.replace(edit, line_region, processed)

        if add_ending:
            self.view.insert(edit, lines[-1].b+offset+1, ')\n')
