import { Pipe, PipeTransform } from '@angular/core';
import { Employee } from '../employees/employees';

@Pipe({
  name: 'multifilter'
})
export class MultifilterPipe implements PipeTransform {

  transform(data: Employee[], myInput: string[]): Employee[] {
    if (myInput && myInput.length <= 0) { return data; }
    return data.filter((data) => {
      var matchFound : boolean;
      for (var i = myInput.length - 1; i >= 0; i--) {
        if (data["First Name"].toLowerCase().match(myInput[i])) {
          matchFound = true;
        } else if (data["Last Name"].toLowerCase().match(myInput[i])) {
          matchFound = true;
        } else if (data["Age"].toString().match(myInput[i])) {
          matchFound = true;
        } else if (data["Birth"].match(myInput[i])) {
          matchFound = true;
        } else if (data["Employee ID"].toString().match(myInput[i])) {
          matchFound = true;
        } else if (data["Employment Date"].toString().match(myInput[i])) {
          matchFound = true;
        } else if (data["Department"].toLowerCase().match(myInput[i])) {
          matchFound = true;
        } else if (data["Salary"].toString().match(myInput[i])) {
          matchFound = true;
        } else if (data["Email"].toLowerCase().match(myInput[i])) {
          matchFound = true;
        } else {
          matchFound = false;
          break;
        }
      }
      return matchFound;
    })
  }
  }
