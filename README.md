**Design Specification for File Data Processor**

**Objective:**
This Python script is designed to read data from multiple input files located in a specific directory, process the data, and generate an output CSV file with additional calculations and footer details.

**Components:**

1. **Input Data Reading Module:**
   - Responsible for reading data from multiple input files in a specified directory.
   - Iterates through each file, reads data line by line, and yields each row as a list.
   - Checks for duplicate email IDs to ensure uniqueness.

2. **Output Data Process Module:**
   - Writes processed data to a CSV file in the specified output directory.
   - Adds a "Gross Salary" column header.
   - Calculates and appends gross salary to each row based on basic salary and allowances.
   - Determines the second highest salary and calculates the average salary.
   - Writes the footer with the second highest salary and average salary to the CSV file.

3. **Main Module:**
   - REsponsible for the execution of the Input Data Reading and Output Data Writing modules.
   - Specifies input and output directories.
   - Invokes the functions to read data from files, process it, and write the result to the CSV file.

**Assumptions:**
- Each input file is in tab-separated format with data fields and with ".dat" extension.
- Email ID (dataList[3]) is assumed to be unique for each record.
- Gross salary is calculated as the sum of basic salary and allowances.
- To get second highest salary records are more than 2

**Coding Patterns and Best Practices:**
- Use of generator function to process input data line by line, ensuring memory efficiency.
- Implementation of modular design to separate concerns and improve maintainability.
- Proper error handling for file operations, such as file opening and reading.
- Informative comments to explain the logic and functionality of each part of the code.
- Utilization of Python's built-in functions and data structures for efficient data processing and manipulation.

**Conclusion:**
The File Data Processor script efficiently processes data from multiple input files, performs necessary calculations, and generates an output CSV file with detailed footer information.
By following coding patterns and best practices, the script ensures readability, maintainability, and reliability in handling file processing tasks.
