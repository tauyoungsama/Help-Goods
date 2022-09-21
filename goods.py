import cmd, sqlite3

class goodsShell(cmd.Cmd):
	intro = '欢迎使用 Goods 交互式环境。键入 help 或者 ? 查看所有命令。\n'
	prompt = '(goods) '

	def __init__(self):
		super(goodsShell, self).__init__()
		self.conn = sqlite3.connect('goods.db')
		self.cur = self.conn.cursor()
		self.cur.execute('CREATE TABLE IF NOT EXISTS GOODS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL);')

	def do_add(self, arg):
		'添加一个物品。'
		self.cur.execute('INSERT INTO GOODS (NAME) VALUES ("%s")' % arg)
		self.conn.commit()
	def do_del(self, arg):
		'删除一个物品。'
		self.cur.execute('DELETE FROM GOODS WHERE NAME = "%s"' % arg)
		self.conn.commit()
	def do_list(self, arg):
		'列出所有物品。'
		self.cur.execute('SELECT * FROM GOODS')
		for record in self.cur.fetchall(): print(record)
	def do_search(self, arg):
		'查找物品。'
		self.cur.execute('SELECT * FROM GOODS WHERE NAME LIKE "%%%s%%"' % arg)
		for record in self.cur.fetchall(): print(record)
	def do_reset(self, arg):
		'重置数据库。'
		self.cur.execute('DROP TABLE GOODS')
		self.cur.execute('CREATE TABLE GOODS(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);')
		self.conn.commit()
	def do_exit(self, arg):
		'退出交互式环境。'
		self.cur.close()
		self.conn.close()
		return True

if __name__ == '__main__':
	goodsShell().cmdloop()