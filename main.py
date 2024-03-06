import os
import csv

def read_file_data(input_dir):
    unique_email_ids=set() ##To store unique email ids
    files=os.listdir(os.path.join(input_dir))
    for filename in files:
        if filename.endswith(".dat"):
            try:
                with open(os.path.join(input_dir, filename),"r") as fp:
                    for line in fp:
                        dataList=line.strip().split('\t')
                        email_id=dataList[3]
                        if email_id not in unique_email_ids:##assuming email id is unique, as "id" is duplicacte..Check if email id is already added or not
                            unique_email_ids.add(email_id)
                            yield dataList
            except FileNotFoundError:
                print(f"File {filename}is not present at given Location")
            except Exception as e:
                print(f"Error Occured while opening {filename} file :- {e}")    
        else:
            print("Please check for extension of file {filename}")

def file_process_data(output_dir,data):
    records= total_salary= highest_salary= second_highest_salary= gross_sal= 0 ##Initialzing values to 0 for avg and SecondHighest
    #footer=[]
    op_file=os.path.join(output_dir,'result.csv')
    try:
        with open(op_file,"a",newline="") as fp:
            writer=csv.writer(fp)
            for records,line in enumerate(data):
                if records == 0:
                    line.append("Gross Salary") ##Adding "Gross Salary" Column in header
                    writer.writerow(line)
                else:
                    basic_sal=float(line[-2])
                    allowances=float(line[-1])
                    gross_sal=basic_sal+allowances ##calculate Gross Salary
                    line.append(gross_sal) ##  adding gross sal value in line
                    writer.writerow(line)

                    ##To find out Second Highest Salary
                    if gross_sal > highest_salary:
                        second_highest_salary=highest_salary
                        highest_salary=gross_sal
                    elif gross_sal > second_highest_salary and gross_sal != highest_salary:
                        second_highest_salary = gross_sal

                    total_salary += gross_sal ##adding salary to var to find avg

            ##To add footer avg salary and second Highest
            writer.writerow((f"Second Highest Salary={second_highest_salary}",f"average salary ={total_salary/(records)}"))  
            print(f"Data Written to CSV file. Second Highest Salary: {second_highest_salary}, Average Salary: {total_salary / (records)}")

        #print(f"numrecords {records} and avg {total_salary/(records)} highest {highest_salary} and secondHighest Salary {second_highest_salary}")
    except IOError:
        print(f"Error Occured while writing to {op_file} file :- {e}")   
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    input_dir="inputs"
    output_dir="outputs"
    try:    
        read_data_gen=read_file_data(input_dir)
        write_data=file_process_data(output_dir,read_data_gen)
    except Exception as e:
        print(f"An Error Occured {e}")
        
if __name__ == "__main__":
    main()