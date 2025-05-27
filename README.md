# Features

- Remove multiple OSSEC agents at once by submitting their IDs in a simple text area.

  ![home_screen](https://github.com/user-attachments/assets/33413a4c-034c-47cd-b399-fc136edfa73d)


# Requirements

- Linux environment with OSSEC installed and accessible at ***/var/ossec/bin/manage_agents.***

- Python 3.8 or higher.

- Python packages:

      pip install requirements.txt

# Installation

- Clone or download the repository to your Linux server running OSSEC.

- Create a Python virtual environment for isolation (recommended):

      python3 -m venv venv
      source venv/bin/activate

# Usage

Start the application:

      python app.py

- Open your web browser and navigate to http://localhost:5000.
- Enter the OSSEC agent IDs you wish to remove, one per line, into the provided text area.
- Submit the form to initiate the removal process.
- Review the results table to confirm which agents were successfully removed and which encountered errors.

# Deployment Recommendations

- Run the application behind a production-ready web server and reverse proxy (Nginx or other).
- Restrict access to the application via network controls or authentication mechanisms to authorized personnel only.
- Regularly update dependencies to incorporate security patches.
- Monitor application logs for unusual activity or errors.

# Security Considerations

- The application uses Flask-WTF to enforce CSRF protection and input validation.
- Agent IDs are strictly validated with a regex pattern to allow only alphanumeric characters, underscores, and hyphens.
- The OSSEC command is invoked with argument lists to prevent shell injection.
- Execution errors are captured and reported without exposing sensitive system information.
- The secret key is generated dynamically for each deployment to enhance session security.

# Troubleshooting

- If the message occurs [TemplateNotFound Error], ensure the templates/index.html file exists relative to app.py.
- If the message occurs [FileNotFoundError on manage_agents], confirm OSSEC is installed and the executable is accessible at ***/var/ossec/bin/manage_agents.***
- If the message occurs [Permission Denied], please verify the application user has execution rights on the OSSEC binaries.
- If the message occurs [Input Validation Errors], provide agent IDs using only letters, numbers, underscores, or hyphens, one per line.

# Contribution

- We value the contribution made by the community, please fork the repository, implement your changes, and submit a pull request for review.
