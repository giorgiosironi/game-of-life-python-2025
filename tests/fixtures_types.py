from typing import TypeAlias, Callable
from bs4 import BeautifulSoup

LoadPage: TypeAlias = Callable[[str], BeautifulSoup]
