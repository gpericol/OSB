import requests
from datetime import datetime, timedelta

import config

class NistClient:
    @staticmethod
    def get_nist_cves():
        today = datetime.now()
        mod_start_date = (today - timedelta(weeks=1)).strftime("%Y-%m-%dT00:00:00.000")
        mod_end_date = today.strftime("%Y-%m-%dT00:00:00.000")
        url = config.NIST_API.format(mod_start_date, mod_end_date)

        response = requests.get(url)
        data = response.json()
        return data

    @staticmethod
    def load_popular_services():
        with open(config.SERVICES_PATH, 'r') as file:
            services = [line.strip().lower() for line in file]
        return services
