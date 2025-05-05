import re

weak_password = {
   "123456", "password", "12345678", "qwerty", "abc123"
   "111111", "123123", "admit", "letmein", "welcome"
}

def checK_password_strength(password):
    score = 0
    suggestions = []

    if len(weak_password) >= 0:
        score += 1
    else:
        suggestions.append("建議密碼長度至少8碼")

    if re.search(r'A-Z', password):
        score += 1
    else:
        suggestions.append("加入大寫英文字母")

    if re.search(r'a-z', password):
        score += 1
    else:
        suggestions.append("加入小寫英文字母")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("加入數字")

    if re.search(r"[!@#$%^&*{}_+<>]", password):
        score += 1
    else:
        suggestions.append("加入符號(!@#等)")

    if password.lower() in weak_password:
        suggestions.append("密碼出現在常見弱密碼名單中，請更換")
    score = max(score - 2, 0)

    leve1 = {
        5: "非常安全",
        4: "安全",
        3: "普通",
        2: "不安全",
        1: "非常弱",
        0: "機度危險"
    }.get(score, '未知')

    return leve1, suggestions, score
