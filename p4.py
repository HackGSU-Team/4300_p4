from pprint import pprint
def application(env,start_response):
    """main uwsgi application"""
    start_response('200 OK',[('Content-Type','text/html')])
    path = "/home/student/projects/p4/index.html"
    file = open(path)
    data=''
    query = env['QUERY_STRING']
    if(len(env['PATH_INFO']) > 4):
      print(env['PATH_INFO'].split('/')[2])
    if(len(query) > 0):
        creds={
            'user':'food',
            'database':'classicmodels',
            'password':'Foo_Pass1',
            'auth_plugin':'mysql_native_password'
        }
        cnx = mysql.connector.connect(**creds)
        cursor = cns.cursor(dictionary=True)
        queryStr = "SELECT productName, productScale, productVendor, productDescription, quantityInStock,MSRP from products WHERE productLine = {}".format(query);
        cursor.execute(queryStr)
        orders = json.dumps(cursor.fetchall())
        pprint(orders)
    pprint(env)
    print(env['PATH_INFO'])
    html = file.read()
    return html.encode()
 
        
    
