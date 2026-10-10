import sys, pathlib
from playwright.sync_api import sync_playwright
d = pathlib.Path(sys.argv[1]).resolve()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto((d / 'carrousel.html').as_uri())
    pg.wait_for_timeout(500)
    for i in range(1, 9):
        pg.locator(f'#c{i}').screenshot(path=str(d / f'carte-{i}.png'))
    b.close()
