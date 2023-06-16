# Open Security Bulletin 🌐🛡️

Welcome to the *Open Security Bulletin* (OSB), a cutting-edge tool that keeps you updated on the latest Common Vulnerabilities and Exposures (CVEs). This system ensures you're never caught off-guard by new vulnerabilities and provides you with comprehensive reports right in your inbox. 📊📧

## 🚀 Getting Started

Before you begin, ensure you have Python installed on your system.

1. Clone the repository to your local machine.

```bash
git clone https://github.com/gpericol/OSB.git
```

2. Navigate to the cloned directory.

```bash
cd open-security-bulletin
```

3. Install the necessary dependencies.

```bash
pip install -r requirements.txt
```

4. You're all set! Run the program.

```bash
python main.py
```

## 🎯 Configuration

Customize the Open Security Bulletin to suit your needs.

- **Credentials:** Before running the program, be sure to set up your email credentials. Rename the config_MODIFY_ME.py file to config.py and replace the placeholder values with your actual email credentials. This ensures that the bulletins are sent from the correct email address. Please handle this file carefully as it contains sensitive information. 🔑🔒
- **Recipient Emails:** You can specify the email addresses that the bulletins are sent to in the `data/mailing.txt` file.
- **Important Services:** You can specify important services in the `data/services.txt` file. Any vulnerabilities related to these services will be specially marked in the bulletins.

## ❤️ Authors

*Open Security Bulletin* has been created with all the love in the world by *Mattia Campanelli* and *Gianluca Pericoli*. 🌎

## 📜 License

This project is licensed under the terms of the GPL v3 License. Please see the [LICENSE](LICENSE) file for more details.

## 🏁 Final Words

Stay informed, stay safe. With *Open Security Bulletin*, the power to anticipate and manage cybersecurity threats is at your fingertips. 

Join us in our quest to make cybersecurity accessible to all. We're proud of what we've built. We hope it serves you well in your cybersecurity journey. Your safety is our success. 🎉🎉🎉

---
