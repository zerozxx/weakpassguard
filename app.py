from flask import Flask, request, render_template_string
from core import checK_password_strength

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<title>WeakPassGuard</title>
<h1>🔐密碼強度檢查器</h1>
<form method="post">
    <input type="text" name="password" placeholder="請書入密碼">
    <input type="submit" value="檢查">
</form>
{% if leve1 %}
 <h2>結果</h2>
 <p><strong>安全等級:</strong>{{ leve1 }} ({{ score }}/5分)</p>
 {% if suggestions %}
 <p><strong>改善建議</strong></p>
 <ul>
    {% for s in suggestions %}
    <li>{{ s }}</li>
    {% endfor %}
 </ul>
 {% else %}
 <p>🎉密碼非常強</p>
 {% endif %}
{% endif %}
'''
@app.route('/',methods=['GET','POST'])
def index():
    leve1 = score = suggestions = None
    if request.method == 'POST':
        pw = request.form['password']
        leve1, suggestions, score = checK_password_strength(pw)
    return render_template_string(HTML_TEMPLATE, leve1=leve1, suggestions=suggestions, score=score)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
