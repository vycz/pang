# coding=UTF-8
import time
import click
from panglib.universe import print_price
from panglib.istore import Istore

istore = Istore()

@click.group(invoke_without_command=True)
@click.argument('alias')
def pang(alias):
    codes = istore.get_signal_data_code(alias)
    while True:
        print_price(codes)
        time.sleep(3)

@pang.command()
@click.option('-alias',help='别名 my_favorite')
@click.option('-code',help='代码 sh600150,sh601989')
def add(alias,code):
    istore.add_data(alias,code)

@pang.command()
@click.option('-alias',help='别名')
def delete(alias):
    istore.del_data(alias)

@pang.command()
def list():
    istore.list_data()

if __name__ == '__main__':
    pang()