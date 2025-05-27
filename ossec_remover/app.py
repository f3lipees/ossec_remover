from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Regexp
import subprocess
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
Bootstrap(app)

class AgentRemoveForm(FlaskForm):
    agents = TextAreaField('Agent IDs (one per line)', validators=[
        DataRequired(),
        Regexp(r'^[\w-]+(\n[\w-]+)*$', message="Only alphanumeric characters, underscores or hyphens allowed, one per line.")
    ])
    submit = SubmitField('Remove Agents')

def remove_agent(agent_id: str) -> tuple[bool, str]:
    agent_id = agent_id.strip()
    if not agent_id:
        return False, "Empty agent ID"
    try:
        result = subprocess.run(
            ["/var/ossec/bin/manage_agents", "-r", agent_id],
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout.strip()
    except FileNotFoundError:
        return False, "OSSEC manage_agents executable not found at /var/ossec/bin/manage_agents"
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip() or "Unknown error"

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AgentRemoveForm()
    results = None
    if form.validate_on_submit():
        agent_ids = list(dict.fromkeys(line.strip() for line in form.agents.data.strip().splitlines() if line.strip()))
        results = []
        for agent_id in agent_ids:
            success, message = remove_agent(agent_id)
            results.append({'agent': agent_id, 'success': success, 'message': message})
        if not results:
            flash("No valid agent IDs provided.", "warning")
    return render_template('index.html', form=form, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
