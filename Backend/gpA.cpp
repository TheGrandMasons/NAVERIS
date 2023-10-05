#include <iostream>
#include <string>
#include <limits>
#include <fstream>
using namespace std;

int main() {
    // Declarations
    const int maxCourses = 100;
    string courseNames[maxCourses];
    int credit[maxCourses];
    string gradeString[maxCourses];
    int numCourses = 0;
    double totalCredits = 0.0, cumulativeCredits = 0.0;
    double totalGradePoints = 0.0, cumulativeGpa = 0.0;
    double gpa = 0.0;
    char addAnother = 'y';


    // Program Start
    cout << "GRADE CALCULATOR ON A 4 POINT GPA SYSTEM." << endl << endl;
    double gpaFromFile = 0.0;
    ifstream inputFile("gpa.txt");
    if (inputFile) {
        inputFile >> gpaFromFile;
        inputFile.close();
        cumulativeGpa = gpaFromFile;
    }


    // Get cumulative gpa
    cout << "Current cumulative GPA value is " << cumulativeGpa << " do you want to edit? (y/n): ";
    cin >> addAnother;
    if (addAnother == 'y' || addAnother == 'Y')
    {
        do {
            cout << "Enter cumulative GPA: ";
            cin >> cumulativeGpa;
            if (cumulativeGpa < 0) {
                cout << "Invalid GPA entered. Please try again." << endl;
            }
        } while (cumulativeGpa < 0);
        do {
            cout << "Enter cumulative credit hours: ";
            cin >> cumulativeCredits;
            if (cumulativeCredits < 0) {
                cout << "Invalid number of credit hours entered. Please try again." << endl;
            }
        } while (cumulativeCredits < 0);
        cin.ignore();
    }


    cout << "Now Lets Gather Scores: \n";
    addAnother = 'y';
        // Get course information from the user
    while (numCourses < maxCourses && (addAnother == 'y' || addAnother == 'Y')) {
        cout << "Enter course name: ";
        cin.ignore(); // Ignore the newline character in the input buffer
        getline(cin, courseNames[numCourses]);

        while(true) {
            cout << "Enter number of credit hours: ";
            cin >> credit[numCourses];
           if(!cin) { // If the input was not an integer
                cout << "Invalid number of credit hours entered. Please try again." << endl;
                cin.clear(); // Clear the error state of the cin
                cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Ignore the remainder of the line
            }
           else if(credit[numCourses] < 0) { // If the input was a negative integer
                cout << "Invalid number of credit hours entered. Please try again." << endl;
            }
            else break; 
        }
        cout << "Enter grade (A, A-, B+, B, B-, C+, C, C-, D, F): ";
        cin >> gradeString[numCourses];


        // Convert grade to numeric value
        double grade = 0.0;
        if (gradeString[numCourses] == "A" || gradeString[numCourses] == "a") {
            grade = 4.0;
        }
        else if (gradeString[numCourses] == "A-" || gradeString[numCourses] == "a-") {
            grade = 3.67;
        }
        else if (gradeString[numCourses] == "B+" || gradeString[numCourses] == "b+") {
            grade = 3.33;
        }
        else if (gradeString[numCourses] == "B" || gradeString[numCourses] == "b") {
            grade = 3.0;
        }
        else if (gradeString[numCourses] == "B-" || gradeString[numCourses] == "b-") {
            grade = 2.67;
        }
        else if (gradeString[numCourses] == "C+" || gradeString[numCourses] == "c+") {
            grade = 2.33;
        }
        else if (gradeString[numCourses] == "C" || gradeString[numCourses] == "c") {
            grade = 2.0;
        }
        else if (gradeString[numCourses] == "C-" || gradeString[numCourses] == "c-") {
            grade = 1.67;
        }
        else if (gradeString[numCourses] == "D" || gradeString[numCourses] == "d") {
            grade = 1.0;
        }
        else if (gradeString[numCourses] == "F" || gradeString[numCourses] == "f") {
            grade = 0.0;
        }
        else {
            cout << "Invalid grade entered. Please try again." << endl;
            continue;
        }


        // Update GPA calculation variables
        totalCredits += credit[numCourses];
        totalGradePoints += grade * credit[numCourses];
        numCourses++;


        // Ask if user wants to add another course
        cout << "Add another course? (y/n): ";
        cin >> addAnother;
    }


    // Calculate and display GPA
    if (numCourses == 0) {
        cout << "No courses entered. GPA cannot be calculated." << endl;
    }
    else {
        if (cumulativeCredits != 0)
        {
            gpa = (totalGradePoints + (cumulativeGpa * cumulativeCredits)) / (totalCredits + cumulativeCredits);
        }
        else
        {
            gpa = (totalGradePoints / totalCredits);
        }
        cout << endl << "GPA: " << gpa << endl;
    }


    // Write the calculated GPA to a file
    ofstream outputFile("gpa.txt");
    outputFile << gpa;
    outputFile.close();
    return 0;
}
