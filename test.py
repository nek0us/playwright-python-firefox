from playwright_firefox.async_api import async_playwright
from playwright_firefox.stealth import Stealth
import asyncio

async def main():
    playwright_manager = async_playwright()
    playwright = await playwright_manager.start()
    browser = await playwright.firefox.launch(
        headless=True,
        slow_mo=50,
    )
    context = await browser.new_context()
    await Stealth().apply_stealth_async(context)
    page = await context.new_page()

    await page.goto("https://playwright.dev")
    await page.screenshot(path="1.png")
    # pass

asyncio.run(main())