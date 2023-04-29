import { Component, OnInit } from '@angular/core';
import { Employee } from '../employees/employees';
import { EmployeeService } from '../employees/employees.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-employee-add',
  templateUrl: './employee-add.component.html',
  styleUrls: ['./employee-add.component.scss']
})
export class EmployeeAddComponent implements OnInit {

  // 
  
  employee = {
    id: null
  }

  successMessage: string = "";

  constructor(private employeeService: EmployeeService) {}

  ngOnInit(): void {
      
  }

  addEmployee(employeeForm: NgForm) {
    this.employee.id = this.employee["Employee ID"]
    this.employeeService.addEmployee(this.employee).subscribe((data) => {
      this.successMessage = 'Employee Added to Database.';
    })
    console.log(this.employee)
  }

}
