#cording:utf-8
import subprocess
import sys
args = sys.argv

#ホストネーム：サーバーのホスト名
host_name = args[1]
#is_local:ローカル接続であるかの有無のチェック
is_local = args[2]

if is_local == "l":
	ip = "-----" # ローカルip
elif is_local == "g":
	ip = "-----" # グローバルip
else:
	while(is_local != "l" and is_local != "g"):
		is_local = input("ローカル接続なら「l」グローバル接続なら「g」を入力してください:")
	if is_local == "l":
		ip = "-----" # ローカルip
	else:
		ip = "-----" # グローバルip
#print(ip)
command = 'ssh '+ host_name +'@'+ ip
#print(command)

subprocess.call(command.split())
