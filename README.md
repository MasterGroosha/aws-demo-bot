# AWS Lambda Demo Telegram Bot

This is a simple demo Telegram bot which you can deploy on AWS Lambda (1M requests per month free)

## Deploy on AWS Lambda

1. Log into your AWS account.
2. Go to Lambda service page.
3. Click "Create function".
4. Enter any name for your new function, use Python 3.11 as Runtime and x86_64 architecture.
5. In "Advanced settings", check "Enable function URL". Confirm your choices by clicking "Create function".
6. In function overview, open "Code" tab and press "Upload from" on the right.
7. Now in this repository, run `build.sh` script in the current directory. A `bot.zip` file should appear next to 
the shell script.
8. Upload `bot.zip` to AWS.
9. In function overview again, open "Configuration" tab and click "Environment variables". Create a new variable 
called `BOT_TOKEN` and your bot token as value.
10. Copy function URL from function overview.
11. Create URL: `https://api.telegram.org/bot<TOKEN>/setWebhook?url=<URL>`. Replace `<TOKEN>` with your bot token and 
<URL> with function URL you got from the previous step.
12. Open this URL in web browser, you should see "Webhook was set" in JSON payload.
13. Go to your bot on Telegram and send `/start`.
