import pymysql

# Important change to use pymysql to avoid installing system-level dependencies for mysqlclient
pymysql.install_as_MySQLdb()
