# AIOSQLITE Auto Backup Webhook

This project allows you to automatically back up your `aiosqlite` database to a webhook. It is a simple and efficient solution to ensure your data is always safely stored in external backups.

## Features

- Automatic `aiosqlite` database backup.
- Uploads the backup to a specified webhook URL.
- Simple configuration using a `.env` file.

## Project Structure

- `backup.py`: Main script responsible for creating the backup and sending the data to the webhook.
- `example.env`: Example configuration file containing the required environment variables.

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aiosqlite-auto-backup-webhook.git
```

### 2. Install the Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Configure the `.env` File

Rename the `example.env` file to `.env` and fill in the required information:

```env
WEBHOOK=https://your-webhook.url
```

- **WEBHOOK**: The webhook URL where the backup will be uploaded.

### 4. Run the Script

Start the backup process:

```bash
python backup.py
```

The script will compress the database and upload the file to the URL configured in the `.env` file.

## Configuration Example

The `example.env` file demonstrates how to configure the required variables:

```env
WEBHOOK=https://example.com/webhook
```

## Contributing

Contributions are welcome! If you have suggestions or encounter any issues, feel free to open an *issue* or submit a *pull request*.