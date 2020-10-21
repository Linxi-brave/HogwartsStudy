#coding=utf-8
import xlrd
from xlutils.copy import copy

#xlwd
class OperaExcel:
	def __init__(self,file_path=None,i=None):
		if file_path == None:
			self.file_path = '../config/case.xls'
		else:
			self.file_path = file_path	
		if i == None:
			i=1
		self.excel = self.get_excel()
		self.data = self.get_sheets(i)
			
	def get_excel(self):
		'''
		获取excel
		'''
		excel = xlrd.open_workbook(self.file_path)
		return excel

	def get_sheets(self,i):
		'''
		获取sheets的内容
		'''
		tables = self.excel.sheets()[i]
		return tables

	def get_lines(self):
		'''
		获取excel行数
		'''
		lines = self.data.nrows
		return lines

	def get_cell(self,row,cell):
		'''
		获取单元格内容
		'''
		data = self.data.cell(row,cell).value
		return data

	def write_value(self,row,cols,value,i = 2):
		'''
		写入表格数据，写入数据默认为第8 列
		:param row: 行数
		:param value: 写入的参数
		:return: 返回执行了写表格操作
		'''

		read_value = self.excel
		write_data = copy(read_value)
		write_save = write_data.get_sheet(i)
		write_save.write(row,cols,value)
		write_data.save(self.file_path)

	def write_value_my(self,row,colos,value,i):
		'''
		写入数据，row代表行数，colos代表列数，i代表第几个表格
		:return: 写入表格数据
		'''
		# file_path = "../config/case.xls"

		excel = xlrd.open_workbook(self.file_path)
		read_value = excel
		write_data = copy(read_value)
		write_save = write_data.get_sheet(i)
		write_save.write(row,colos,value)
		write_data.save(self.file_path)



if __name__ == '__main__':
	opera = OperaExcel()
	# print (opera.get_lines())

	print(opera.write_value_my(2,10,"12234444",0))



