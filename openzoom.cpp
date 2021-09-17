#include <chrono>  // chrono::system_clock
#include <ctime>   // time_t, tm, localtime, mktime
#include <fstream>
#include <iomanip>  // put_time
#include <iostream>
#include <sstream>
#include <string>
#include <thread>  // this_thread::sleep_until
#include <vector>

using namespace std;

class Class {
 public:
  string title;
  vector<int> days;
  string time;
  string link;
  Class(string t, vector<int> d, string tm, string l) {
    title = t;
    days = d;
    time = tm;
    link = l;
  }
};

void PrintData(vector<Class> c) {
  cout << "i" << "\t|\t" << "Course" << "\t|\t" << "Days after Sunday" << "\t|\t" 
       << "Sync Time" << "\t|\t" << "Zoom Link" << endl;
  for (int i = 0; i < c.size(); i++) {
    cout << i << ": " << c[i].title << "\t";
    for (int j : c[i].days) {
      cout << j;
      // if it's the last term in the vector, print ""
      // otherwise, print "|" to separate the days
      j != c[i].days[c[i].days.size() - 1] ? cout << "|" : cout << "";
    }
    cout << "\t" << c[i].time << "\t" << c[i].link << endl;
  }
}

// copied from stack overflow
// makes a string into a vector using a delimiter
void split(string const &str, const char delim,
           vector<string> &out) {
  size_t start;
  size_t end = 0;

  while ((start = str.find_first_not_of(delim, end)) != string::npos) {
    end = str.find(delim, start);
    out.push_back(str.substr(start, end - start));
  }
}

int daysAfterSunday(string day) {
  if (day == "Mon") {
    return 1;
  } else if (day == "Tue") {
    return 2;
  } else if (day == "Wed") {
    return 3;
  } else if (day == "Thu") {
    return 4;
  } else if (day == "Fri") {
    return 5;
  } else if (day == "Sat") {
    return 6;
  } else {
    return 7;
  }
}

int main() {
  // ---------------------------------------------------------
  // how many minutes before class should the zoom link open |
  int minutesBeforeClass = 2; //                             |
  // ---------------------------------------------------------

  vector<Class> classes;
  string tempTitle, tempLink, tempDay, tempTime, templine, temp;
  vector<string> tempDaysVector;
  const char daysDelimiter = '|';
  vector<int> daysAfterSundayVector;
  // 1 = Mon, 2 = Tues, 3 = Wed, etc...
  ifstream inputfile;
  ofstream outputfile;
  int rep;

  inputfile.open("classes.txt", ios::in);

  while (getline(inputfile, temp, ',')) {
    stringstream line(temp);
    line >> tempTitle >> tempDay >> tempTime >> tempLink;
    split(tempDay, daysDelimiter, tempDaysVector);
    for (auto day : tempDaysVector) {
      daysAfterSundayVector.push_back(daysAfterSunday(day));
    }
    Class c(tempTitle, daysAfterSundayVector, tempTime, tempLink);
    classes.push_back(c);
    tempDaysVector.clear();
    daysAfterSundayVector.clear();
  }

  inputfile.close();

  PrintData(classes);

  using chrono::system_clock;
  time_t tt = time(NULL);

  // time structure <ptm> = localtime memory location
  struct tm *ptm = localtime(&tt);

  // put_time(struct tm * data type, specifier)
  // https://www.cplusplus.com/reference/iomanip/put_time/ -> specifiers
  // "%X" -> time specifier
  cout << "Current time: " << put_time(ptm, "%X") << '\n';

  vector<int> classesTodayIndex;
  int classIndex = 0;

  // check if there are classes today
  // saves the class index to the classesTodayIndex vector
  for (int i = 0; i < 7; i++) {
    if (i == ptm->tm_wday) {
      for (auto j : classes) {
        for (auto k : j.days) {
          if (k == i) {
            classesTodayIndex.push_back(classIndex);
          }
        }
        classIndex++;
      }
    }
  }

  vector<string> tempClassTimesTodayString;
  vector<int> tempClassTimesTodayInt;
  const char timeDelimiter = ':';

  for (auto i : classesTodayIndex) {
    // cout << classes[i].time << endl;
    split(classes[i].time, timeDelimiter, tempClassTimesTodayString);
    
    // converts string to int
    for (auto &s : tempClassTimesTodayString) {
      stringstream parser(s);
      int x = 0;
      parser >> x;
      tempClassTimesTodayInt.push_back(x);
    }

    // skips opening the zoom link if the time has passed
    if (ptm->tm_hour > tempClassTimesTodayInt[0]) {
      continue;
    }

    ++ptm->tm_hour = tempClassTimesTodayInt[0];
    // change the value of the minutes in the time to 60 if it's originally 0
    // otherwise, retain the value
    tempClassTimesTodayInt[1] == 0 ? tempClassTimesTodayInt[1] = 60 : tempClassTimesTodayInt[1];
    ++ptm->tm_min = tempClassTimesTodayInt[1] - minutesBeforeClass;
    ++ptm->tm_sec = 0;

    this_thread::sleep_until(system_clock::from_time_t(mktime(ptm)));
    system(("start chrome " + classes[i].link).c_str());

    tempClassTimesTodayString.clear();
    tempClassTimesTodayInt.clear();
  }

  return 0;
}