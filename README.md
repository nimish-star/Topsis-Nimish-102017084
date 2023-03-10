Submitted by:   
Name: **Nimish Lakhmani**   
Roll No: **102017084**  
Group: **3CS4** 

## Installation
```pip install Nimish-102017084-Topsis```

## How to use it?
Open terminal Write:
```Topsis <inputFilename.csv> <"Weights"> <"Impacts"> <outputFilename.csv>```


* Enter the three parameters in three lines:
  * .csv filename, followed by .csv extension
  * values of weights, each separated by comma(,)
  * values of impacts, either '+' or '-', each separated by comma(,) 
  
bash
  sample.csv
  0.25,0.25,0.25,0.25
  -,+,+,+




## Example of input & output

### Input:

* sample.csv file, depicts the dataset of mobile phones having varying features.

| Model | Price (in $) | Storage Space (in GB) | Camera (in MP)| Looks | 
| :---------------: | :---------------: | :---------------: | :---------------: | :---------------: |
| M1 | 250 | 16 | 12 | Excellent |
| M2 | 200 | 16 | 8 | Average |
| M3 | 300 | 32 | 16 |  Good |
| M4 | 275 | 32 | 8 |  Good |
| M5 | 225 | 16 | 16 |  Below Average |

* weights = [0.25,0.25,0.25,0.25]  
* impacts = [-,+,+,+]

### Output:

| Model | Price (in $) | Storage Space (in GB) | Camera (in MP)| Looks | Topsis Score | Rank | 
| :---------------: | :---------------: | :---------------: | :---------------: | :---------------: | :---------------: | :---------------: |
| M1 | 250 | 16 | 12 | Excellent | 0.526983 | 3 |
| M2 | 200 | 16 | 8 | Average | 0.190599 | 5 |
| M3 | 300 | 32 | 16 |  Good | 0.809401 | 1 |
| M4 | 275 | 32 | 8 |  Good | 0.688168 | 2 |
| M5 | 225 | 16 | 16 |  Below Average | 0.422630 | 4 |





## Important Points

* The first column is not considered while solving the MCDM Problem. Make sure the csv file follows the format as shown in sample.csv.
* Any column (from 2nd to last) containing categorical values is converted into numeric column .

## License

[MIT](https://choosealicense.com/licenses/mit/)