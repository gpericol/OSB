import re
import nist_client

class CVEFormatter:

    @staticmethod
    def format_cve_html(cve):
        cve_id = cve['cve']['id']
        cve_published = cve['cve']['published'].split("T")[0]
        vuln_status = cve['cve']['vulnStatus']

        if vuln_status != 'Analyzed':
            return '', False

        description = cve['cve']['descriptions'][0].get('value', 'N/A')
        metrics = cve['cve']['metrics']
        regex_v3 = re.compile(r"cvssMetricV3[01]")
        regex_v2 = re.compile(r"cvssMetricV2")

        base_score = next((metrics[key][0]['cvssData'].get('baseScore', 'N/A') for key in metrics if regex_v3.match(key)), None) \
                    or next((metrics[key][0]['score'].get('base', 'N/A') for key in metrics if regex_v2.match(key)), None)

        base_severity = next((metrics[key][0]['cvssData'].get('baseSeverity', 'N/A') for key in metrics if regex_v3.match(key)), None)

        severity_color = ''
        if base_severity == 'HIGH':
            severity_color = 'red'
        elif base_severity == 'CRITICAL':
            severity_color = 'purple'

        popular_services = nist_client.NistClient.load_popular_services()
        popular_flag = 'popular' if any(service in description for service in popular_services) else ''
        popular_alert = '*POPULAR!*' if popular_flag else ''

        html = f"<div class='cve_card {popular_flag}'>"
        html += f"<br><a class='cve_id' href='https://nvd.nist.gov/vuln/detail/{cve_id}'>{cve_id}</a><span>&emsp;{popular_alert}</span>"
        html += f"<p><b>Description:</b> {description}</p>"
        html += f"<p><span><b>Score:</b> {base_score or 'N/A'}</span> <span><b>Severity:</b> <span style='color: {severity_color};'>{base_severity or 'N/A'}</span></span> <span><b>Published:</b> {cve_published}</span></p>"
        html += f"</div>"
        html += "<hr>"

        return html, popular_flag == 'popular'

    @staticmethod
    def get_cve_html(cves):
        popular_html = "<hr>"
        normal_html = "<hr>"
        for cve in cves:
            cve_html, is_popular = CVEFormatter.format_cve_html(cve)
            if is_popular:
                popular_html += cve_html
            else:
                normal_html += cve_html
        return popular_html + normal_html