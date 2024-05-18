# Shodan To Discord Webhook (Shodancord)

This is a Python script but yet meant to be a server but fetches data from Shodan using the Shodan API and sends it to a Discord webhook. It can be used to monitor specific queries, such as IP cameras in a particular city, and send screenshots and information about them to a Discord channel.

## Requirements

- Python 3.x
- pip

## Installation

1. Clone the repository:

```sh
git clone https://github.com/PlayerFridei/Shodan-To-Discord-Webhook
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Usage

1. Obtain a Shodan API key from [Shodan](https://account.shodan.io/register).
2. Create a Discord webhook URL for the channel where you want to receive the data. Instructions can be found [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
3. Update the `SHODAN_API_KEY` and `DISCORD_WEBHOOK_URL` variables in the script with your API key and webhook URL.
4. Customize the `SPECIFIC_QUERY` variable in the script to define the specific search query you want to monitor.
5. Run the script:

```sh
python shodancord.py
```

Optional arguments:

- `--debugtest`: Test the Discord webhook with random data.
- `--sleep [hours]`: Set the sleep time in hours between data fetch cycles.
- `--rate-limit [seconds]`: Set the rate limit in seconds between sending each message to the Discord webhook.

## Examples

```sh
python shodancord.py --sleep 12 --rate-limit 2.0
```

This command will make the script wait for 12 hours between each data fetch cycle and 2 seconds between each message sent to the Discord webhook.

```sh
python shodancord.py --debugtest
```
This command will send random data to your discord webhook to test that your webhook is working correctly.

# Disclaimer

By downloading and using this tool, you agree to the following terms:

1. The tool is provided without any warranty, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement.

2. The creator of the tool shall not be liable for any direct, indirect, incidental, special, consequential, or exemplary damages, including but not limited to, damages for loss of profits, goodwill, use, data, or other intangible losses.

3. You understand and acknowledge that the tool is still under development and may not be fully polished. As such, it might contain bugs or other issues that could affect its performance.

4. You understand and acknowledge that the creator of the tool may, at their sole discretion, discontinue support for the tool at any time and without notice. This means that there is no guarantee of ongoing maintenance, updates, or technical assistance.

5. You agree to use the tool at your own risk and understand that the creator of the tool does not provide any assurances regarding its functionality, reliability, or suitability for any purpose.

6. The creator of the tool reserves the right to modify, suspend, or terminate the tool at any time, with or without cause, and without liability to you or any third party.

By downloading and using the tool, you acknowledge that you have read, understood, and agreed to these terms. If you do not agree with any part of these terms, you should not download or use the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
