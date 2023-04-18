import { Pipe, PipeTransform } from '@angular/core';
import { Employee } from '../employees/employees';

@Pipe({
  name: 'multifilter'
})
export class MultifilterPipe implements PipeTransform {

  transform(data: Employee[], myInput: string): Employee[] {
    if (myInput === undefined) { console.log("bruh"); return data; }
    return data.filter((data) => {
      console.log("PIng poNG")
      var matchFound : boolean;
        if (data["First Name"].toLowerCase().includes(myInput)) {
          matchFound = true;
        } else if (data["Last Name"].toLowerCase().includes(myInput)) {
          matchFound = true;
        } else if (data["Age"].toString().includes(myInput)) {
          matchFound = true;
        } else if (data["Birth"].includes(myInput)) {
          matchFound = true;
        } else if (data["Employee ID"].toString().includes(myInput)) {
          matchFound = true;
        } else if (data["Employment Date"].toString().includes(myInput)) {
          matchFound = true;
        } else if (data["Department"].toLowerCase().includes(myInput)) {
          matchFound = true;
        } else if (data["Salary"].toString().includes(myInput)) {
          matchFound = true;
        } else if (data["Email"].toLowerCase().includes(myInput)) {
          matchFound = true;
        }
      console.log(myInput)
      return matchFound;
    })
  }


  // transform(data: Employee[], myInput: string[]): Employee[] {
  //   if (myInput === undefined || myInput.length == 0) return data;
  //   return data.filter((data) => {
  //     var matchFound : boolean;
  //     for (let i = 0; i < myInput.length; i++) {
  //       if (data.firstName.toLowerCase().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Last Name"].toLowerCase().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Age"].toString().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Birth"].includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Employee ID"].toString().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Employment Date"].toString().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Department"].toLowerCase().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Salary"].toString().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       } else if (data["Email"].toLowerCase().includes(myInput[i])) {
  //         matchFound = true;
  //         break;
  //       }
  //     }
  //     console.log(myInput)
  //     return matchFound;
  //   })
  // }
}
