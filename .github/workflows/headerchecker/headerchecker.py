from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseRawFileChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter

class HeaderChecker(BaseRawFileChecker):
    name = 'header_checker'
    msgs = {
        'C5001': (
            'Header missing',
            'no-header',
            (
                'Output in case of a missing header.'
            ),
        )
    }
    options = ()

    def process_module(self, node: nodes.Module) -> None:
        with node.stream() as stream:
            content = stream.read().decode('utf-8')
            header = '# Copyright'
            search = content.find(header)
            if search == -1:
                self.add_message('no-header', 1)

def register(linter: 'PyLinter') -> None:
  linter.register_checker(HeaderChecker(linter))
