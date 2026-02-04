from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import csv  # For saving results

# Setup Chrome with profile (login manually first)
options = Options()
options.add_argument("--user-data-dir=/path/to/your/chrome/profile")  # Update path
driver = webdriver.Chrome(options=options)

# Navigate to Naukri
driver.get("https://www.naukri.com")

# Search for MERN developer jobs
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "qp"))
)
search_box.clear()
search_box.send_keys("MERN developer")  # Customize: "MERN developer Haryana" for location
search_box.submit()

time.sleep(3)

# Scrape job listings
jobs = []
job_elements = driver.find_elements(By.CSS_SELECTOR, ".jobTuple")[:10]  # Top 10 results

for job in job_elements:
    try:
        title_elem = job.find_element(By.CSS_SELECTOR, "a.title")
        title = title_elem.text.strip()
        link = title_elem.get_attribute("href")
        
        company_elem = job.find_element(By.CSS_SELECTOR, "[itemprop='name']")
        company = company_elem.text.strip()
        
        location_elem = job.find_element(By.CSS_SELECTOR, ".jobTuple-header .chevron-right-bold")
        location = location_elem.text.strip()
        
        experience_elem = job.find_element(By.CSS_SELECTOR, ".jobTuple-header .experience")
        experience = experience_elem.text.strip()
        
        posted_elem = job.find_element(By.CSS_SELECTOR, ".jobTuple-header .postedDate")
        posted = posted_elem.text.strip()
        
        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Experience": experience,
            "Posted": posted,
            "Link": link
        })
        print(f"Found: {title} at {company}")
    except Exception as e:
        print(f"Error parsing job: {e}")
        continue

# Save to CSV
with open("mern_jobs_naukri.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Company", "Location", "Experience", "Posted", "Link"])
    writer.writeheader()
    writer.writerows(jobs)

print(f"Saved {len(jobs)} MERN developer jobs to mern_jobs_naukri.csv")

driver.quit()
