import pandas as pd
import scrapy

class CVESpider(scrapy.Spider):
    name = "cve_spider"
    start_urls = [
        "https://www.thehackernews.com/",
        "https://www.dfirreport.com/",
        "https://www.clamav.com/",
        "https://www.securitynews.com/",
    ]

    def parse(self, response):
        cve_scores = []
        for article in response.css("article"):
            cve_score = article.css(".cve-score::text").get()
            if cve_score and float(cve_score) >= 7.8:
                cve_scores.append(cve_score)

        df = pd.DataFrame(cve_scores, columns=["CVE Score"])
        df["Vendor"] = article.css(".cve-vendor::text").get()
        df["Short Description"] = article.css(".cve-description::text").get()
        df["Link"] = article.css(".cve-link::attr(href)").get()

        # Remove duplicate CVEs
        df = df.drop_duplicates(subset=["CVE Score", "Vendor"])

        # Upload the Excel spreadsheet to the SharePoint server
        with pd.ExcelWriter("cve_scores.xlsx") as writer:
            df.to_excel(writer)
            writer.save()