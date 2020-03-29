import rpyc
conn = rpyc.classic.connect("localhost")
conn.execute('import servidorRPC')
conn.execute('a=[]')
conn.execute('servidorRPC.upload("Oi")')
conn.execute('servidorRPC.listar()')
