import re, time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

BASE = "https://www.mgm.gov.tr/veridegerlendirme/il-ve-ilceler-istatistik.aspx"

S = requests.Session()
S.headers.update({
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.7,en;q=0.6",
    "Referer": "https://www.mgm.gov.tr/",
})

NUM_RE = re.compile(r"[-+]?\d+(?:[.,]\d+)?")

def to_float(x):
    """Convert a string number that may use comma decimal into float."""
    return float(str(x).strip().replace(",", "."))

def extract_12_from_row(tr):
    """Extract 12 numeric values from a single <tr> row (months)."""
    cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
    nums = []
    for c in cells:
        found = NUM_RE.findall(c)
        for f in found:
            try:
                nums.append(to_float(f))
            except:
                pass
    return nums[:12] if len(nums) >= 12 else None

def find_row_12vals(soup, label_keywords):
    """
    Find the table row that contains all label_keywords and return its 12 monthly values.
    label_keywords example:
      ["Ortalama Sıcaklık"]
      ["Aylık Toplam Yağış Miktarı", "Ortalaması"]
    """
    for tr in soup.find_all("tr"):
        row_text = tr.get_text(" ", strip=True)
        if all(k in row_text for k in label_keywords):
            vals = extract_12_from_row(tr)
            if vals is not None:
                return vals
    return None

def get_cities_from_ankara_page():
    """
    Collect province links by scanning the ANKARA page for anchors that contain 'm='.
    Returns: [(m_param, display_name), ...]
    """
    r = S.get(BASE, params={"k": "H", "m": "ANKARA"}, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    cities = []
    seen = set()

    # Scan all links; extract m= parameter
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "m=" not in href:
            continue
        full = urljoin("https://www.mgm.gov.tr", href)
        q = parse_qs(urlparse(full).query)
        m = q.get("m", [None])[0]
        if not m:
            continue

        # Visible province name
        disp = a.get_text(strip=True)

        # Basic filter to avoid unrelated links
        if not disp or len(disp) > 25:
            continue

        key = (m, disp)
        if key not in seen:
            seen.add(key)
            cities.append(key)

    # Fallback: if nothing found, regex-scan the HTML for k=H&m= links
    if len(cities) == 0:
        html = r.text
        ms = re.findall(
            r"il-ve-ilceler-istatistik\.aspx\?k=H(?:&amp;|&)m=([A-Za-zÇĞİÖŞÜçğıöşü0-9]+)",
            html
        )
        ms = list(dict.fromkeys(ms))  # unique preserving order
        cities = [(m, m) for m in ms]

    return cities

def scrape_city(m_param, disp_name=None):
    """
    Scrape one province page:
    - 12 monthly average temperatures
    - 12 monthly total precipitation averages
    plus computed annual metrics.
    """
    r = S.get(BASE, params={"k": "H", "m": m_param}, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}")

    soup = BeautifulSoup(r.text, "lxml")

    temp12 = find_row_12vals(soup, ["Ortalama Sıcaklık"])
    prec12 = find_row_12vals(soup, ["Aylık Toplam Yağış Miktarı", "Ortalaması"])

    if temp12 is None or prec12 is None:
        raise ValueError("Could not find the 12-month temperature/precipitation rows in the table.")

    row = {
        "province": disp_name if disp_name else m_param,
        "m_param": m_param,
        "temp_annual_mean": sum(temp12) / 12.0,
        "prec_annual_total": sum(prec12),
    }

    for i, v in enumerate(temp12, start=1):
        row[f"temp_m{i:02d}"] = v

    for i, v in enumerate(prec12, start=1):
        row[f"prec_m{i:02d}"] = v

    return row

# =========================
# RUN FOR ALL PROVINCES
# =========================
cities = get_cities_from_ankara_page()
print("Number of province links found:", len(cities))
print("First 20:", cities[:20])

if len(cities) == 0:
    raise RuntimeError("Could not find the province list. The page structure may have changed.")

rows = []
failed = []

for idx, (m_param, disp) in enumerate(cities, start=1):
    try:
        rows.append(scrape_city(m_param, disp))
    except Exception as e:
        failed.append({"m_param": m_param, "display": disp, "error": str(e)})

    time.sleep(0.6)  # be polite with rate-limiting

print("Success:", len(rows), "| Failed:", len(failed))

if rows:
    out = pd.DataFrame(rows).sort_values("province").reset_index(drop=True)
    out.to_csv("iklim_mgm_1991_2020.csv", index=False, encoding="utf-8-sig")
    
    print("Saved: iklim_mgm_1991_2020.csv")
    # --- Preview the generated CSV in the notebook ---
   # print("\n=== Preview: iklim_mgm_1991_2020.csv ===")
    #print("Shape:", out.shape)
    #display(out.head(10))          # first 10 rows

   # print("\nColumns:", list(out.columns))
    #display(out.tail(5))           # last 5 rows (optional)

    # Quick sanity checks
    #print("\nMissing values (top):")
    #display(out.isna().sum().sort_values(ascending=False).head(10))

    #print("\nBasic stats:")
    #display(out[["temp_annual_mean", "prec_annual_total"]].describe())


if failed:
    pd.DataFrame(failed).to_csv("iklim_failed.csv", index=False, encoding="utf-8-sig")
    #print("Saved: iklim_failed.csv")
    #display(pd.DataFrame(failed).head(15))

