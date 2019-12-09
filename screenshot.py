# -*- coding: utf-8 -*- 
"""
__author__ = "Road36"
__date__ = "19-12-9"
Describe:
"""

import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'--no-sandbox': '--disable-setuid-sandbox'})
    # const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
    page = await browser.newPage()
    await page.goto('http://baidu.com')
    await page.screenshot({'path': 'baidu.png'})
    await browser.close()

asyncio.run(main())
