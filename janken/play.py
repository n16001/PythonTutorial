HANDS = ('グー', 'チョキ', 'パー')


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """
    import ramdom

    ramdom.choice(HANDS)

    return


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0,負けは-1を返す
    """
    if player == computer:
        if player == 1 or player == 2 or player == 3:

            return 0

        else:
            if player == 1:
                if computer == 2:
                    return 1
                if computer == 3:
                    return -1
            if player == 2:
                if computer == 1:
                    return -1
                if computer == 3
                    return 1
            if player == 3:
                if computer == 1:
                    return 1
                if computer == 2:
                    return -1


def save_score(result):
    """
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    """








if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示

    print(computer)

    print(result)

    save_score(result)