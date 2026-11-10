"""Mobile website checks: what a manual tester does on a phone, automated.
Run:  .\run_mobile.ps1 -Url "https://your-site.com" -Test test_mobile_website.py
"""
import time
import config


def _open(d):
    d.get(config.TEST_URL)
    time.sleep(2)


def test_page_loads_with_title(web_driver):
    _open(web_driver)
    assert web_driver.title.strip(), "page has no <title>"


def test_no_horizontal_scroll(web_driver):
    """Responsive check: page must fit phone width."""
    _open(web_driver)
    page_w = web_driver.execute_script("return document.documentElement.scrollWidth")
    view_w = web_driver.execute_script("return window.innerWidth")
    assert page_w <= view_w + 1, f"page {page_w}px wider than screen {view_w}px"


def test_has_viewport_meta(web_driver):
    _open(web_driver)
    vp = web_driver.execute_script(
        "var m=document.querySelector('meta[name=viewport]');return m?m.content:''")
    assert "width=device-width" in vp, "missing <meta name=viewport content=width=device-width>"


def test_links_are_tappable(web_driver):
    """Links should be at least 24x24 px for a finger."""
    _open(web_driver)
    small = web_driver.execute_script("""
        return [...document.querySelectorAll('a')].filter(a=>{
          const r=a.getBoundingClientRect();
          return r.width>0 && (r.width<24 || r.height<24);
        }).map(a=>a.innerText.trim()||a.href).slice(0,10);""")
    assert not small, f"links too small to tap: {small}"


def test_scroll_to_bottom(web_driver):
    _open(web_driver)
    web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    y = web_driver.execute_script("return window.scrollY")
    h = web_driver.execute_script("return document.body.scrollHeight - window.innerHeight")
    assert y >= h - 5 or h <= 0


def test_landscape_rotation(web_driver):
    _open(web_driver)
    web_driver.orientation = "LANDSCAPE"
    time.sleep(2)
    try:
        page_w = web_driver.execute_script("return document.documentElement.scrollWidth")
        view_w = web_driver.execute_script("return window.innerWidth")
        assert page_w <= view_w + 1, "layout breaks in landscape"
    finally:
        web_driver.orientation = "PORTRAIT"


def test_page_load_time(web_driver):
    _open(web_driver)
    ms = web_driver.execute_script(
        "const t=performance.timing;return t.loadEventEnd-t.navigationStart")
    assert ms < 10000, f"page took {ms} ms to load"
