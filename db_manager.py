import MySQLdb
import ast


def get_dbs():

    #db_orm = MySQLdb.connect(host="127.0.0.1", port=3306, user="toor", passwd="pinacolada", db="ORM")
    db_dont = MySQLdb.connect(host="127.0.0.1", port=3306, user="toor", passwd="pinacolada", db="ORMdontCare")
    db_ninja = MySQLdb.connect(host="127.0.0.1", port=3306, user="toor", passwd="pinacolada", db="ORMninja")
    db_click = MySQLdb.connect(host="127.0.0.1", port=3306, user="toor", passwd="pinacolada", db="ORMclick")
    db_geo = MySQLdb.connect(host="127.0.0.1", port=3306, user="toor", passwd="pinacolada", db="ORMgeo")
    db_pablo = MySQLdb.connect(host="127.0.0.1", port=3306, user="toor", passwd="pinacolada", db="ORMpablo")

    return db_dont, db_ninja, db_click, db_geo, db_pablo


def get_headers_cookies(db, domain):

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT DISTINCT domain.name, url.id, url.headers, url.url " \
            f"FROM domain, url, domain_url " \
            f"WHERE domain.id = domain_url.domain_id " \
            f"AND domain_url.url_id = url.id " \
            f"AND domain.name = '{domain}' " \
            f"AND url.headers LIKE '%\\'set-cookie\\':%'"

    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results

def get_all_headers(db, domain):

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT DISTINCT domain.name, url.id, url.headers, url.url " \
            f"FROM domain, url, domain_url " \
            f"WHERE domain.id = domain_url.domain_id " \
            f"AND domain_url.url_id = url.id " \
            f"AND domain.name = '{domain}'"

    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results


def get_count_urls(db, domain):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT COUNT(DISTINCT url.id) as total_urls " \
            f"FROM domain, url, domain_url " \
            f"WHERE domain.id = domain_url.domain_id " \
            f"AND domain_url.url_id = url.id " \
            f"AND domain.name = '{domain}'"

    cursor.execute(query)
    results = cursor.fetchall()
    total_cookies = int(results[0]["total_urls"])
    cursor.close()

    return total_cookies


def get_count_cookies(db, domain):

    total_cookies = 0

    try:
        requests = get_all_headers(db, domain)
    except UnicodeDecodeError:
        print("MySQLdb doing strange things with unicode")
    else:
        for request in requests:
            if request["headers"] is not None and ((request["headers"].find("set-cookie") != -1) or (request["headers"].find("Set-Cookie") != -1)):
                total_cookies += len(request["headers"].split("set-cookie"))-1
                total_cookies += len(request["headers"].split("Set-Cookie"))-1

                #if request["headers"].find("domain") != -1:
                    #print(request["headers"])

            '''
            try:
                if "set-cookie" not in request["headers"] and "Set-Cookie" not in request["headers"]:
                    continue
                header_dict = ast.literal_eval(request["headers"])
                if 'set-cookie' in header_dict:
                    cookies_list = str.split(header_dict["set-cookie"], "\n")
                    total_cookies += len(cookies_list) - 1
                elif 'Set-Cookie' in header_dict:
                    cookies_list = str.split(header_dict["Set-Cookie"], "\n")
                    total_cookies += len(cookies_list) - 1
            except:
                print("Unhandled Error")
                '''

    return total_cookies


def get_clicked(db, domain):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT clicked " \
            f"FROM domain " \
            f"WHERE name='{domain}'"

    cursor.execute(query)
    results = cursor.fetchall()
    clicked_bool = bool(results[0]["clicked"])
    cursor.close()

    return clicked_bool


def get_total_clicked(db):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT SUM(clicked) AS clicks " \
            f"FROM ORM.domain"

    cursor.execute(query)
    results = cursor.fetchall()
    total_clicks = int(results[0]["clicks"])
    cursor.close()

    return total_clicks


def get_domains(db):

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT domain.id, domain.name " \
            f"FROM domain"
    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results


def get_geoLocationDom(db,domain):
    
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT DISTINCT location.country_code, url.headers " \
            f"FROM url JOIN location " \
            f"ON url.id = location.id " \
            f"WHERE url.url LIKE '%{domain}%'"

    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            #print(key)
            #print(row["country_code"])
            result = row["country_code"]
            #result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results


def get_geoLocation(db,domain):

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT DISTINCT location.country_code " \
            f"FROM location, domain, url, domain_url " \
            f"WHERE domain.id = domain_url.domain_id " \
            f"AND domain_url.url_id = url.id " \
            f"AND url.id = location.id " \
            f"AND domain.name = '{domain}'"

    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results


def get_geoLocationDomHead(db,domain):
    
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    query = f"SELECT DISTINCT location.country_code, url.headers " \
            f"FROM url JOIN location " \
            f"ON url.id = location.id " \
            f"WHERE url.url LIKE '%{domain}%'"

    cursor.execute(query)

    results = []
    for row in cursor.fetchall():
        result = {}
        for key in row.keys():
            #print(key)
            #print(row["country_code"])
            #result = row["country_code"]
            if row["headers"].find(domain) != -1:
                result = True #It is first party domain
            else:
                result = False #It is third party domain
            #result[key] = row[key]
            if row[key] == "NULL":
                result[key] = None
        results.append(result)

    cursor.close()

    return results