import { Pipe, PipeTransform } from '@angular/core';
import { Employee } from '../employees/employees';

@Pipe({
  name: 'multifilter'
})
export class MultifilterPipe implements PipeTransform {

  transform(data: Employee[], myInput: string): Employee[] {
    if (myInput == "") { return data; }
    return data.filter((data) => {
      var matchFound : boolean;
        if (data["First Name"].toLowerCase().match(myInput)) {
          matchFound = true;
        } else if (data["Last Name"].toLowerCase().match(myInput)) {
          matchFound = true;
        } else if (data["Age"].toString().match(myInput)) {
          matchFound = true;
        } else if (data["Birth"].match(myInput)) {
          matchFound = true;
        } else if (data["Employee ID"].toString().match(myInput)) {
          matchFound = true;
        } else if (data["Employment Date"].toString().match(myInput)) {
          matchFound = true;
        } else if (data["Department"].toLowerCase().match(myInput)) {
          matchFound = true;
        } else if (data["Salary"].toString().match(myInput)) {
          matchFound = true;
        } else if (data["Email"].toLowerCase().match(myInput)) {
          matchFound = true;
        }
      return matchFound;
    })
  }
}
