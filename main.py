import csv
import argparse
import db_manager


parser = argparse.ArgumentParser(description='ORM data exporter')
parser.add_argument('-limit', dest='limit', type=int, default=0, help='Execution row limit (number of domains by '
                                                                      'default')

if __name__ == '__main__':

    args = parser.parse_args()

    csv_header = ["domain_ID", "domain_name", "cookies_default", "cookies_dont", "cookies_ninja", "cookies_accepted", "clicked","location","first_parties","cookies_pablo","accepted_pablo"]
    #csv_header = ["domain_ID", "domain_name", "cookies_default", "cookies_dont", "cookies_ninja"]

    #db_orm, db_dont, db_ninja, db_click, db_geo = db_manager.get_dbs()
    db_dont, db_ninja, db_click, db_geo, db_pablo = db_manager.get_dbs()

    domains = db_manager.get_domains(db_geo)

    with open("cookies_report.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)

        for domain in domains:
            print(f"ID: {domain['id']}\t{domain['name']}")

            
            if domain['name'] == 'google.com':
                header = db_manager.get_all_headers(db_geo, domain['name'])
                print(header)

            if domain['name'] == 'amazon.com':
                header = db_manager.get_all_headers(db_geo, domain['name'])
                print(header)
            

            urls_default = db_manager.get_count_urls(db_geo, domain["name"])
            urls_dont = db_manager.get_count_urls(db_dont, domain["name"])
            urls_ninja = db_manager.get_count_urls(db_ninja, domain["name"])
            urls_accepted = db_manager.get_count_urls(db_click, domain["name"])
            urls_pablo = db_manager.get_count_urls(db_pablo, domain["name"])

            if urls_default > 0 and urls_ninja > 0 and urls_accepted > 0:
                cookies_default = db_manager.get_count_cookies(db_geo, domain["name"])
                cookies_dont = db_manager.get_count_cookies(db_dont, domain["name"])
                cookies_ninja = db_manager.get_count_cookies(db_ninja, domain["name"])
                cookies_accepted = db_manager.get_count_cookies(db_click, domain["name"])
                domain_clicked = db_manager.get_clicked(db_click, domain["name"])
                domainLoc = db_manager.get_geoLocationDom(db_geo,domain["name"])
                #print(domainLoc)
                domainLocHead = db_manager.get_geoLocationDomHead(db_geo, domain["name"])
                #print(domainLocHead)
                cookies_pablo = db_manager.get_count_cookies(db_pablo, domain["name"])
                pablo_clicked = db_manager.get_clicked(db_pablo, domain["name"])

                csv_writer.writerow([domain["id"], domain["name"], cookies_default, cookies_dont, cookies_ninja, cookies_accepted, domain_clicked, domainLoc, domainLocHead, cookies_pablo, pablo_clicked])
                #csv_writer.writerow([domain["id"], domain["name"], cookies_default, cookies_dont, cookies_ninja])

            if domain["id"] == args.limit:
                break

    exit(0)
