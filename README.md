# UNJobs-Selective-Extractor

The **UNJobs-Selective-Extractor** is a Python-based tool designed to automate the collection of job listings from the UNJobs website. It aggregates a comprehensive list of job opportunities and offers users the flexibility to filter these listings through interactive customization. Users can tailor their search to focus on opportunities that match either a set of default criteria or their specific interests and career goals. This feature ensures a personalized job hunting experience.

https://github.com/Op27/UNJobs-Selective-Extractor/assets/39921621/7d947b4c-5779-47cc-817a-8353eff03392

## Features
- **Data Extraction**: Automatically scrapes job listings from the UNJobs website.
- **Selective Filtering**: Users can specify criteria to filter the extracted job listings, focusing on opportunities that match their skills and interests.
- **Export Functionality**: Extracted and filtered job data can be saved in a structured format, facilitating easy review and application.

## Installation

To set up **UNJobs-Selective-Extractor** on your machine, follow these steps:

1. Ensure you have Python 3.6+ installed on your system.
2. Clone this repository to your local machine using Git:
    ```bash
    git clone https://github.com/Op27/UNJobs-Selective-Extractor.git
    ```
3. Navigate into the cloned repository's directory:
    ```bash
    cd UNJobs-Selective-Extractor
    ```
4. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start using the **UNJobs-Selective-Extractor**, follow these instructions:

1. Launch the script with Python:
    ```bash
    python main.py
    ```
2. When prompted, enter your criteria for job listings (e.g., name of target country or URL). For example, you can respond like the following:
    ```bash
    🌐  Enter the country name or the full URL for job listing -> Ukraine
    ```
3. You will be asked if you want to use the default keywords for filtering jobs or enter your own. The default keywords are [Data, data, Information, information, analysis, Analysis, Engineer, Developer, GIS, Geographic].
   - If you choose to enter your customized keywords, follow the prompt to input your custom keywords separated by commas. For example, you can respond like the following:
        ```bash
        Enter your custom keywords, separated by commas (e.g., Analyst, Software, Research): Coordinator, Assistant
        ```
5. The script will scrape, filter, and save the job listings based on your inputs.

### Configuring the Save Location
To ensure the UNJobs-Selective-Extractor saves files where you can easily find them, you'll need to set the correct save path in the script:

In main.py, find this line:
```bash
file_path = rf'INSERT_PATH_TO_USER_FOLDER_HERE/scraping_unjobs/{file_name}'
```

Replace `INSERT_PATH_TO_USER_FOLDER_HERE` with the path to where you want the files saved. For example:

- On Windows: C:/Users/YourName/Documents/UNJobs/{file_name}
- On Mac/Linux: /Users/YourName/Documents/UNJobs/{file_name}

<br>Remember to change `YourName` to your actual username.

## Customizing Job Matching Keywords

The **UNJobs-Selective-Extractor** offers flexibility in filtering job listings by allowing users to customize the job matching keywords interactively.

### Interactive Customization
Upon running the script, users are prompted to decide whether to use the default set of keywords or to input their own. This feature ensures that users can tailor the job search to their specific interests and career goals without manually editing the script.

- **Default Keywords**: The default set includes [Data, data, Information, information, analysis, Analysis, Engineer, Developer, GIS, Geographic].
- **Entering Custom Keywords**: If opting for custom keywords, you'll be prompted to enter them separated by commas (e.g., Coordinator, Associate, GBV).

By engaging with this interactive feature, you enhance the tool's utility, making your job search more targeted and efficient.


## Disclaimer

### Web Scraping Legal Considerations
The **UNJobs-Selective-Extractor** is designed for the purpose of aggregating job listings from the publicly accessible UNJobs website. While web scraping for non-commercial, informational purposes is generally permissible, it is crucial for users to respect privacy laws and the terms of service of the target website.

- **Terms of Service Compliance**: Users are encouraged to review and comply with the terms of service of the UNJobs website or any other sources they intend to scrape. These terms outline permissible use and restrictions related to accessing and using the website's content.

### User Responsibility
The deployment and application of **UNJobs-Selective-Extractor** rest entirely with the user. The creators and contributors of this project disclaim any legal liability or responsibility for the use of the tool and the outcomes of such use. Users are accountable for employing **UNJobs-Selective-Extractor** in a lawful manner, adhering to all relevant laws and regulations applicable to their situation, including, but not limited to, privacy and data protection laws.

By using **UNJobs-Selective-Extractor**, you acknowledge and agree to these terms, taking full responsibility for your actions and the compliance of your activities with legal standards.


## Contributing

Contributions to the **UNJobs-Selective-Extractor** are welcome! If you have suggestions for improvements or new features, feel free to:

- Open an issue to discuss your idea.
- Fork this repository, make your changes, and submit a pull request.

Please ensure your contributions adhere to the project's coding standards and are accompanied by appropriate documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
