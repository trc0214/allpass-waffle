# Project Title
ALLPASS Waffle! 🧇

## Description
A waffle that assists your study group by offering structure, reorganizing files, AI question answering, and more!

## Installation
Ensure you have Python 3.8 or higher installed. Then, follow these steps:
```
git clone https://github.com/trc0214/allpass-waffle.git
cd ./allpass-waffle
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Environment Variables
Copy the `.env.example` file to `.env` and update the environment variables as needed.
```
cp .env.example .env
```

## Usage
To use the bot, follow these steps:
1. Ensure you have set the `DISCORD_TOKEN` in your `.env` file.
2. Run the bot using the following command:
    ```
    py main.py
    ```
3. Use the following commands in your Discord server:
    - `$load <extension>`: Load a specific cog.
    - `$unload <extension>`: Unload a specific cog.
    - `$reload <extension>`: Reload a specific cog.
    - `/add_category <category_name>`: Add a new category with predefined channels.
    - `/delete_category <category_name>`: Delete an existing category and its channels.

## Contributing
To contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feat/feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, please contact the project maintainer at [timray0214@gmail.com].
