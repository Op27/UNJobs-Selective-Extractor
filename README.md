# UNJobs-Selective-Extractor

The **UNJobs-Selective-Extractor** is a Python-based tool designed to automate the collection of job listings from the UNJobs website. It not only aggregates a comprehensive list of opportunities but also filters these listings based on user-defined criteria, making it easier to find relevant UN job opportunities.

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
2. When prompted, enter your criteria for job listings (i.e., name of targe country or url).
3. The script will scrape, filter, and save the job listings based on your input.

## Customizing Job Matching Keywords

The **UNJobs-Selective-Extractor** is designed with flexibility in mind, allowing users to customize the criteria for job matching to suit their specific interests and career goals. The core of this customization lies in the ability to modify the list of keywords that the script uses to filter job listings.

### Subject Line for Customization

In the script, the line responsible for defining the keywords for job matching is as follows:

```bash
keywords = ['Data', 'data', 'Information', 'information', 'analysis', 'Analysis', 'Engineer', 'Developer', 'GIS', 'Geographic']
```

This list of keywords is fully customizable. To tailor the job search to your areas of interest, you can modify this list by adding or replacing keywords. For example, if you are interested in job opportunities for coordinator or associate position in the field of GBV, you might replace keywords with such as 'Coordinator', 'Associate', or 'GBV'. 

### How to Customize
To customize the keywords for job matching:
1. Open the script using your preferred text editor or IDE.
2. Locate the keywords line as shown above.
3. Modify the list by adding or removing keywords according to your preferences, ensuring each keyword is enclosed in quotes and separated by commas.
4. Save your changes and run the script as usual to see job listings filtered based on your customized keywords.

By customizing the keywords, you make the UNJobs-Selective-Extractor more relevant to your personal job search, enhancing the tool's utility and effectiveness.



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
