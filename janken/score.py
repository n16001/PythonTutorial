# 'score.txt' のデータを読み取り、現状の戦績を表示するだけ。
import jsonprint(x)
x = {}
with open("score.txt", "r") as f:
    x = json.load(f)

