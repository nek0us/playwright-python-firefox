# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from pathlib import Path

from playwright_firefox.sync_api import Playwright, sync_playwright


def main(playwright: Playwright, browser_name: str) -> None:
    browser = playwright[browser_name].launch()
    page = browser.new_page()
    page.goto("data:text/html,Foobar")
    here = Path(__file__).parent.resolve()
    page.screenshot(path=here / f"{browser_name}.png")
    page.close()
    browser.close()


if __name__ == "__main__":
    browser_name = sys.argv[1]
    with sync_playwright() as p:
        main(p, browser_name)
