from bs4 import BeautifulSoup
from typing import TypeAlias, Callable

LoadPage: TypeAlias = Callable[[str], BeautifulSoup]
