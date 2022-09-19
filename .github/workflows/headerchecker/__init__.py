from typing import TYPE_CHECKING

from headerchecker import HeaderChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter

def register(linter: 'PyLinter') -> None:
  linter.register_checker(HeaderChecker(linter))